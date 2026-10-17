#!/usr/bin/env python3
"""
plot_cc1pip.py -- sigma(nu_mu p -> mu- p pi+) against the ANL and BNL
bubble-chamber data, before and after the Delta-coupling correction.

W < 1.4 GeV ON BOTH SIDES.  The data sets used are the ones with the hadronic
invariant mass cut that isolates the Delta, and the model is integrated with the
same cut (wprod_from_ufo.py --wmax 1.4).  Comparing an uncut model curve to cut
data flatters the model badly -- the model has strength above the Delta that the
data excludes -- so the cut is not optional.

*** LEGACY -- V9-ERA SCRIPT, SUPERSEDED BY plot_w_vs_data.py. ***

Everything below describes a hand-applied correction to a model where hD, G1
and G2 were EXTERNAL numbers, and both hard-coded arrays (BEFORE/AFTER) are
frozen output of a wprod_from_ufo.py run on ChiPT_UFO_All.  V10 inverted that
parametrisation -- the widths became the inputs and the couplings are derived
from them -- and V13 moved both widths to the pole, so from V10 on there is no
correction left to apply: tools/delta_widths.py returns ratio 1.000000 for both
widths on ChiPT_UFO_V13.  The numbers in this file are NOT V13 numbers and
regenerating them would mean rerunning the scan at all 14 energies.

For the current comparison use plot_w_vs_data.py, which reads the W < 1.4 GeV
Sherpa scan (w_scan_results.csv) and puts the cut on both sides; the V13 result
it writes is cc1pi_sherpa_vs_data_V13.csv.  This script is kept only so the
V9-era figure can still be redrawn.

THE CORRECTION (V9-era, historical).  h -> 2.17 h and the Delta propagator
width -> 116.5 MeV, the value that same vertex then implies.  Both followed
from delta_couplings.py run on ChiPT_UFO_All:

  * Gamma(Delta -> N pi) from that model's vertex is 24.75 MeV against the
    Breit-Wigner 117, so h is short by sqrt(117/24.75) = 2.17 in amplitude;
  * Gamma(Delta -> N gamma) is 2.23 MeV against the PDG 0.66, so g is LARGE
    by 1.84;
  * the product g*h is off by only 0.84, which is why the Fig. 33
    photoproduction fit -- which constrains g*h alone -- never saw either.

The weak sector carries h TWICE (the gauged W-N-Delta transition and the
Delta -> N pi decay) and g not at all, so nothing compensates there.  g1/g2 do
not enter this observable; they would have to be rescaled by the same 2.17 to
hold photoproduction fixed, which is a separate exercise.

Run:  python3 plot_cc1pip.py
"""

import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# sigma in microbarn, W < 1.4 GeV, from wprod_from_ufo.py on ChiPT_UFO_All,
# Gauss-Legendre grid (20,12,12,8)
BEFORE = {0.400: 2.40376e-11, 0.625: 2.34788e-10, 0.650: 2.69422e-10,
          0.875: 5.67541e-10, 0.900: 5.97017e-10, 1.100: 8.11272e-10,
          1.125: 8.36208e-10, 1.300: 1.00645e-09, 1.375: 1.07896e-09,
          1.500: 1.20147e-09, 1.700: 1.40505e-09, 1.950: 1.67564e-09,
          2.000: 1.73194e-09, 3.000: 2.97942e-09}
AFTER = {0.400: 9.65364e-11, 0.625: 1.11807e-09, 0.650: 1.26466e-09,
         0.875: 2.37415e-09, 0.900: 2.46918e-09, 1.100: 3.07381e-09,
         1.125: 3.13445e-09, 1.300: 3.50154e-09, 1.375: 3.63716e-09,
         1.500: 3.84581e-09, 1.700: 4.15325e-09, 1.950: 4.51776e-09,
         2.000: 4.58964e-09, 3.000: 6.03796e-09}


def read_data(path='anl_bnl_cc1pip.csv'):
    rows = [r for r in csv.DictReader(l for l in open(path) if not l.startswith('#'))]
    out = {}
    for r in rows:
        if r['wcut'] != '1.4':
            continue
        key = (r['experiment'], r['correction'])
        out.setdefault(key, []).append(
            (float(r['E_lo']), float(r['E_hi']), float(r['E_mid']),
             float(r['sigma_ub']), float(r['dsigma_ub'])))
    for v in out.values():
        v.sort()
    return out


def table(data):
    print("sigma(nu_mu p -> mu- p pi+), W < 1.4 GeV on both sides, in ub\n")
    print("%-6s %-4s %11s %11s %11s %8s %8s"
          % ("E_nu", "exp", "data", "model before", "model after",
             "d/m bef", "d/m aft"))
    for exp, corr in (('ANL', 'wilkinson'), ('BNL', 'wilkinson')):
        for elo, ehi, em, xs, dxs in data[(exp, corr)]:
            if em not in AFTER:
                continue
            b, a = BEFORE[em], AFTER[em]
            print("%-6.3f %-4s %11.4g %11.4g %11.4g %8.2f %8.2f"
                  % (em, exp, xs, b, a, xs / b, xs / a))


def make_plot(data, stem='cc1pip_vs_data'):
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
    C_AFT, C_BEF, INK = '#2a78d6', '#eb6834', '#111111'
    fig, (ax, axr) = plt.subplots(2, 1, figsize=(5.4, 5.4), sharex=True,
                                  gridspec_kw=dict(height_ratios=[2.6, 1],
                                                   hspace=0.07))
    E = sorted(AFTER)
    ax.plot(E, [1e38 * 1e-30 * AFTER[e] for e in E], color=C_AFT, lw=1.5,
            zorder=4, label=r'model, $h\to2.17\,h$')
    ax.plot(E, [1e38 * 1e-30 * BEFORE[e] for e in E], color=C_BEF, lw=1.3,
            ls=(0, (4.5, 2.2)), zorder=3, label='model, as published')

    style = {('ANL', 'wilkinson'): dict(marker='o', mfc=INK, mec=INK, ms=3.2),
             ('BNL', 'wilkinson'): dict(marker='s', mfc='none', mec=INK, ms=3.4,
                                        mew=0.8)}
    for key, st in style.items():
        d = np.array([(r[2], r[3], r[4], r[2] - r[0], r[1] - r[2])
                      for r in data[key]])
        ax.errorbar(d[:, 0], 1e8 * d[:, 1], yerr=1e8 * d[:, 2],
                    xerr=[d[:, 3], d[:, 4]], ls='none', ecolor=INK,
                    elinewidth=0.6, capsize=0, zorder=5,
                    label='%s (Wilkinson et al. re-analysis)' % key[0], **st)

    ax.set_ylabel(r'$\sigma$  ($10^{-38}\,$cm$^2$)')
    ax.set_xscale('log'); ax.set_xlim(0.35, 3.4); ax.set_ylim(0, 0.85)
    ax.legend(loc='upper left', handlelength=2.2)
    ax.text(0.97, 0.06, r'$\nu_\mu\,p\to\mu^-p\,\pi^+$,   $W<1.4$ GeV',
            transform=ax.transAxes, ha='right', fontsize=10)

    for key, st in style.items():
        d = np.array([(r[2], r[3], r[4]) for r in data[key] if r[2] in AFTER])
        m = np.array([AFTER[e] for e in d[:, 0]]) * 1e-30 * 1e38
        axr.errorbar(d[:, 0], 1e8 * d[:, 1] / m, yerr=1e8 * d[:, 2] / m,
                     ls='none', ecolor=INK, elinewidth=0.6, capsize=0, **st)
    axr.axhline(1.0, color=C_AFT, lw=1.2)
    axr.set_xlabel(r'$E_\nu$  (GeV)')
    axr.set_ylabel('data / model')
    axr.set_ylim(0, 3.0)
    axr.set_xticks([0.4, 0.6, 0.8, 1.0, 1.5, 2.0, 3.0])
    axr.get_xaxis().set_major_formatter(matplotlib.ticker.ScalarFormatter())

    for ext in ('pdf', 'png'):
        fig.savefig('%s.%s' % (stem, ext), dpi=600)
    print("\nwrote %s.pdf and %s.png" % (stem, stem))


def write_csv(data, out='cc1pip_vs_data.csv'):
    with open(out, 'w') as f:
        f.write("# sigma(nu_mu p -> mu- p pi+), W < 1.4 GeV on both sides, ub\n"
                "# model: wprod_from_ufo.py on ChiPT_UFO_All, grid (20,12,12,8)\n"
                "# after = h -> 2.17 h and Delta propagator width -> 116.5 MeV\n")
        f.write("experiment,correction,E_lo,E_hi,E_mid,sigma_data_ub,"
                "dsigma_data_ub,model_before_ub,model_after_ub,"
                "ratio_before,ratio_after\n")
        for exp, corr in (('ANL', 'wilkinson'), ('BNL', 'wilkinson')):
            for elo, ehi, em, xs, dxs in data[(exp, corr)]:
                if em not in AFTER:
                    continue
                b, a = BEFORE[em], AFTER[em]
                f.write("%s,%s,%.3f,%.3f,%.3f,%.6g,%.4g,%.6g,%.6g,%.3f,%.3f\n"
                        % (exp, corr, elo, ehi, em, xs, dxs, b, a, xs / b, xs / a))
    print("wrote %s" % out)


if __name__ == '__main__':
    d = read_data()
    table(d)
    write_csv(d)
    make_plot(d)
