#!/usr/bin/env python3
"""
plot_all_channels_cc1pi.py -- all three charged-current single-pion channels on
one axis, with a data/model ratio panel per channel underneath.

    nu p -> mu- p pi+     pure I = 3/2
    nu n -> mu- p pi0     I = 3/2 + I = 1/2
    nu n -> mu- n pi+     I = 3/2 + I = 1/2

WHY THE THREE TOGETHER.  The Delta contributions are fixed relative to each
other by isospin alone -- amplitudes 1 : sqrt2/3 : 1/3, rates 9 : 2 : 1 -- and
the model reproduces 9 : 2.05 : 1 for the Delta-only pieces (the 2.5% is the
pi0/pi+ mass difference in the phase space).  So any channel-to-channel
disagreement with data cannot be the Delta; it has to be the I = 1/2 amplitude,
which only the lower two channels carry.

W < 1.4 GeV ON BOTH SIDES.  NOTE when setting this beside the Achilles DCC
figure, which is plotted WITHOUT a W cut out to 2.5 GeV: these are different
observables and the curves are not interchangeable.  A cut model curve against
uncut data (or vice versa) is meaningless -- the model has strength above the
Delta that the cut data excludes.

MODEL: ChiPT_UFO_All with the corrected Delta sector, h -> 2.17 h and the
propagator width -> 116.5 MeV (delta_couplings.py), grid (20,12,12,8).

COLOUR.  Channel by hue, matching the Achilles figure's assignment so the two
can be read side by side; experiment by marker (circle ANL, square BNL), also
its convention.  Curves additionally carry distinct dash patterns and are
direct-labelled, so channel identity never rests on colour alone.  Palette
validated with the dataviz six checks (port in /tmp/.../valpal.py, since node is
unusable here): CVD dE 8.6 >= 8.0 target, normal-vision floor 25.2, contrast
>= 3.0 on all three.  Light surface only -- this is a print figure.
"""

import csv
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D

UB = 1e8            # microbarn -> 1e-38 cm^2

# axial-only Delta transition (the model as it stands)
AXIAL = {
    'ppip': {0.400: 9.65364e-11, 0.625: 1.11807e-09, 0.875: 2.37415e-09,
             1.125: 3.13445e-09, 1.375: 3.63716e-09, 1.500: 3.84581e-09},
    'ppi0': {0.400: 4.02245e-11, 0.500: 1.57593e-10, 0.625: 4.08718e-10,
             0.750: 7.00832e-10, 0.875: 9.81715e-10, 1.000: 1.24769e-09,
             1.125: 1.50676e-09, 1.250: 1.76648e-09, 1.375: 2.03174e-09,
             1.500: 2.30516e-09},
    'npip': {0.400: 2.76339e-11, 0.500: 8.95946e-11, 0.625: 2.09211e-10,
             0.750: 3.48931e-10, 0.875: 4.90098e-10, 1.000: 6.30366e-10,
             1.125: 7.71445e-10, 1.250: 9.15093e-10, 1.375: 1.06236e-09,
             1.500: 1.21369e-09},
}
# The full model.  Five changes on top of the axial-only reference, none of them
# fitted to this data:
#   h -> 2h, g -> g/2      the missing 1/(2J+1) as an exact factor 2 in
#                          amplitude, with g*h -- the only combination the
#                          Fig. 33 fit constrains -- preserved, so
#                          photoproduction is untouched by construction
#   + CVC vector N->Delta  the weak vector transition the gauging never
#                          produced, built from the model's own photon vertex
#   C5A(0) = 1.2           h -> 2h already gives 1.241; this trims 3%
#   + CVC on PF and CT     Gonzalez-Jimenez et al. Eq. (18): once F1V is on the
#                          nucleon poles, CVC REQUIRES it on the pion-in-flight
#                          and the vector half of the contact term
#   C4A = -C5A/4           Adler's subleading axial N->Delta form factor
#                          (C3A = 0 the model already satisfies)
MODEL = {
    'ppip': {0.400: 1.39277e-10, 0.500: 6.77035e-10, 0.625: 1.79306e-09,
             0.750: 2.94841e-09, 0.875: 3.85484e-09, 1.000: 4.49460e-09,
             1.125: 4.92739e-09, 1.250: 5.21545e-09, 1.375: 5.40622e-09,
             1.500: 5.53243e-09},
    'ppi0': {0.400: 4.46802e-11, 0.500: 1.96368e-10, 0.625: 5.18374e-10,
             0.750: 8.60777e-10, 0.875: 1.13571e-09, 1.000: 1.33548e-09,
             1.125: 1.47585e-09, 1.250: 1.57398e-09, 1.375: 1.64314e-09,
             1.500: 1.69265e-09},
    'npip': {0.400: 3.16599e-11, 0.500: 1.11192e-10, 0.625: 2.64699e-10,
             0.750: 4.29187e-10, 0.875: 5.68143e-10, 1.000: 6.75138e-10,
             1.125: 7.54795e-10, 1.250: 8.13661e-10, 1.375: 8.57383e-10,
             1.500: 8.90223e-10},
}
CH = ['ppip', 'ppi0', 'npip']
COLOR = {'ppip': '#2a78d6', 'ppi0': '#117733', 'npip': '#e8710a'}
DASH = {'ppip': (0, ()), 'ppi0': (0, (5.0, 2.0)), 'npip': (0, (1.5, 1.7))}
TITLE = {'ppip': r'$\nu_\mu p\to\mu^-p\,\pi^+$',
         'ppi0': r'$\nu_\mu n\to\mu^-p\,\pi^0$',
         'npip': r'$\nu_\mu n\to\mu^-n\,\pi^+$'}
ISO = {'ppip': r'pure $I=3/2$', 'ppi0': r'$I=3/2+1/2$', 'npip': r'$I=3/2+1/2$'}
MARK = {'ANL': 'o', 'BNL': 's'}
INK, GREY = '#111111', '#8a8a8a'


def read(path='anl_bnl_cc1pip.csv'):
    out = {}
    for r in csv.DictReader(l for l in open(path) if not l.startswith('#')):
        if r['wcut'] != '1.4':
            continue
        out.setdefault((r['channel'], r['experiment'], r['correction']), []).append(
            (float(r['E_lo']), float(r['E_hi']), float(r['E_mid']),
             float(r['sigma_ub']) * UB, float(r['dsigma_ub']) * UB))
    for v in out.values():
        v.sort()
    return out


def main():
    data = read()
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
        E = np.array(sorted(MODEL[ch]))
        m = np.array([MODEL[ch][e] for e in E]) * UB
        ax.plot(E, m, color=COLOR[ch], lw=1.7, ls=DASH[ch], zorder=4)
        Ea = np.array(sorted(AXIAL[ch]))
        ma = np.array([AXIAL[ch][e] for e in Ea]) * UB
        ax.plot(Ea, ma, color=COLOR[ch], lw=1.0, ls=(0, (1, 2)), alpha=0.55,
                zorder=3)
        ax.annotate(TITLE[ch], xy=(E[-1], m[-1]), xytext=(4, 0),
                    textcoords='offset points', va='center', ha='left',
                    fontsize=9, color=COLOR[ch])
        for exp in ('ANL', 'BNL'):
            d = data.get((ch, exp, 'wilkinson'))
            if not d:
                continue
            a = np.array(d)
            ax.errorbar(a[:, 2], a[:, 3], yerr=a[:, 4],
                        xerr=[a[:, 2] - a[:, 0], a[:, 1] - a[:, 2]],
                        ls='none', marker=MARK[exp], ms=3.6,
                        mfc=COLOR[ch] if exp == 'ANL' else 'none',
                        mec=COLOR[ch], mew=0.9, ecolor=COLOR[ch],
                        elinewidth=0.7, capsize=0, zorder=5)

    ax.set_xlim(0.30, 2.10); ax.set_ylim(0, 0.72)
    ax.set_xlabel(r'$E_\nu$  (GeV)')
    ax.set_ylabel(r'$\sigma$  ($10^{-38}\,$cm$^2$)')
    handles = [Line2D([], [], color=INK, lw=1.5, label='full model'),
               Line2D([], [], color=INK, lw=1.0, ls=(0, (1, 2)), alpha=0.55,
                      label='axial $N\\!\\to\\!\\Delta$ only, no CVC fix'),
               Line2D([], [], ls='none', marker='o', ms=3.6, mfc=INK, mec=INK,
                      label='ANL (re-analysed)'),
               Line2D([], [], ls='none', marker='s', ms=3.6, mfc='none',
                      mec=INK, mew=0.9, label='BNL (re-analysed)')]
    ax.legend(handles=handles, loc='upper left', handlelength=1.9)
    ax.text(0.985, 0.04, r'$W<1.4$ GeV;  $g\,h$ fixed, CVC restored, $C_4^A=-C_5^A/4$',
            transform=ax.transAxes, ha='right', fontsize=8.5, color=GREY)

    for col, ch in enumerate(CH):
        axr = fig.add_subplot(gs[1, col])
        E = np.array(sorted(MODEL[ch]))
        m = np.array([MODEL[ch][e] for e in E]) * UB
        for exp in ('ANL', 'BNL'):
            d = data.get((ch, exp, 'wilkinson'))
            if not d:
                continue
            a = np.array(d)
            keep = (a[:, 2] >= E[0]) & (a[:, 2] <= E[-1])
            mi = np.interp(a[keep, 2], E, m)
            axr.errorbar(a[keep, 2], a[keep, 3] / mi, yerr=a[keep, 4] / mi,
                         ls='none', marker=MARK[exp], ms=3.4,
                         mfc=COLOR[ch] if exp == 'ANL' else 'none',
                         mec=COLOR[ch], mew=0.9, ecolor=COLOR[ch],
                         elinewidth=0.7, capsize=0)
        axr.axhline(1.0, color=COLOR[ch], lw=1.3, ls=DASH[ch])
        axr.set_xlim(0.30, 1.60); axr.set_ylim(0, 2.6)
        axr.set_xticks([0.5, 1.0, 1.5])
        axr.set_xlabel(r'$E_\nu$  (GeV)')
        if col == 0:
            axr.set_ylabel('data / model')
        else:
            axr.set_yticklabels([])
        axr.text(0.5, 1.04, TITLE[ch], transform=axr.transAxes, ha='center',
                 fontsize=8.5, color=COLOR[ch])
        axr.text(0.96, 0.90, ISO[ch], transform=axr.transAxes, ha='right',
                 va='top', fontsize=7, color=GREY)

    for ext in ('pdf', 'png'):
        fig.savefig('cc1pi_all_channels.%s' % ext, dpi=600)
    print("wrote cc1pi_all_channels.pdf and .png")


if __name__ == '__main__':
    main()
