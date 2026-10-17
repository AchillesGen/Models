#!/usr/bin/env python3
"""Impact of the running-width prescription on the model default (V13).

Sherpa can only carry a FIXED Delta width -- Comix reads it from the DECAY block
and applies it to the s- and u-channel propagator alike -- so this has to be done
with the analytic amplitude.  Everything here is the same UFO, the same
parameters and the same grid; only Gamma(s) changes.

GAMMA_0 IS READ FROM THE UFO, NOT HARD-CODED.  It is GamNPi + GamNGam, the sum
of the partial widths the card carries, because that is the resonance Comix is
handed through the DECAY block; forcing it is what makes the analytic engine and
Sherpa comparable (unforced, wprod_from_ufo.py takes Gamma_Delta from the
WDeltaP external instead, and the two engines can disagree).

Through V12 that sum was 0.11766 -- the BREIT-WIGNER partial widths, 117 MeV and
0.66 MeV, sitting at the POLE mass 1.209 while WDeltaP carried the pole width
0.102.  V13 moved the partial widths to the pole convention too (ChiPT.fr:1220-
1265), so the sum is now 0.102 EXACTLY and equals WDeltaP; the mismatch that
made one of the two numbers look stale is gone.  Deriving GAM0 from the card
rather than restating it here is what keeps that true through the next change.
"""
import csv, os, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from fig33_from_ufo import load_ufo, parameter_namespace
import wprod_from_ufo as W

UFO   = os.environ.get('UFO', 'ChiPT_UFO_V13')
GRID  = tuple(int(x) for x in os.environ.get('GRID', '10,6,6,5').split(','))

# PSET=pole (default) runs the Delta the UFO ships, which from V13 is the POLE
# parametrisation: M = 1.209, Gamma = 102 MeV, the PDG pole position 1210 - 50i,
# with the partial widths scaled to it at fixed branching ratio.
# PSET=bw substitutes the BREIT-WIGNER numbers -- PDG 2024 Delta(1232) listings,
# M = 1.232, Gamma(N pi) = 117 MeV, B(N gamma) = 0.56% giving 0.66 MeV.
#
# THE COUPLINGS FOLLOW, they are not held fixed.  From V10 hD, G1, G2, C4AN and
# C6AN are INTERNAL and derived from MDelta and the two partial widths
# (ChiPT.fr:1682-1702), and parameter_namespace resolves externals before
# internals -- so overriding the externals on the loaded UFO here re-derives
# every coupling at the new parametrisation, which is the honest comparison.
# Holding them fixed would put a ~7% Delta-strength shift on top of the
# lineshape change.
PSET  = os.environ.get('PSET', 'pole')
BWSET = {'MDelta': 1.232, 'GamNPi': 0.117, 'GamNGam': 0.00066}
OUT   = os.environ.get('OUT', 'width_study_V13%s.csv'
                       % ('' if PSET == 'pole' else '_' + PSET.upper()))

P, V = load_ufo(UFO)
if PSET == 'bw':
    _tot = BWSET['GamNPi'] + BWSET['GamNGam']
    for p in P.all_parameters:
        if p.name in BWSET:
            p.value = BWSET[p.name]
        elif p.name.startswith('WDelta'):    # every charge state
            p.value = _tot
elif PSET != 'pole':
    raise SystemExit("PSET must be 'pole' or 'bw', got %r" % PSET)
ns = parameter_namespace(P)

def _rp(x):
    return float(x.real) if isinstance(x, complex) else float(x)

# Gamma_0 = the sum of the partial widths the card carries; see the note above.
GAM0 = _rp(ns['GamNPi']) + _rp(ns['GamNGam'])
if abs(GAM0 - _rp(ns['WDeltaP'])) > 1e-9:
    print("note: GamNPi + GamNGam = %.6f but WDeltaP = %.6f -- the vertex and the"
          " propagator describe different resonances in this UFO"
          % (GAM0, _rp(ns['WDeltaP'])))
ns['WDeltaP'] = GAM0
ff = W.form_factors(ns, os.path.exists(os.path.join(UFO, 'form_factors.py')))

def run(ch, enu, edw, wmax, bwr=5.06773):
    opt = dict(born=True, delta=True, dwidth=True, wwidth=True,
               wmax=wmax, mmu=0.10566, edw=(edw or False), bwr=bwr)
    return W.sigma(ch, enu, V, ns, ff, opt, GRID, False) * 1e8   # -> 1e-38 cm^2

# The nine energies width_study_V12.csv was produced on.  plot_delta_width.py
# interpolates R(E) from these onto the Sherpa grid, so thinning them coarsens
# the dashed curves; the file had drifted to five at some point after that run.
# Overrides for running_width_factor.py, which needs only the fixed width ('')
# and HNV ('hnv'), on a denser and wider grid, with and without the W cut:
#     ENERGIES=0.3,0.35,...  EDWS=,hnv  WMAXES=1.4,none  EXTRAS=0
# The defaults reproduce width_study_V13*.csv and the App. F figure.
def _env_list(name, default, conv):
    v = os.environ.get(name)
    return default if v is None else [conv(x) for x in v.split(',')]
ENERGIES = _env_list('ENERGIES', [0.35, 0.45, 0.5, 0.6, 0.75, 1.0, 1.25, 1.5, 1.6],
                     float)
EDWS     = _env_list('EDWS', ['', 'x', 'hnv', 'bw'], str)
WMAXES   = _env_list('WMAXES', [1.4], lambda x: None if x == 'none' else float(x))
EXTRAS   = os.environ.get('EXTRAS', '1') != '0'
rows, t0 = [], time.time()

def emit(**kw):
    rows.append(kw)
    print("  %-5s E=%.3f  %-5s wmax=%-4s R=%-5s -> %9.5f   [%4.0fs]"
          % (kw['channel'], kw['E_nu'], kw['edw'] or 'fixed',
             kw['wmax'], kw['bwr_fm'], kw['sigma'], time.time() - t0), flush=True)

for wm in WMAXES:
    for ch in ('ppip', 'ppi0', 'npip'):
        for e in ENERGIES:
            for edw in EDWS:
                emit(channel=ch, E_nu=e, edw=edw, wmax=wm, bwr_fm=1.0,
                     sigma=run(ch, e, edw, wm))

if EXTRAS:
    for e in (1.0, 1.5):
        for edw in EDWS:
            emit(channel='ppip', E_nu=e, edw=edw, wmax=None, bwr_fm=1.0,
                 sigma=run('ppip', e, edw, None))
    for e in (1.0, 1.5):
        for Rfm in (0.5, 1.5):
            emit(channel='ppip', E_nu=e, edw='bw', wmax=1.4, bwr_fm=Rfm,
                 sigma=run('ppip', e, 'bw', 1.4, bwr=5.06773 * Rfm))

with open(OUT, 'w', newline='') as f:
    f.write("# sigma in 1e-38 cm^2, UFO %s, pset %s, M_Delta = %.4f, "
            "Gamma_0 = %.5f GeV, hD = %.6f, grid %s, m_mu on\n"
            % (UFO, PSET, _rp(ns['MDelta']), GAM0, _rp(ns['hD']),
               ','.join(map(str, GRID))))
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print("wrote", OUT, len(rows), "rows")
