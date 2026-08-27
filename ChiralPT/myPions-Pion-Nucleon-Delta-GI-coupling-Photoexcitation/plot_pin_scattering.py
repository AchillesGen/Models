#!/usr/bin/env python3
"""plot_pin_scattering.py -- pi N -> pi N elastic, model against data and unitarity.

    pin_scattering.pdf / .png / .csv

WHY THIS PLOT EXISTS.  Every other check on the Delta sector runs through either
a photon or a neutrino beam.  Pion-nucleon elastic scattering uses the SAME
strong pi-N-Delta and pi-N-N vertices and none of the electroweak machinery, so
it isolates the strong sector -- and unlike photoproduction it has a ceiling
that needs no fit: pi+ p is pure I = 3/2, the Delta is elastic there
(BR(N pi) = 1), and a single resonant J = 3/2 partial wave cannot exceed

    sigma_el <= 8 pi / k(W)^2 ,

about 190 mb at the Breit-Wigner mass.  The bound runs with W, so the model is
compared with 8 pi / k(W)^2 at each W rather than with its value at the pole;
comparing everything with the peak value makes the high-W tail look like a
violation when it is not.

THE pi- p PANEL.  pi- p elastic is (1/3) A_3 + (2/3) A_1 in amplitude, so the
pure-I = 3/2 piece the model has enters its cross section with weight 1/9.  That
curve is drawn from the model's own Delta-only pi+ p result, rotated by isospin,
and it is deliberately NOT a prediction of pi- p: the model contains no I = 1/2
resonance (no Roper, no D13), so the gap between it and the data IS the missing
I = 1/2 sector, shown rather than hidden.

DATA.  pin_data.py, from the PDG hadronic cross-section compilation.  Both the
elastic and the total sets are plotted: below about W = 1.35 GeV the Delta is
elastic and they coincide, and where they separate a tree-level elastic model
cannot follow the total any more.  The elastic compilation is sparse through the
resonance precisely because total = elastic there, which is why the total set
carries the peak.

Usage:  CHIPT_MODEL=ChiPT_UFO_V13 python3 plot_pin_scattering.py
"""
import csv
import os
import sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tools'))
from _vertex import load                                        # noqa: E402
import pin_scattering as pin                                    # noqa: E402
from fig33_from_ufo import kmom                                  # noqa: E402

MB = 0.389379
MODEL = os.environ.get('CHIPT_MODEL', 'ChiPT_UFO_V13')
DATA = 'pin_data.csv'
STEM = 'pin_scattering'
INK, GREY = '#111111', '#8a8a8a'
CPLUS, CMINUS, CLIM = '#2a78d6', '#cc3311', '#117733'


def read_data():
    out = {}
    with open(DATA) as f:
        for r in csv.DictReader(l for l in f if not l.startswith('#')):
            W = float(r['W_GeV'])
            if not (1.08 <= W <= 1.60):
                continue
            out.setdefault((r['reaction'], r['kind']), []).append(
                (W, float(r['sigma_mb']),
                 0.5 * (float(r['err_hi_mb']) + float(r['err_lo_mb']))))
    return {k: tuple(np.array(c) for c in zip(*sorted(v)))
            for k, v in out.items()}


def main():
    ns, ff, V = load()
    MN, MD, mpi = ns['MNucleon'], ns['MDelta'], ns['MPiP']
    Ws = np.linspace(1.09, 1.60, 60)
    full = dict(delta_s=True, nucleon_u=True, delta_u=True, contact=True)
    donly = dict(delta_s=True, nucleon_u=False, delta_u=False, contact=False)

    sig_full = np.array([pin.sigma(V, ns, ff, W, full) for W in Ws])
    sig_dlt = np.array([pin.sigma(V, ns, ff, W, donly) for W in Ws])
    lim = np.array([MB * 8 * np.pi / kmom(W ** 2, mpi, MN) ** 2 for W in Ws])
    dat = read_data()

    plt.rcParams.update({
        'font.family': 'serif', 'font.serif': ['STIXGeneral', 'DejaVu Serif'],
        'mathtext.fontset': 'stix', 'font.size': 9, 'axes.labelsize': 10,
        'xtick.labelsize': 8.5, 'ytick.labelsize': 8.5, 'legend.fontsize': 7.6,
        'axes.linewidth': 0.7, 'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.top': True, 'ytick.right': True,
        'xtick.minor.visible': True, 'ytick.minor.visible': True,
        'legend.frameon': False, 'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.02})
    fig = plt.figure(figsize=(7.2, 3.35))
    gs = gridspec.GridSpec(1, 3, wspace=0.30, figure=fig, top=0.80)

    # ---- pi+ p, the clean I = 3/2 channel -------------------------------
    ax = fig.add_subplot(gs[0, 0])
    for kind, mk, mfc in (('total', 'o', INK), ('elastic', 's', 'none')):
        d = dat.get(('pi+p', kind))
        if d is None:
            continue
        W, s, e = d
        ax.errorbar(W, s, yerr=e, ls='none', marker=mk, ms=2.4, mfc=mfc,
                    mec=INK, mew=0.7, ecolor=INK, elinewidth=0.5, capsize=0,
                    alpha=0.75, zorder=2)
    ax.plot(Ws, lim, color=CLIM, lw=1.2, ls=(0, (1.4, 1.4)), zorder=3)
    ax.plot(Ws, sig_dlt, color=CPLUS, lw=1.3, ls=(0, (5.0, 2.0)), zorder=4)
    ax.plot(Ws, sig_full, color=CPLUS, lw=1.7, zorder=5)
    ax.axvline(MD, color=GREY, lw=0.7, ls=':')
    ax.set_xlim(1.08, 1.60); ax.set_ylim(0, 330)
    ax.set_xlabel(r'$W$  (GeV)'); ax.set_ylabel(r'$\sigma$  (mb)')
    ax.set_title(r'$\pi^+p\to\pi^+p$   (pure $I=3/2$)', fontsize=9)
    ax.text(1.45, 250, r'$8\pi/k^2$', fontsize=8, color=CLIM)

    # ---- saturation of the bound ----------------------------------------
    ax2 = fig.add_subplot(gs[0, 1])
    ax2.plot(Ws, sig_full / lim, color=CPLUS, lw=1.7)
    ax2.plot(Ws, sig_dlt / lim, color=CPLUS, lw=1.3, ls=(0, (5.0, 2.0)))
    for kind, mk, mfc in (('total', 'o', INK), ('elastic', 's', 'none')):
        d = dat.get(('pi+p', kind))
        if d is None:
            continue
        W, s, e = d
        li = np.array([MB * 8 * np.pi / kmom(w ** 2, mpi, MN) ** 2 for w in W])
        ax2.plot(W, s / li, ls='none', marker=mk, ms=2.4, mfc=mfc, mec=INK,
                 mew=0.7, alpha=0.75)
    ax2.axhline(1.0, color=CLIM, lw=1.2, ls=(0, (1.4, 1.4)))
    ax2.axvline(MD, color=GREY, lw=0.7, ls=':')
    ax2.set_xlim(1.08, 1.60); ax2.set_ylim(0, 1.75)
    ax2.set_xlabel(r'$W$  (GeV)')
    ax2.set_ylabel(r'$\sigma\,/\,(8\pi/k^2)$')
    ax2.set_title('saturation of the unitarity bound', fontsize=9)

    # ---- pi- p, where the missing I = 1/2 shows ---------------------------
    ax3 = fig.add_subplot(gs[0, 2])
    for kind, mk, mfc in (('total', 'o', INK), ('elastic', 's', 'none')):
        d = dat.get(('pi-p', kind))
        if d is None:
            continue
        W, s, e = d
        ax3.errorbar(W, s, yerr=e, ls='none', marker=mk, ms=2.4, mfc=mfc,
                     mec=INK, mew=0.7, ecolor=INK, elinewidth=0.5, capsize=0,
                     alpha=0.75, zorder=2)
    ax3.plot(Ws, sig_dlt / 9.0, color=CMINUS, lw=1.7, zorder=4)
    ax3.axvline(MD, color=GREY, lw=0.7, ls=':')
    ax3.set_xlim(1.08, 1.60); ax3.set_ylim(0, 90)
    ax3.set_xlabel(r'$W$  (GeV)'); ax3.set_ylabel(r'$\sigma$  (mb)')
    ax3.set_title(r'$\pi^-p$   ($I=3/2$ piece only)', fontsize=9)

    from matplotlib.lines import Line2D
    h = [Line2D([], [], color=CPLUS, lw=1.7, label=r'model, full'),
         Line2D([], [], color=CPLUS, lw=1.3, ls=(0, (5.0, 2.0)),
                label=r'model, $\Delta$ only'),
         Line2D([], [], color=CMINUS, lw=1.7,
                label=r'model $\Delta$, isospin-rotated ($\times 1/9$)'),
         Line2D([], [], color=CLIM, lw=1.2, ls=(0, (1.4, 1.4)),
                label=r'unitarity $8\pi/k(W)^2$'),
         Line2D([], [], ls='none', marker='o', ms=2.8, mfc=INK, mec=INK,
                label='PDG total'),
         Line2D([], [], ls='none', marker='s', ms=2.8, mfc='none', mec=INK,
                label='PDG elastic')]
    fig.legend(handles=h, loc='upper center', ncol=3,
               bbox_to_anchor=(0.5, 1.02), handlelength=2.4,
               columnspacing=1.4, labelspacing=0.3)

    fig.savefig(STEM + '.pdf'); fig.savefig(STEM + '.png', dpi=200)
    print('wrote %s.pdf and %s.png' % (STEM, STEM))

    with open(STEM + '.csv', 'w', newline='') as f:
        f.write('# pi N elastic scattering: model against the unitarity bound.\n')
        f.write('# model %s, sigma in mb, W in GeV.\n' % MODEL)
        f.write('# sigma_pip_full/_delta are pi+ p; sigma_pim_I32 is the same\n')
        f.write('# Delta piece rotated to pi- p by isospin (factor 1/9).\n')
        w = csv.writer(f)
        w.writerow(['W_GeV', 'sigma_pip_full_mb', 'sigma_pip_delta_mb',
                    'unitarity_mb', 'ratio_full', 'sigma_pim_I32_mb'])
        for i, W in enumerate(Ws):
            w.writerow(['%.4f' % W, '%.4f' % sig_full[i], '%.4f' % sig_dlt[i],
                        '%.4f' % lim[i], '%.4f' % (sig_full[i] / lim[i]),
                        '%.4f' % (sig_dlt[i] / 9.0)])
    print('wrote %s.csv' % STEM)

    ipk = int(np.argmax(sig_full))
    print('\nmodel peak  %.1f mb at W = %.4f   (bound there %.1f, ratio %.3f)'
          % (sig_full[ipk], Ws[ipk], lim[ipk], sig_full[ipk] / lim[ipk]))
    print('max saturation %.3f at W = %.4f'
          % (max(sig_full / lim), Ws[int(np.argmax(sig_full / lim))]))


if __name__ == '__main__':
    main()
