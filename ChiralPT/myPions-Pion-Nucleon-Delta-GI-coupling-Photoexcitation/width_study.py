#!/usr/bin/env python3
"""Impact of the running-width prescription on the model default (V12).

Sherpa can only carry a FIXED Delta width -- Comix reads it from the DECAY block
and applies it to the s- and u-channel propagator alike -- so this has to be done
with the analytic amplitude.  Everything here is the same UFO, the same
parameters and the same grid; only Gamma(s) changes.

Gamma_0 is forced to GamNPi + GamNGam = 0.11766, the value the shipped param
card carries.  The UFO's own WDeltaP external is stale at 0.102 and that is what
wprod_from_ufo.py picks up by default, so an unforced analytic run is NOT
comparable with Sherpa.
"""
import csv, os, sys, time
import numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, '.')
from fig33_from_ufo import load_ufo, parameter_namespace
import wprod_from_ufo as W

UFO   = 'ChiPT_UFO_V12'
GRID  = tuple(int(x) for x in os.environ.get('GRID', '10,6,6,5').split(','))
GAM0  = 0.11766                       # GamNPi + GamNGam, as in the param card
OUT   = os.environ.get('OUT', 'width_study_V12.csv')

P, V = load_ufo(UFO)
ns = parameter_namespace(P)
ns['WDeltaP'] = GAM0
ff = W.form_factors(ns, os.path.exists(os.path.join(UFO, 'form_factors.py')))

def run(ch, enu, edw, wmax, bwr=5.06773):
    opt = dict(born=True, delta=True, dwidth=True, wwidth=True,
               wmax=wmax, mmu=0.10566, edw=(edw or False), bwr=bwr)
    return W.sigma(ch, enu, V, ns, ff, opt, GRID, False) * 1e8   # -> 1e-38 cm^2

ENERGIES = [0.5, 0.75, 1.0, 1.25, 1.5]
EDWS     = ['', 'x', 'hnv', 'bw']
rows, t0 = [], time.time()

def emit(**kw):
    rows.append(kw)
    print("  %-5s E=%.3f  %-5s wmax=%-4s R=%-5s -> %9.5f   [%4.0fs]"
          % (kw['channel'], kw['E_nu'], kw['edw'] or 'fixed',
             kw['wmax'], kw['bwr_fm'], kw['sigma'], time.time() - t0), flush=True)

for ch in ('ppip', 'ppi0', 'npip'):
    for e in ENERGIES:
        for edw in EDWS:
            emit(channel=ch, E_nu=e, edw=edw, wmax=1.4, bwr_fm=1.0,
                 sigma=run(ch, e, edw, 1.4))

# uncut, where the width choice is not hidden by the W < 1.4 cut
for e in (1.0, 1.5):
    for edw in EDWS:
        emit(channel='ppip', E_nu=e, edw=edw, wmax=None, bwr_fm=1.0,
             sigma=run('ppip', e, edw, None))

# Blatt-Weisskopf radius sensitivity
for e in (1.0, 1.5):
    for Rfm in (0.5, 1.5):
        emit(channel='ppip', E_nu=e, edw='bw', wmax=1.4, bwr_fm=Rfm,
             sigma=run('ppip', e, 'bw', 1.4, bwr=5.06773 * Rfm))

with open(OUT, 'w', newline='') as f:
    f.write("# sigma in 1e-38 cm^2, UFO %s, Gamma_0 = %.5f GeV, grid %s, m_mu on\n"
            % (UFO, GAM0, ','.join(map(str, GRID))))
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader(); w.writerows(rows)
print("wrote", OUT, len(rows), "rows")
