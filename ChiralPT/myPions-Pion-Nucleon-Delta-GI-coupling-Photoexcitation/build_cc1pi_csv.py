#!/usr/bin/env python3
"""
build_cc1pi_csv.py -- one CSV holding everything needed to replot the CC
single-pion comparison, and the figure drawn from it.

    cc1pi_all_channels.csv     model + data + errors, long format
    cc1pi_all_channels.pdf/png the figure

WHY THERE ARE TWO MODEL COLUMNS.  The ANL/BNL sets used here are the ones with
the hadronic invariant-mass cut W < 1.4 GeV, so a model curve has to carry the
same cut.  SHERPA CANNOT APPLY IT: its "Mass" invariant-mass selector is inert
for this process.  Verified rather than assumed -- with the selector present at
W < 1.4 and at W < 1.2, both globally and as a per-process `Selectors:` list, the
integrated cross section is identical to the uncut one to six digits:

    no cut  1.01653e-08     W < 1.4  1.01653e-08     W < 1.2  1.01653e-08

There is no flavour filter in the selector code -- Combined_Selector::Initialize
throws if a selector name is unknown, and it does not, so IMass_Selector IS
constructed and attached; PHASIC++/Selectors has no IsHadron/Strong test on the
way in.  A cut BELOW the pi-N threshold does reach the phase space (it crashes
PeakedDist), which shows the lower limit propagates through Cut_Data while the
upper limit only ever acts inside IMass_Selector::Trigger.  The most likely
mechanism is the mapped-process bypass in Process_Base:

    void Process_Base::SetSelector(const Selector_Key &key)
    { if (IsMapped()) return; ... }
    bool Process_Base::Trigger(const Vec4D_Vector &p)
    { if (IsMapped() && LookUp()) return Selector()->Result(); ... }

so a mapped process retains a selector that was never initialised.  That
is a Sherpa-side question, not a model one.

So: sigma_sherpa_uncut_ub is what Sherpa actually produces, and
sigma_model_wcut_ub is the SAME model integrated with the cut by
wprod_from_ufo.py.  COMPARE THE DATA AGAINST THE WCUT COLUMN.

MUON MASS.  Both engines now run with a MASSIVE muon (m = 0.10566 GeV): the run
card carries 13: {Massive: true} and wprod_from_ufo.py is called with
mmu = MMU.  Everything before 2026-08-15 in this project was massless -- the UFO
always had MMU right, but the card and the analytic default were overriding it.
It is not a small correction at bubble-chamber energies; sigma(massive)/
sigma(massless) for ppip runs 0.059, 0.393, 0.726, 0.934, 0.975, 0.982 at
E_nu = 0.4, 0.5, 0.625, 0.875, 1.25, 1.5.  Threshold moves to E_nu = 0.277 GeV.

The two engines agree with the mass on: ppip at 0.875 GeV gives 4.212025e-09
(Sherpa) against 4.21245e-09 (analytic), and 6.104665e-09 against 6.09546e-09 at
1.25.  Turning the mass back off reproduces the previous massless numbers to
every printed digit, so the phase-space refactor is clean.

INDUCED PSEUDOSCALAR, and PCAC.  V7 adds the fourth Lorentz structure of the
nucleon weak vertex, q^mu gamma5, on BOTH the W and the Z, with

    F_P(Q^2) / F_A(Q^2) = 2 MN / (Q^2 + mpi^2)

fixed by PCAC / off-diagonal Goldberger-Treiman -- no free parameter.  The 2 MN
sits in the coupling and 1/(Q^2+mpi^2) in the form factor, which also keeps the
structures separate: with the identical prefactor FeynRules merged the
pseudoscalar into the axial structure and produced one structure carrying two
form factors, the sympy Mul that Sherpa-generate-model rejects.  The charged
current uses the pi+ mass and the neutral current the pi0; the NC axial current
of the nucleon is pure isovector, so it carries the same pole.

PCAC IS NOW SATISFIED, verified on the generated vertices rather than assumed.
Contracting q_mu into the vertex must give a result suppressed like
mpi^2/(Q^2+mpi^2); measured against that prediction at Q^2 = 0.05, 0.2, 0.5, 1.0:

    charged current  0.28037 0.08875 0.03750 0.01911   (predicted, to all digits)
    neutral current  0.26706 0.08349 0.03516 0.01789   (predicted, to all digits)

The overall sign was FIXED by this test, not chosen: the opposite sign ENHANCES
the contraction by 1 + Q^2/(Q^2+mpi^2) = 1.720, 1.911, 1.963, 1.981 instead.

This matters only because the muon is now massive: q^mu contracted with the
lepton tensor is proportional to m_mu^2, so the whole term is identically zero
for a massless lepton.

C6A ON THE DELTA.  V8 adds the q^alpha q^mu structure of the N -> Delta axial
current, PCAC-tied to C5A by C6A = C5A MN^2/(Q^2 + mpi^2).  Its normalisation
C6AN is CALIBRATED, not assumed: the model's C5A comes from the gauged
Pascalutsa coupling rather than a plain g^{alpha mu} structure, so the ratio is
not 1 by inspection.  Contracting q_mu into the axial N -> Delta structures with
the Rarita-Schwinger leg projected on shell, and requiring the residue to be
mpi^2/(Q^2+mpi^2), gives

    C6AN = 1.520000  at Q^2 = 0.05, 0.1, 0.2, 0.5, 1.0, 2.0   (spread 3.5e-16)

and the residue then reproduces the PCAC prediction to all printed digits.  That
value equals hD, and not by accident: C5A carries hD through the gauged coupling
and the C6A operator does not.  IF hD CHANGES, RE-RUN THE CALIBRATION
(see tools/pcac_delta.py).  Note the Rarita-Schwinger leg MUST be projected on
shell for this test: without it the unphysical spin-1/2 components make C6A look
orthogonal to the rest and the fit returns 0.

STILL MISSING: the separate PP topology (W -> pi* -> pipi NN).  The pion pole is
put in here as an effective operator with the propagator absorbed into a form
factor, the same trick FrhoCT uses -- FeynRules cannot export the two-point W-pi
mixing (the UFO has no two-point vertices at all), so PCAC is imposed by
construction rather than emerging from gauging, which is a weaker statement than
the CVC story.

HOW WELL SHERPA AND THE ANALYTIC AGREE.  Below ~0.65 GeV the W cut removes almost
nothing, so agreement there is an end-to-end test of the model and of the FVND
form factor through Sherpa's own plugin.  Above that the two columns legitimately
differ by the size of the real W > 1.4 tail, which is negligible for ppip (FVND
damps high Q^2, and high Q^2 correlates with high W) and substantial for ppi0
and npip.

MODEL: ChiPT_UFO_V8, regenerated from ChiPT.fr on 2026-08-15.  Carries CKM, the
weak nucleon form factors, the CVC vector N -> Delta transition WITH its dipole
FVND, CVC on the pion-in-flight and contact terms, Adler's C4A = -C5A/4, the
spin-average shift (hD 0.76 -> 1.52, G1 6.061 -> 3.0305, G2 2.414 -> 1.207, with
g*h and hence Fig. 33 preserved exactly), and the IsoVecSource sign fix that puts
the weak vector N -> Delta transition on the sign CVC requires.

Verified on V6: internal CVC ratio +1.00000000 (residual 1.2e-16); photoproduction
bit-identical to ChiPT_UFO_All in all four charge channels.

NOT included: axND, the 3.3% trim that would move C5A(0) from the model's
predicted 1.241 to the phenomenological 1.2.
"""

import csv
import os

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D

UB = 1e8                      # microbarn -> 1e-38 cm^2
CHANNEL_OF = {"14 2212 -> 13 2212 211": "ppip",
              "14 2112 -> 13 2212 111": "ppi0",
              "14 2112 -> 13 2112 211": "npip"}
TITLE = {'ppip': r'$\nu_\mu p\to\mu^-p\,\pi^+$',
         'ppi0': r'$\nu_\mu n\to\mu^-p\,\pi^0$',
         'npip': r'$\nu_\mu n\to\mu^-n\,\pi^+$'}
ISO = {'ppip': 'pure I=3/2', 'ppi0': 'I=3/2+1/2', 'npip': 'I=3/2+1/2'}
COLOR = {'ppip': '#2a78d6', 'ppi0': '#117733', 'npip': '#e8710a'}
DASH = {'ppip': (0, ()), 'ppi0': (0, (5.0, 2.0)), 'npip': (0, (1.5, 1.7))}
MARK = {'ANL': 'o', 'BNL': 's'}
INK, GREY = '#111111', '#8a8a8a'
CH = ['ppip', 'ppi0', 'npip']


def read_sherpa(path='w_scan_results.csv'):
    out = {}
    for r in csv.DictReader(l for l in open(path) if not l.startswith('#')):
        ch = CHANNEL_OF.get(r['process'])
        if ch is None or r.get('wcut', 'none') != 'none':
            continue
        out[(ch, round(float(r['E_nu']), 4))] = (float(r['sigma_ub']),
                                                 float(r['dsigma_ub']))
    return out


ANALYTIC_LOG = os.environ.get('CHIPT_ANALYTIC_LOG', 'analytic_scan.log')


def read_analytic(path=None):
    path = path or ANALYTIC_LOG
    out = {}
    for line in open(path):
        f = line.split()
        if len(f) == 3:
            out[(f[0], round(float(f[1]), 4))] = float(f[2])
    return out


def read_data(path='anl_bnl_cc1pip.csv'):
    """ANL/BNL, W<1.4, Wilkinson re-analysis, keyed by channel."""
    out = {}
    for r in csv.DictReader(l for l in open(path) if not l.startswith('#')):
        if r['wcut'] != '1.4' or r['correction'] != 'wilkinson':
            continue
        out.setdefault(r['channel'], []).append(
            (float(r['E_lo']), float(r['E_hi']), float(r['E_mid']),
             float(r['sigma_ub']), float(r['dsigma_ub']), r['experiment']))
    for v in out.values():
        v.sort()
    return out


def build(out='cc1pi_all_channels.csv'):
    sh, an, dat = read_sherpa(), read_analytic(), read_data()
    energies = sorted({e for _, e in an})
    rows = []
    for ch in CH:
        for e in energies:
            a = an.get((ch, e))
            s, ds = sh.get((ch, e), (None, None))
            # nearest data bin containing this energy, if any
            d = de = None
            dexp = dlo = dhi = ''
            for elo, ehi, em, xs, dxs, exp in dat.get(ch, []):
                if elo <= e < ehi:
                    d, de, dexp, dlo, dhi = xs, dxs, exp, elo, ehi
                    break
            rows.append(dict(
                channel=ch, process=[k for k, v in CHANNEL_OF.items() if v == ch][0],
                isospin=ISO[ch], E_nu=e,
                sigma_model_wcut_ub=a, sigma_model_wcut_1e38cm2=a * UB if a else None,
                sigma_sherpa_uncut_ub=s, dsigma_sherpa_uncut_ub=ds,
                data_experiment=dexp, data_E_lo=dlo, data_E_hi=dhi,
                data_sigma_ub=d, data_dsigma_ub=de,
                data_sigma_1e38cm2=d * UB if d else None,
                data_dsigma_1e38cm2=de * UB if de else None,
                ratio_data_over_model=(d / a) if (d and a) else None))
    cols = ["channel", "process", "isospin", "E_nu",
            "sigma_model_wcut_ub", "sigma_model_wcut_1e38cm2",
            "sigma_sherpa_uncut_ub", "dsigma_sherpa_uncut_ub",
            "data_experiment", "data_E_lo", "data_E_hi",
            "data_sigma_ub", "data_dsigma_ub",
            "data_sigma_1e38cm2", "data_dsigma_1e38cm2",
            "ratio_data_over_model"]
    with open(out, 'w') as f:
        f.write("# CC single-pion production off the free nucleon.\n"
                "# model: ChiPT_UFO_V8 (CKM, weak nucleon form factors, CVC vector\n"
                "#        N->Delta WITH the FVND dipole, CVC on pion-in-flight and\n"
                "#        contact, Adler C4A = -C5A/4, spin-average shift, and the\n"
                "#        IsoVecSource sign fix, induced pseudoscalar on W and Z,\n"
                "#        Adler C6A on the N->Delta transition),\n"
                "#        MASSIVE muon.  PCAC verified on the vertices:\n"
                "#        see the header of build_cc1pi_csv.py.\n"
                "# sigma_model_wcut_*   : W < 1.4 GeV, from wprod_from_ufo.py\n"
                "# sigma_sherpa_uncut_* : Sherpa, NO W cut -- its Mass selector is\n"
                "#                        inert for this process (see the header of\n"
                "#                        build_cc1pi_csv.py).  2 seeds averaged.\n"
                "# data                 : ANL / BNL, W<1.4, Wilkinson et al. 2014\n"
                "#                        re-analysis, from anl_bnl_cc1pip.csv.\n"
                "#                        The data value is the flux-averaged one\n"
                "#                        over [data_E_lo, data_E_hi].\n"
                "# 1 ub = 1e-30 cm^2, so *_1e38cm2 = *_ub * 1e8.\n")
        f.write(",".join(cols) + "\n")
        for r in rows:
            f.write(",".join("" if r[c] is None else
                             ("%.6g" % r[c] if isinstance(r[c], float) else str(r[c]))
                             for c in cols) + "\n")
    print("wrote %s  (%d rows)" % (out, len(rows)))
    return rows, dat


def plot(rows, dat, stem='cc1pi_all_channels'):
    plt.rcParams.update({
        'font.family': 'serif', 'font.serif': ['STIXGeneral', 'DejaVu Serif'],
        'mathtext.fontset': 'stix', 'font.size': 9, 'axes.labelsize': 10,
        'xtick.labelsize': 8.5, 'ytick.labelsize': 8.5, 'legend.fontsize': 8,
        'axes.linewidth': 0.7, 'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.top': True, 'ytick.right': True,
        'xtick.minor.visible': True, 'ytick.minor.visible': True,
        'xtick.major.width': 0.7, 'ytick.major.width': 0.7,
        'xtick.minor.width': 0.5, 'ytick.minor.width': 0.5,
        'xtick.major.size': 3.4, 'ytick.major.size': 3.4,
        'xtick.minor.size': 1.9, 'ytick.minor.size': 1.9,
        'legend.frameon': False, 'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.02,
    })
    fig = plt.figure(figsize=(6.6, 5.8))
    gs = gridspec.GridSpec(2, 3, height_ratios=[2.5, 1], hspace=0.30,
                           wspace=0.16, figure=fig)
    ax = fig.add_subplot(gs[0, :])
    for ch in CH:
        pts = [(r['E_nu'], r['sigma_model_wcut_1e38cm2']) for r in rows
               if r['channel'] == ch and r['sigma_model_wcut_1e38cm2']]
        pts.sort()
        E = np.array([p[0] for p in pts]); m = np.array([p[1] for p in pts])
        ax.plot(E, m, color=COLOR[ch], lw=1.7, ls=DASH[ch], zorder=4)
        ax.annotate(TITLE[ch], xy=(E[-1], m[-1]), xytext=(4, 0),
                    textcoords='offset points', va='center', fontsize=9,
                    color=COLOR[ch])
        for exp in ('ANL', 'BNL'):
            d = [x for x in dat.get(ch, []) if x[5] == exp]
            if not d:
                continue
            a = np.array([(x[2], x[3] * UB, x[4] * UB, x[2] - x[0], x[1] - x[2])
                          for x in d])
            ax.errorbar(a[:, 0], a[:, 1], yerr=a[:, 2],
                        xerr=[a[:, 3], a[:, 4]], ls='none', marker=MARK[exp],
                        ms=3.6, mfc=COLOR[ch] if exp == 'ANL' else 'none',
                        mec=COLOR[ch], mew=0.9, ecolor=COLOR[ch],
                        elinewidth=0.7, capsize=0, zorder=5)
    ax.set_xlim(0.30, 2.05); ax.set_ylim(0.0, 0.80)
    ax.set_xlabel(r'$E_\nu$  (GeV)')
    ax.set_ylabel(r'$\sigma$  ($10^{-38}\,$cm$^2$)')
    ax.legend(handles=[
        Line2D([], [], color=INK, lw=1.5, label=r'model, $W<1.4$ GeV'),
        Line2D([], [], ls='none', marker='o', ms=3.6, mfc=INK, mec=INK,
               label='ANL (re-analysed)'),
        Line2D([], [], ls='none', marker='s', ms=3.6, mfc='none', mec=INK,
               mew=0.9, label='BNL (re-analysed)')],
        loc='upper left', bbox_to_anchor=(0.02, 0.92), handlelength=1.9)
    ax.text(0.02, 0.96, 'ChiPT_UFO_V8, massive $\\mu$; CVC + PCAC on nucleon and $\\Delta$',
            transform=ax.transAxes, va='top', fontsize=8, color=GREY)

    for col, ch in enumerate(CH):
        axr = fig.add_subplot(gs[1, col])
        for exp in ('ANL', 'BNL'):
            pr = [(r['E_nu'], r['ratio_data_over_model']) for r in rows
                  if r['channel'] == ch and r['ratio_data_over_model']
                  and r['data_experiment'] == exp]
            if not pr:
                continue
            pr.sort()
            axr.plot([p[0] for p in pr], [p[1] for p in pr], ls='none',
                     marker=MARK[exp], ms=3.4,
                     mfc=COLOR[ch] if exp == 'ANL' else 'none',
                     mec=COLOR[ch], mew=0.9)
        axr.axhline(1.0, color=COLOR[ch], lw=1.3, ls=DASH[ch])
        axr.set_ylim(0.0, 3.0); axr.set_yticks([0, 1, 2, 3])
        axr.set_xlim(0.30, 1.60); axr.set_xticks([0.5, 1.0, 1.5])
        axr.set_xlabel(r'$E_\nu$  (GeV)')
        if col == 0:
            axr.set_ylabel('data / model')
        else:
            axr.set_yticklabels([])
        axr.text(0.5, 1.04, TITLE[ch], transform=axr.transAxes, ha='center',
                 fontsize=8.5, color=COLOR[ch])
    for ext in ('pdf', 'png'):
        fig.savefig('%s.%s' % (stem, ext), dpi=600)
    print("wrote %s.pdf and %s.png" % (stem, stem))


if __name__ == '__main__':
    r, d = build()
    plot(r, d)
