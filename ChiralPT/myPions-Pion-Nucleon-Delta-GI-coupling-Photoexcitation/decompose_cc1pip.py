#!/usr/bin/env python3
"""
decompose_cc1pip.py -- sigma(nu_mu p -> mu- p pi+) split into Delta, Born and
their interference, the weak-sector counterpart of fig33_decomposition.

    sigma_total = sigma_Delta + sigma_Born + sigma_int
    sigma_int   = sigma_total - sigma_Delta - sigma_Born

which is exact, because |M_D + M_B|^2 = |M_D|^2 + |M_B|^2 + 2 Re(M_D M_B*).
The three pieces come from wprod_from_ufo.py with opt['delta'] / opt['born']
toggled; there is no separate interference run.

MODEL: ChiPT_UFO_All with the corrected Delta sector AND the CVC vector
N -> Delta transition.  The missing 1/(2J+1) is absorbed as an exact factor 2
in amplitude: h -> 2h and g -> g/2, so g*h -- the only combination the Fig. 33
fit constrains -- is preserved and photoproduction is untouched.  The propagator
width stays at the card's 102 MeV for the same reason.

*** V9-ERA NUMBERS.  TOTAL/DELTA/BORN below are frozen output of that
ChiPT_UFO_All run, and the h/g corrections described here belong to a model
whose hD, G1 and G2 were EXTERNAL.  From V10 the widths are the inputs and the
couplings are inverted from them, so the vertex reproduces both by construction
(tools/delta_widths.py, ratio 1.000000 on ChiPT_UFO_V13) and no such rescaling
applies.  These arrays are NOT V10+ numbers; rerunning the decomposition on a
current UFO means rerunning wprod_from_ufo.py at all six energies. ***
W < 1.4 GeV, matching the ANL/BNL cut sets.  Grid (20,12,12,8).

All three pieces are re-run: the CVC fix (F1V on the pion-in-flight and the
vector half of the contact term, F_rho on its axial half) changes the Born
sector too, and C4A = -C5A/4 changes the Delta.

CAVEAT ON THE DELTA PIECE.  The u-channel Delta is absent: the vertex-level
FpiNDelta(p_Delta^2) returns sqrt(X(u)) = 0 there and deletes it, where Fig. 33
would damp it by sqrt(X(s)).  Restoring it (the paper's prescription) adds
5-8% to the total -- so 'Delta only' here is really 's-channel Delta only'.
"""

import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# With the CVC vector N -> Delta transition, and g and h each on their own
# measured width (spin average included): h x 2.17, g / 1.84.
TOTAL = {0.400: 1.39277e-10, 0.625: 1.79306e-09, 0.875: 3.85484e-09,
         1.125: 4.92739e-09, 1.375: 5.40622e-09, 1.500: 5.53243e-09}
DELTA = {0.400: 1.37618e-10, 0.625: 1.47309e-09, 0.875: 2.98563e-09,
         1.125: 3.76182e-09, 1.375: 4.10756e-09, 1.500: 4.19821e-09}
BORN = {0.400: 1.87355e-11, 0.625: 1.18733e-10, 0.875: 2.49384e-10,
        1.125: 3.19552e-10, 1.375: 3.53874e-10, 1.500: 3.64251e-10}

UB = 1e-30 / 1e-38          # microbarn -> 1e-38 cm^2


def data_ratio(path='anl_bnl_cc1pip.csv'):
    out = {}
    for r in csv.DictReader(l for l in open(path) if not l.startswith('#')):
        if r['wcut'] == '1.4' and r['correction'] == 'wilkinson':
            out.setdefault(r['experiment'], []).append(
                (float(r['E_mid']), float(r['sigma_ub']), float(r['dsigma_ub'])))
    return out


def table():
    print("sigma(nu_mu p -> mu- p pi+), W < 1.4 GeV, in 1e-38 cm^2")
    print("model: full -- g*h fixed, CVC vector N->Delta, CVC on PF/CT, C4A=-C5A/4\n")
    print("%-7s %9s %9s %9s %9s   %6s %6s %6s"
          % ("E_nu", "total", "Delta", "Born", "interf",
             "%D", "%B", "%int"))
    for e in sorted(TOTAL):
        t, d, b = TOTAL[e] * UB, DELTA[e] * UB, BORN[e] * UB
        i = t - d - b
        print("%-7.3f %9.4f %9.4f %9.4f %9.4f   %5.0f%% %5.0f%% %5.0f%%"
              % (e, t, d, b, i, 100 * d / t, 100 * b / t, 100 * i / t))


def write_csv(out='cc1pip_decomposition.csv'):
    with open(out, 'w') as f:
        f.write("# sigma(nu_mu p -> mu- p pi+) decomposition, W < 1.4 GeV, ub\n"
                "# model ChiPT_UFO_All, h -> 2.17 h, Delta width 116.5 MeV\n"
                "# interference = total - delta - born (exact)\n")
        f.write("E_nu,sigma_total_ub,sigma_delta_ub,sigma_born_ub,"
                "sigma_interference_ub,frac_delta,frac_born,frac_interference\n")
        for e in sorted(TOTAL):
            t, d, b = TOTAL[e], DELTA[e], BORN[e]
            i = t - d - b
            f.write("%.3f,%.6g,%.6g,%.6g,%.6g,%.4f,%.4f,%.4f\n"
                    % (e, t, d, b, i, d / t, b / t, i / t))
    print("\nwrote %s" % out)


def make_plot(stem='cc1pip_decomposition'):
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
    # colourblind-safe categorical slots, separated by line style as well
    C_TOT, C_D, C_B, C_I, INK = '#111111', '#2a78d6', '#eb6834', '#59a14f', '#111111'
    E = np.array(sorted(TOTAL))
    t = np.array([TOTAL[e] for e in E]) * UB
    d = np.array([DELTA[e] for e in E]) * UB
    b = np.array([BORN[e] for e in E]) * UB
    i = t - d - b

    fig, (ax, axf) = plt.subplots(2, 1, figsize=(5.4, 5.6), sharex=True,
                                  gridspec_kw=dict(height_ratios=[2.4, 1],
                                                   hspace=0.07))
    ax.plot(E, t, color=C_TOT, lw=1.6, zorder=5, label='total')
    ax.plot(E, d, color=C_D, lw=1.4, ls='-', zorder=4, label=r'$\Delta$ only')
    ax.plot(E, b, color=C_B, lw=1.4, ls=(0, (4.5, 2.2)), zorder=4,
            label='Born only')
    ax.plot(E, i, color=C_I, lw=1.4, ls=(0, (1.4, 1.6)), zorder=4,
            label='interference')
    ax.axhline(0, color='0.75', lw=0.6, zorder=1)

    dat = data_ratio()
    for exp, st in (('ANL', dict(marker='o', mfc=INK, mec=INK, ms=3.2)),
                    ('BNL', dict(marker='s', mfc='none', mec=INK, ms=3.4, mew=0.8))):
        a = np.array(dat[exp])
        ax.errorbar(a[:, 0], a[:, 1] * UB, yerr=a[:, 2] * UB, ls='none',
                    ecolor=INK, elinewidth=0.6, capsize=0, zorder=6,
                    label='%s data' % exp, **st)

    ax.set_ylabel(r'$\sigma$  ($10^{-38}\,$cm$^2$)')
    ax.set_xscale('log'); ax.set_xlim(0.35, 1.62); ax.set_ylim(-0.05, 0.72)
    ax.legend(loc='upper left', ncol=2, handlelength=2.2, columnspacing=1.4)
    ax.text(0.97, 0.05, r'$\nu_\mu\,p\to\mu^-p\,\pi^+$,   $W<1.4$ GeV',
            transform=ax.transAxes, ha='right', fontsize=10)

    axf.plot(E, 100 * d / t, color=C_D, lw=1.4)
    axf.plot(E, 100 * b / t, color=C_B, lw=1.4, ls=(0, (4.5, 2.2)))
    axf.plot(E, 100 * i / t, color=C_I, lw=1.4, ls=(0, (1.4, 1.6)))
    axf.axhline(0, color='0.75', lw=0.6)
    axf.set_xlabel(r'$E_\nu$  (GeV)')
    axf.set_ylabel('fraction of total  (%)')
    axf.set_ylim(-20, 100)
    axf.set_xticks([0.4, 0.6, 0.8, 1.0, 1.5])
    axf.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    for ext in ('pdf', 'png'):
        fig.savefig('%s.%s' % (stem, ext), dpi=600)
    print("wrote %s.pdf and %s.png" % (stem, stem))


if __name__ == '__main__':
    table()
    write_csv()
    make_plot()
