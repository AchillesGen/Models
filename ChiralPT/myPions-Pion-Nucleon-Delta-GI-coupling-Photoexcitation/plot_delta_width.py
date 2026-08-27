#!/usr/bin/env python3
"""plot_delta_width.py -- what a running Delta width would do, for the paper.

    cc1pi_width.pdf / .png / .csv

THE POINT, AND WHY IT IS A FUTURE-WORK FIGURE.  Comix takes the Delta width from
the DECAY block of the param card and uses that ONE number in every propagator,
s- and u-channel alike.  Nothing in the UFO interface can express a width that
depends on the propagator's own invariant mass, so an energy-dependent width is
not something this model can be given -- it is something Sherpa would have to
learn to do.  This figure is the estimate of what that costs, computed with the
independent analytic engine, so the paper can say how big the missing effect is
rather than only that it is missing.

THREE PRESCRIPTIONS, all normalised so Gamma(M_Delta) = Gamma_0 exactly, so the
figure is about SHAPE and nothing here rescales the resonance:

  HNV   Hernandez, Nieves and Valverde [PRD 76 (2007) 033005, Eq. (45)],
            Gamma(s) = Gamma_0 (M_Delta/sqrt(s)) (k/k_0)^3 Theta(sqrt(s)-M-mpi)
        Their own absolute normalisation comes from f* = 2.14 and gives 113 MeV
        at the pole; that 4% against this model's 117.66 MeV is deliberately NOT
        folded in.  The bare k^3 runs away above the resonance -- 563 MeV by
        W = 1.4, twenty times Gamma_0 by W = 1.8 -- which is the honest reason
        not to adopt it unmodified.
  BW    the same expression with the l = 1 Blatt-Weisskopf barrier factor put
        back, F^2(q)/F^2(q0) = (1+(q0 R)^2)/(1+(q R)^2), R = 1 fm.  It turns the
        large-q behaviour from q^3 into q and caps the width near 3x Gamma_0.
        HNV is its R -> 0 limit, and R over 0.5-1.5 fm is worth about 7% on
        sigma, so the two are ends of one soft parameter, not rival choices.
  X_pi  Fig. 33's prescription, Gamma = Gamma_0 X_pi with X = 2r^3/(1+r^5).  It
        is NOT a k^3 law: X_pi rises like r^3 near threshold and then TURNS
        OVER, so the width stays between about 70 and 120 MeV over the whole
        W < 1.4 region.  That is why it barely moves the cross section, and why
        the three prescriptions bracket the fixed-width answer so widely rather
        than agreeing with each other.

THE THETA FUNCTION IS NOT A DETAIL, and it is the part of this that is a defect
rather than a preference.  Below the pi N threshold the running width is zero,
and the crossed (u-channel) Delta is ALWAYS below it -- u < 0 for physical
kinematics.  The fixed-width run hands that propagator a 118 MeV imaginary part
it has no business having.  No choice of Gamma_0 fixes that; only a width that
knows its own argument does.

WHERE EACH CURVE COMES FROM.  The solid curves are the Sherpa scan, which is
what the rest of the paper uses.  The correction factor

    R(E) = sigma[running width] / sigma[fixed width]

comes from width_study.py via width_study_V12.csv -- the analytic engine, nine
energies per channel, the SAME integration grid for both widths so the
quadrature error cancels in the ratio -- and is interpolated onto the Sherpa
grid.  The dashed curves are the Sherpa cross section times R(E).  Doing it as a
ratio rather than plotting the analytic engine directly keeps the absolute
normalisation identical to every other figure in the paper.

THE TWO ENGINES AGREE ONLY IF THE WIDTH IS FORCED.  wprod_from_ufo.py reads
Gamma_Delta from the UFO's WDeltaP external, which is stale at 0.102, while the
card and hence Comix carry GamNPi + GamNGam = 0.11766.  Unforced, the analytic
engine sits 17% high and it looks like a grid error; forced, the two agree to
better than 1% (0.803 vs 0.810 for ppip at E_nu = 1 GeV, W < 1.4).
width_study.py forces it.

Usage:  python3 plot_delta_width.py
"""
import csv
import os

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D

UB = 1e8                       # microbarn -> 1e-38 cm^2
SCAN = 'w_scan_results.csv'
DATA = 'anl_bnl_cc1pip.csv'
STEM = 'cc1pi_width'
MODEL = 'ChiPT_UFO_V12'
PARAM = 'param_ChiPT_UFO_V12.dat'
EDW_CSV = 'width_study_V12.csv'
WCUT = '1.40'

CH = ['ppip', 'ppi0', 'npip']
TITLE = {'ppip': r'$\nu_\mu p\to\mu^-p\,\pi^+$',
         'ppi0': r'$\nu_\mu n\to\mu^-p\,\pi^0$',
         'npip': r'$\nu_\mu n\to\mu^-n\,\pi^+$'}
COL = {'ppip': '#2a78d6', 'ppi0': '#cc3311', 'npip': '#117733'}
MARK = {'ANL': 'o', 'BNL': 's'}
INK, GREY = '#111111', '#8a8a8a'
XLIM = (0.25, 1.75)

# The Delta as the model's OWN (default) card carries it.  GAM0 is
# GamNPi + GamNGam, the value make_param_cards.py writes into the DECAY block
# and the value Comix therefore runs -- NOT the UFO's stale WDeltaP external of
# 0.102, which is what wprod_from_ufo.py picks up if it is not overridden.
MD, GAM0, MN, MPI0 = 1.209, 0.11766, 0.938272, 0.1349768


def kmom(s, m1, m2):
    a = (s - (m1 + m2) ** 2) * (s - (m1 - m2) ** 2)
    return np.sqrt(np.maximum(a, 0.0)) / (2 * np.sqrt(s))


def gamma_run(W):
    """Eq. (45) as a ratio to Gamma_0, so Gamma(M_Delta) = Gamma_0 exactly."""
    W = np.atleast_1d(np.asarray(W, dtype=float))
    k0 = kmom(MD ** 2, MPI0, MN)
    out = np.zeros_like(W)
    ok = W > MN + MPI0
    r = kmom(W[ok] ** 2, MPI0, MN) / k0
    out[ok] = GAM0 * (MD / W[ok]) * r ** 3
    return out


def gamma_xpi(W):
    """Fig. 33's prescription, Gamma(W) = Gamma_0 X_pi(W), X = 2r^3/(1+r^5).

    It is NOT a k^3 law.  X_pi rises like r^3 near threshold and then TURNS
    OVER -- the r^5 in the denominator wins -- so the width stays between about
    90 and 120 MeV over the whole W < 1.4 region instead of growing without
    bound.  That is why it barely moves the cross section, and it is the reason
    the two running-width prescriptions bracket the fixed-width answer so
    widely rather than agreeing with each other.
    """
    W = np.atleast_1d(np.asarray(W, dtype=float))
    k0 = kmom(MD ** 2, MPI0, MN)
    out = np.zeros_like(W)
    ok = W > MN + MPI0
    r = kmom(W[ok] ** 2, MPI0, MN) / k0
    out[ok] = GAM0 * 2.0 * r ** 3 / (1.0 + r ** 5)
    return out


BWR = 5.06773                 # Blatt-Weisskopf radius in GeV^-1; = 1 fm


def gamma_bw(W, R=BWR):
    """HNV's k^3 with the l = 1 Blatt-Weisskopf barrier factor put back.

        Gamma = Gamma_0 (q/q0)^3 (m0/W) F^2(q)/F^2(q0),
        F^2(q)/F^2(q0) = (1 + (q0 R)^2)/(1 + (q R)^2)

    which is the SAME expression as Eq. (45) with F = 1.  The factor is
    normalised to 1 at the pole, so Gamma(M_Delta) = Gamma_0 for any R, and it
    turns the large-q behaviour from q^3 into q.
    """
    W = np.atleast_1d(np.asarray(W, dtype=float))
    k0 = kmom(MD ** 2, MPI0, MN)
    out = np.zeros_like(W)
    ok = W > MN + MPI0
    q = kmom(W[ok] ** 2, MPI0, MN)
    out[ok] = (GAM0 * (q / k0) ** 3 * (MD / W[ok])
               * (1.0 + (k0 * R) ** 2) / (1.0 + (q * R) ** 2))
    return out


def bw_ratio_g(W, gfun):
    d = W ** 2 - MD ** 2
    g = gfun(W)
    return (d ** 2 + (MD * GAM0) ** 2) / (d ** 2 + (MD * g) ** 2)


def bw_ratio(W):
    """|BW(running)|^2 / |BW(fixed)|^2 at hadronic mass W."""
    d = W ** 2 - MD ** 2
    g = gamma_run(W)
    return (d ** 2 + (MD * GAM0) ** 2) / (d ** 2 + (MD * g) ** 2)


def read_scan():
    out = {}
    with open(SCAN) as f:
        for r in csv.DictReader(l for l in f if not l.startswith('#')):
            if (r['wcut'] != WCUT or r['model'] != MODEL
                    or r['param_card'] != PARAM):
                continue
            out.setdefault(r['channel'], []).append(
                (float(r['E_nu']), float(r['sigma_ub']) * UB,
                 float(r['err_ub']) * UB))
    return {k: tuple(np.array(c) for c in zip(*sorted(v)))
            for k, v in out.items()}


def read_data():
    out = {}
    with open(DATA) as f:
        for r in csv.DictReader(l for l in f if not l.startswith('#')):
            if r['wcut'] != '1.4' or r['correction'] != 'wilkinson':
                continue
            if not (XLIM[0] <= float(r['E_mid']) <= XLIM[1]):
                continue
            out.setdefault((r['channel'], r['experiment']), []).append(
                (float(r['E_mid']), float(r['E_lo']), float(r['E_hi']),
                 float(r['sigma_ub']) * UB, float(r['dsigma_ub']) * UB))
    return {k: tuple(np.array(c) for c in zip(*sorted(v)))
            for k, v in out.items()}


def read_edw():
    """{(channel, prescription): (E, R)} from width_study_V12.csv.

    R(E) = sigma[running] / sigma[fixed] at the same energy, the same channel,
    the same W < 1.4 cut and the SAME integration grid, so the quadrature error
    cancels in the ratio.  width_study.py writes that file; it forces
    Gamma_0 = GamNPi + GamNGam so the analytic engine and Sherpa are comparing
    the same resonance.
    """
    tag = {'x': 'xpi', 'hnv': 'hnv', 'bw': 'bw'}
    sig = {}
    with open(EDW_CSV) as f:
        for r in csv.DictReader(l for l in f if not l.startswith('#')):
            if r['wmax'] != '1.4' or float(r['bwr_fm']) != 1.0:
                continue
            sig[(r['channel'], float(r['E_nu']), r['edw'])] = float(r['sigma'])
    out = {}
    for ch in CH:
        es = sorted({e for (c, e, w) in sig if c == ch and w == ''})
        for w, t in tag.items():
            pts = [(e, sig[(ch, e, w)] / sig[(ch, e, '')]) for e in es
                   if (ch, e, w) in sig]
            if pts:
                out[(ch, t)] = tuple(np.array(c) for c in zip(*pts))
    return out


def main():
    scan, dat, edw = read_scan(), read_data(), read_edw()
    if not edw:
        raise SystemExit("no fixed/running pairs found in %s" % EDW_CSV)
    for ch in CH:
        for w in ('hnv', 'bw', 'xpi'):
            n = len(edw.get((ch, w), ([],))[0])
            print("%-6s %-4s %d energies against the fixed width" % (ch, w, n))

    plt.rcParams.update({
        'font.family': 'serif', 'font.serif': ['STIXGeneral', 'DejaVu Serif'],
        'mathtext.fontset': 'stix', 'font.size': 9, 'axes.labelsize': 10,
        'xtick.labelsize': 8.5, 'ytick.labelsize': 8.5, 'legend.fontsize': 8,
        'axes.linewidth': 0.7, 'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.top': True, 'ytick.right': True,
        'xtick.minor.visible': True, 'ytick.minor.visible': True,
        'legend.frameon': False, 'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.02,
    })
    fig = plt.figure(figsize=(7.2, 5.4))
    gs = gridspec.GridSpec(2, 3, height_ratios=[1.3, 1.0], hspace=0.46,
                           wspace=0.30, figure=fig, top=0.87, bottom=0.08)

    rows = []
    for col, ch in enumerate(CH):
        ax = fig.add_subplot(gs[0, col])
        E, S, dS = scan[ch]
        ax.plot(E, S, color=COL[ch], lw=1.6, zorder=4)
        Ri = {}
        for w, dash in (('hnv', (0, (5.0, 2.0))),
                        ('bw', (0, (6.0, 1.6, 1.2, 1.6))),
                        ('xpi', (0, (1.4, 1.4)))):
            if (ch, w) not in edw:
                continue
            Ee, R = edw[(ch, w)]
            Ri[w] = np.interp(E, Ee, R)
            ax.plot(E, S * Ri[w], color=COL[ch], lw=1.5, ls=dash, zorder=4)
        for exp in ('ANL', 'BNL'):
            d = dat.get((ch, exp))
            if not d:
                continue
            Em, Elo, Ehi, sg, dsg = d
            ax.errorbar(Em, sg, yerr=dsg, xerr=[Em - Elo, Ehi - Em],
                        ls='none', marker=MARK[exp], ms=3.4,
                        mfc=INK if exp == 'ANL' else 'none', mec=INK, mew=0.9,
                        ecolor=INK, elinewidth=0.7, capsize=0, zorder=5)
        ax.set_xlim(*XLIM)
        ax.set_ylim(bottom=0.0)
        ax.set_title(TITLE[ch], fontsize=9.5, pad=4)
        ax.set_xlabel(r'$E_\nu$  (GeV)')
        if col == 0:
            ax.set_ylabel(r'$\sigma$  ($10^{-38}\,$cm$^2$)')
        for w in Ri:
            for e, s, r in zip(E, S, Ri[w]):
                rows.append(dict(series='sigma_' + w, channel=ch, x=e,
                                 y_fixed=s, y_running=s * r, ratio=r))

    # ---- the mechanism: the width itself -----------------------------------
    axg = fig.add_subplot(gs[1, 0])
    Wg = np.linspace(1.08, 1.42, 400)
    g = gamma_run(Wg)
    gx, gb = gamma_xpi(Wg), gamma_bw(Wg)
    axg.axhline(1000 * GAM0, color=INK, lw=1.5)
    axg.plot(Wg, 1000 * g, color=INK, lw=1.5, ls=(0, (5.0, 2.0)))
    axg.plot(Wg, 1000 * gb, color=INK, lw=1.5,
             ls=(0, (6.0, 1.6, 1.2, 1.6)))
    axg.plot(Wg, 1000 * gx, color=INK, lw=1.5, ls=(0, (1.4, 1.4)))
    axg.axvline(MD, color=GREY, lw=0.7, ls=':')
    axg.set_xlabel(r'$W$  (GeV)')
    axg.set_ylabel(r'$\Gamma_\Delta$  (MeV)')
    axg.axvline(1.4, color=GREY, lw=0.7, ls='--')
    axg.set_xlim(1.08, 1.42)
    axg.set_ylim(0, 620)
    axg.text(1.093, 1000 * GAM0 + 22, 'fixed', fontsize=7.5, color=INK)
    axg.text(1.328, 470, r'$k^3$', fontsize=9, color=INK)
    axg.text(1.352, 215, r'BW', fontsize=8.5, color=INK)
    axg.text(1.352, 40, r'$X_\pi$', fontsize=9, color=INK)
    axg.text(1.4, 632, r'$W<1.4$', fontsize=7, color=GREY,
             ha='center', va='bottom', clip_on=False)
    for w, gg, gbb, gxx in zip(Wg, g, gb, gx):
        for tag, v in (('hnv', gg), ('bw', gbb), ('xpi', gxx)):
            rows.append(dict(series='width_' + tag, channel='', x=w,
                             y_fixed=GAM0, y_running=v, ratio=v / GAM0))

    # ---- what it does to the propagator ------------------------------------
    axb = fig.add_subplot(gs[1, 1])
    br = bw_ratio_g(Wg, gamma_run)
    bb = bw_ratio_g(Wg, gamma_bw)
    bx = bw_ratio_g(Wg, gamma_xpi)
    axb.plot(Wg, br, color=INK, lw=1.5, ls=(0, (5.0, 2.0)))
    axb.plot(Wg, bb, color=INK, lw=1.5, ls=(0, (6.0, 1.6, 1.2, 1.6)))
    axb.plot(Wg, bx, color=INK, lw=1.5, ls=(0, (1.4, 1.4)))
    axb.axhline(1.0, color=GREY, lw=0.7, ls=':')
    axb.axvline(MD, color=GREY, lw=0.7, ls=':')
    axb.set_xlabel(r'$W$  (GeV)')
    axb.set_ylabel(r'$|{\rm BW}|^2$  running / fixed')
    axb.axvline(1.4, color=GREY, lw=0.7, ls='--')
    axb.set_xlim(1.08, 1.42)
    axb.set_ylim(0, 2.2)
    for w, v1, v2, v3 in zip(Wg, br, bb, bx):
        for tag, v in (('hnv', v1), ('bw', v2), ('xpi', v3)):
            rows.append(dict(series='bw_ratio_' + tag, channel='', x=w,
                             y_fixed=1.0, y_running=v, ratio=v))

    # ---- and to the integrated cross section --------------------------------
    axr = fig.add_subplot(gs[1, 2])
    for ch in CH:
        for w, dash, mk, mfc in (('hnv', (0, (5.0, 2.0)), 'o', None),
                                 ('bw', (0, (6.0, 1.6, 1.2, 1.6)), 's', None),
                                 ('xpi', (0, (1.4, 1.4)), 'o', 'none')):
            if (ch, w) not in edw:
                continue
            Ee, R = edw[(ch, w)]
            axr.plot(Ee, R, color=COL[ch], lw=1.4, ls=dash, marker=mk,
                     ms=3.2 if mk == 'o' else 2.8,
                     mfc=mfc if mfc else COL[ch], mec=COL[ch], mew=0.9)
            for e, r in zip(Ee, R):
                rows.append(dict(series='R_' + w, channel=ch, x=e, y_fixed=1.0,
                                 y_running=r, ratio=r))
    axr.axhline(1.0, color=GREY, lw=0.7, ls=':')
    axr.set_xlabel(r'$E_\nu$  (GeV)')
    axr.set_ylabel(r'$\sigma$  running / fixed')
    axr.set_xlim(*XLIM)
    axr.set_ylim(0.6, 1.68)

    handles = [Line2D([], [], color=INK, lw=1.6, label='fixed width (Comix)'),
               Line2D([], [], color=INK, lw=1.5, ls=(0, (5.0, 2.0)),
                      label=r'running, HNV Eq. (45): $\Gamma_0\,(M_\Delta/W)'
                            r'\,(k/k_0)^3$'),
               Line2D([], [], color=INK, lw=1.5,
                      ls=(0, (6.0, 1.6, 1.2, 1.6)),
                      label=r'running, $+$ Blatt--Weisskopf $\ell=1$, '
                            r'$R=1$ fm'),
               Line2D([], [], color=INK, lw=1.5, ls=(0, (1.4, 1.4)),
                      label=r'running, Fig. 33: $\Gamma_0\,X_\pi$'),
               Line2D([], [], ls='none', marker='o', ms=3.4, mfc=INK, mec=INK,
                      label='ANL (re-analysed)'),
               Line2D([], [], ls='none', marker='s', ms=3.4, mfc='none',
                      mec=INK, mew=0.9, label='BNL (re-analysed)')]
    fig.legend(handles=handles, loc='upper center', ncol=3,
               bbox_to_anchor=(0.5, 1.005), handlelength=2.6,
               columnspacing=1.4, labelspacing=0.35)

    fig.savefig(STEM + '.pdf')
    fig.savefig(STEM + '.png', dpi=200)
    print("wrote %s.pdf and %s.png" % (STEM, STEM))

    cols = ['series', 'channel', 'x', 'y_fixed', 'y_running', 'ratio']
    with open(STEM + '.csv', 'w') as f:
        f.write("# Effect of an energy-dependent Delta width on CC single-pion "
                "production.\n"
                "# model %s, card %s, W < 1.4 GeV.\n"
                "# series=sigma   x=E_nu/GeV, y in 1e-38 cm^2; y_fixed is the "
                "Sherpa scan, y_running is that times ratio.\n"
                "# series=width_*    x=W/GeV, y in GeV; y_fixed is Gamma_0, "
                "y_running the prescription named by the suffix.\n"
                "# series=bw_ratio_* x=W/GeV, "
                "|BW(running)|^2/|BW(fixed)|^2.\n"
                "# suffix hnv = HNV Eq.(45), Gamma_0 (M_Delta/W)(k/k_0)^3;\n"
                "# suffix bw  = the same times an l=1 Blatt-Weisskopf factor "
                "(1+(q0 R)^2)/(1+(q R)^2), R = 1 fm;\n"
                "# suffix xpi = Fig. 33, Gamma_0 X_pi with X_pi = "
                "2r^3/(1+r^5).\n"
                "# series=R_*     x=E_nu/GeV, sigma(running)/sigma(fixed) "
                "computed with wprod_from_ufo.py at these six energies; the\n"
                "#                sigma rows use it interpolated onto the "
                "Sherpa energy grid.\n" % (MODEL, PARAM))
        f.write(",".join(cols) + "\n")
        for r in rows:
            f.write(",".join("%s" % r[c] for c in cols) + "\n")
    print("wrote %s.csv (%d rows)" % (STEM, len(rows)))

    print("\n  sigma(running)/sigma(fixed), and the resulting sigma")
    print("  %-6s %6s %8s %8s %8s %9s %9s %9s"
          % ("chan", "E_nu", "k^3", "+BW", "X_pi", "s(k^3)", "s(+BW)",
             "s(X_pi)"))
    for ch in CH:
        E, S, _ = scan[ch]
        Eh, Rh = edw[(ch, 'hnv')]
        nan = np.full_like(Rh, np.nan)
        Rb = edw.get((ch, 'bw'), (Eh, nan))[1]
        Rx = edw.get((ch, 'xpi'), (Eh, nan))[1]
        for e, rh, rb, rx in zip(Eh, Rh, Rb, Rx):
            s0 = np.interp(e, E, S)
            print("  %-6s %6.2f %8.4f %8.4f %8.4f %9.4f %9.4f %9.4f"
                  % (ch, e, rh, rb, rx, s0 * rh, s0 * rb, s0 * rx))


if __name__ == '__main__':
    main()
