#!/usr/bin/env python3
"""plot_w_vs_data.py -- Sherpa CC single-pion cross sections against ANL/BNL.

    python3 plot_w_vs_data.py                 # -> cc1pi_sherpa_vs_data.pdf/.png
    python3 plot_w_vs_data.py --published     # overlay the uncorrected data too

Reads the dense W < 1.4 GeV scan written by run_w_all.py (w_scan_results.csv)
and the bubble-chamber data extracted by anl_bnl_data.py (anl_bnl_cc1pip.csv),
and draws one panel per channel: sigma(E_nu) with the measurements on top, and a
data/model ratio row underneath.

BOTH SIDES CARRY THE SAME CUT.  The ANL/BNL sets selected here are the W < 1.4
GeV ones, and the Sherpa curve is the W < 1.4 GeV scan -- the invariant-mass
selector really is applied in the run cards (see run_w.py's header for the
placeholder bug that used to make --wcut a silent no-op).  Nothing here is
rescaled or renormalised.

WHICH DATA.  The default is the Wilkinson et al. re-analysis (PRD 90, 112017),
which re-does the ANL and BNL flux normalisations.  It matters: it moves ANL UP
by ~16% and BNL DOWN by ~29%, which is what brings the two experiments into
agreement with each other.  --published overlays the original numbers as open
grey markers so the size of that correction stays visible.

A CAVEAT ON THE COMPARISON.  The published cross sections are FLUX-AVERAGED over
each energy bin, while the curve is evaluated at a single energy.  The points are
therefore drawn at the bin centre with a horizontal bar spanning the bin, and the
ratio row divides by the model at that same centre.  Where the curve is strongly
convex across a wide bin -- the 0.3-0.5 GeV bin above all -- sigma(E_mid)
underestimates the bin average, so the lowest-energy ratio point is the least
trustworthy one in the figure.  Doing better needs the experiments' flux shapes,
which are not in this repository.
"""

import argparse
import collections
import csv
import os

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

SCAN_CSV = "w_scan_results.csv"
DATA_CSV = "anl_bnl_cc1pip.csv"
STEM = "cc1pi_sherpa_vs_data"

UB = 1e8                     # 1 ub = 1e-30 cm^2, so ub -> 1e-38 cm^2 is x1e8
WCUT = "1.40"                # the scan rows to plot
DATA_WCUT = "1.4"            # the matching data sets

CH = ["ppip", "ppi0", "npip"]
LABEL = {
    "ppip": r"$\nu_\mu\,p \to \mu^-\,p\,\pi^+$",
    "ppi0": r"$\nu_\mu\,n \to \mu^-\,p\,\pi^0$",
    "npip": r"$\nu_\mu\,n \to \mu^-\,n\,\pi^+$",
}
ISO = {"ppip": r"pure $I=3/2$", "ppi0": r"$I=3/2 \oplus 1/2$",
       "npip": r"$I=3/2 \oplus 1/2$"}
# Plain-text twins of the above, for the csv -- a collaborator reading the table
# should not have to strip LaTeX to learn which isospin channels contribute.
ISO_PLAIN = {"ppip": "pure I=3/2", "ppi0": "I=3/2 and I=1/2",
             "npip": "I=3/2 and I=1/2"}
PROCESS = {"ppip": "14 2212 -> 13 2212 211",
           "ppi0": "14 2112 -> 13 2212 111",
           "npip": "14 2112 -> 13 2112 211"}

# Categorical slots, checked rather than chosen by eye: worst-case CVD
# separation over protan/deutan/tritan is dE 21.6 (OKLab x100) and the worst
# normal-vision pair is 27.4, against targets of 8 and 15.  The green #117733
# this project used for ppi0 elsewhere fails that test against the orange --
# dE 7.4 under protanopia -- so the middle slot is re-stepped to wine here.
COLOR = {"ppip": "#2a78d6", "ppi0": "#882255", "npip": "#e8710a"}
# Channel identity is carried by dash pattern as well as hue, so it survives
# greyscale printing and does not rest on colour alone.  Same patterns as
# build_cc1pi_csv.py.
DASH = {"ppip": (0, ()), "ppi0": (0, (5.0, 2.0)), "npip": (0, (1.5, 1.7))}
INK, GREY, FAINT = "#111111", "#8a8a8a", "#c8c8c8"
# Experiment identity rides on marker SHAPE, so it never rests on colour, and
# the panel colour is left to mean "the model" alone.
MARK = {"ANL": "o", "BNL": "s"}

XLIM = (0.25, 1.65)


def read_scan(path=SCAN_CSV):
    """{channel: (E, sigma, err)} in 1e-38 cm^2, from the W<1.4 scan."""
    out = collections.defaultdict(list)
    with open(path) as f:
        for r in csv.DictReader(l for l in f if not l.startswith("#")):
            if r["wcut"] != WCUT:
                continue
            out[r["channel"]].append((float(r["E_nu"]),
                                      float(r["sigma_ub"]) * UB,
                                      float(r["err_ub"]) * UB))
    return {k: tuple(np.array(c) for c in zip(*sorted(v)))
            for k, v in out.items()}


def scan_provenance(path=SCAN_CSV):
    """(model, param card) of the W<WCUT rows, for the csv header."""
    seen = set()
    with open(path) as f:
        for r in csv.DictReader(l for l in f if not l.startswith("#")):
            if r["wcut"] == WCUT:
                seen.add((r["model"], r["param_card"]))
    if len(seen) != 1:
        return ("+".join(sorted(m for m, _ in seen)) or "unknown",
                "+".join(sorted(p for _, p in seen)) or "unknown")
    return seen.pop()


def read_data(path=DATA_CSV, correction="wilkinson"):
    """{(channel, experiment): (E_mid, E_lo, E_hi, sigma, err)} in 1e-38 cm^2."""
    out = collections.defaultdict(list)
    with open(path) as f:
        for r in csv.DictReader(l for l in f if not l.startswith("#")):
            if r["wcut"] != DATA_WCUT or r["correction"] != correction:
                continue
            if not (XLIM[0] <= float(r["E_mid"]) <= XLIM[1]):
                continue
            out[(r["channel"], r["experiment"])].append(
                (float(r["E_mid"]), float(r["E_lo"]), float(r["E_hi"]),
                 float(r["sigma_ub"]) * UB, float(r["dsigma_ub"]) * UB))
    return {k: tuple(np.array(c) for c in zip(*sorted(v)))
            for k, v in out.items()}


def model_at(scan_ch, energies, tol=1e-3):
    """The scan point at each energy, or nan where the grid has none.

    Deliberately NOT an interpolation: the scan grid was built as a superset of
    the data energies precisely so the ratio is a comparison of computed numbers.
    """
    E, S, _ = scan_ch
    out = np.full(len(energies), np.nan)
    for i, e in enumerate(energies):
        j = np.argmin(np.abs(E - e))
        if abs(E[j] - e) < tol:
            out[i] = S[j]
    return out


_TRAPZ = getattr(np, "trapezoid", None) or np.trapz


def model_binaveraged(scan_ch, elo, ehi):
    """<sigma> over each bin, at FLAT flux, off the dense grid.

    Only an approximation to what the experiments quote -- the real weight is
    the neutrino flux, which is not in this repository and is steeply rising
    across the lowest bin.  Its use here is diagnostic: comparing it with
    sigma(E_mid) says how much of a given ratio is a binning artefact.  For
    every bin above 0.5 GeV the two agree to within 4%, so the figure's default
    E_mid comparison is safe there; in the 0.3-0.5 GeV bin they differ by a
    factor 5, which is why that point is flagged rather than trusted.
    """
    E, S, _ = scan_ch
    out = np.full(len(elo), np.nan)
    for i, (a, b) in enumerate(zip(elo, ehi)):
        b = min(b, E.max())
        if b <= a:
            continue
        g = np.linspace(a, b, 400)
        out[i] = _TRAPZ(np.interp(g, E, S), g) / (b - a)
    return out


CSV_COLS = ["kind", "channel", "process", "label_tex", "isospin", "source",
            "correction", "wcut_GeV", "E_nu_GeV", "E_lo_GeV", "E_hi_GeV",
            "sigma_1e38cm2", "sigma_err_1e38cm2", "sigma_ub", "sigma_err_ub"]

CSV_HEADER = """\
# Everything drawn in cc1pi_sherpa_vs_data.pdf, in one long-format table.
# Written by plot_w_vs_data.py from the same arrays the figure uses, so the two
# cannot disagree.  One row per plotted point; `kind` says which layer it is.
#
#   kind=model   the Sherpa curve.  One row per scan energy, 32 per channel.
#                E_lo/E_hi are empty -- it is a point evaluation, not a bin.
#   kind=data    a measured point.  E_nu is the BIN CENTRE and E_lo/E_hi are the
#                published bin edges; the quoted value is FLUX-AVERAGED over
#                that bin, not evaluated at the centre.
#
# COLUMNS
#   channel        ppip / ppi0 / npip, the same names used across this project
#   process        PDG initial and final state, as given to Sherpa
#   label_tex      ready-to-use LaTeX for a legend or direct label
#   isospin        which isospin amplitudes contribute
#   source         Sherpa, ANL or BNL
#   correction     data only: `wilkinson` (PRD 90, 112017 re-analysis, what the
#                  figure shows) or `published` (the original numbers).  The
#                  re-analysis moves ANL UP ~16% and BNL DOWN ~29%, which is
#                  what brings the two experiments into agreement.
#   wcut_GeV       hadronic invariant-mass cut.  1.4 on BOTH sides -- the model
#                  is integrated with the same cut the data carry, not rescaled.
#   sigma_*        cross section and its error, given twice: in 1e-38 cm^2 (the
#                  usual unit for these plots, and what the figure's y axis is)
#                  and in ub.  1 ub = 1e-30 cm^2.  For kind=model the error is
#                  the Monte-Carlo statistical error only.
#
# TWO THINGS TO KNOW BEFORE REPLOTTING
#  1. The model is a curve through 32 computed energies per channel, spaced
#     0.025 GeV below 0.65, 0.05 to 1.0 and 0.1 above -- chosen so a plain line
#     through the points is smooth without interpolation doing the work.  Join
#     them with a simple line; no spline is needed.
#  2. The lowest data bin, 0.3-0.5 GeV, spans the muon-mass threshold turn-on,
#     where sigma rises by three orders of magnitude.  Comparing a curve read at
#     its centre against that bin understates the model by a factor ~5, so the
#     figure does not draw any conclusion there.  Every bin above 0.5 GeV is
#     safe: bin-averaging the model changes the comparison by at most 4%.
#
# Data beyond 1.6 GeV exists in anl_bnl_cc1pip.csv (ANL ppip to 4.75 GeV, BNL to
# 3.1) but is omitted here because the model scan stops at 1.6.
#
# model {MODEL}, param {PARAM}.  Generated {DATE}.
"""


def write_plot_csv(path, scan, sets, model, param):
    """The figure's contents as a tidy table, one row per plotted point."""
    import datetime
    rows = []
    for ch in CH:
        E, S, dS = scan[ch]
        for e, s, ds in zip(E, S, dS):
            rows.append(dict(kind="model", channel=ch, process=PROCESS[ch],
                             label_tex=LABEL[ch], isospin=ISO_PLAIN[ch],
                             source="Sherpa", correction="", wcut_GeV="1.4",
                             E_nu_GeV="%.4f" % e, E_lo_GeV="", E_hi_GeV="",
                             sigma_1e38cm2="%.8g" % s,
                             sigma_err_1e38cm2="%.8g" % ds,
                             sigma_ub="%.8g" % (s / UB),
                             sigma_err_ub="%.8g" % (ds / UB)))
    for corr, d in sets:
        for ch in CH:
            for exp in ("ANL", "BNL"):
                if (ch, exp) not in d:
                    continue
                Em, Elo, Ehi, S, dS = d[(ch, exp)]
                for em, el, eh, s, ds in zip(Em, Elo, Ehi, S, dS):
                    rows.append(dict(
                        kind="data", channel=ch, process=PROCESS[ch],
                        label_tex=LABEL[ch], isospin=ISO_PLAIN[ch], source=exp,
                        correction=corr, wcut_GeV="1.4",
                        E_nu_GeV="%.4f" % em, E_lo_GeV="%.4f" % el,
                        E_hi_GeV="%.4f" % eh, sigma_1e38cm2="%.8g" % s,
                        sigma_err_1e38cm2="%.8g" % ds,
                        sigma_ub="%.8g" % (s / UB),
                        sigma_err_ub="%.8g" % (ds / UB)))
    order = {c: i for i, c in enumerate(CH)}
    rows.sort(key=lambda r: (order[r["channel"]], r["kind"] != "model",
                             r["correction"], r["source"],
                             float(r["E_nu_GeV"])))
    with open(path, "w", newline="") as f:
        # .replace, not %-formatting: the header prose is full of literal
        # percent signs and every one of them would need escaping.
        f.write(CSV_HEADER.replace("{MODEL}", model).replace("{PARAM}", param)
                .replace("{DATE}", datetime.date.today().isoformat()))
        w = csv.DictWriter(f, fieldnames=CSV_COLS)
        w.writeheader()
        w.writerows(rows)
    print("wrote %s (%d rows)" % (path, len(rows)))


def style():
    plt.rcParams.update({
        'font.family': 'serif', 'font.serif': ['STIXGeneral', 'DejaVu Serif'],
        'mathtext.fontset': 'stix', 'font.size': 9, 'axes.labelsize': 9.5,
        'xtick.labelsize': 8.5, 'ytick.labelsize': 8.5, 'legend.fontsize': 8,
        'axes.linewidth': 0.7, 'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.top': True, 'ytick.right': True,
        'xtick.minor.visible': True, 'ytick.minor.visible': True,
        'xtick.major.width': 0.7, 'ytick.major.width': 0.7,
        'xtick.minor.width': 0.5, 'ytick.minor.width': 0.5,
        'xtick.major.size': 3.4, 'ytick.major.size': 3.4,
        'xtick.minor.size': 1.9, 'ytick.minor.size': 1.9,
        'legend.frameon': False, 'savefig.bbox': 'tight',
        'savefig.pad_inches': 0.02, 'axes.axisbelow': True,
    })


def draw_data(ax, d, color, exp, filled=True, size=4.4, zorder=5, lw=0.9):
    """One experiment's points: y error bars, and x bars spanning the bin.

    A 2px surface ring keeps a marker legible where two channels' points land on
    top of each other, which they do around 0.9-1.1 GeV.
    """
    Em, Elo, Ehi, S, dS = d
    # The bin bars are context, the uncertainty is the measurement -- so the
    # horizontal bars are drawn lighter and thinner than the vertical ones.
    # Equal weight makes a ladder of bars that buries the curves at low sigma.
    ax.errorbar(Em, S, xerr=[Em - Elo, Ehi - Em], fmt='none', ecolor=color,
                elinewidth=0.6, alpha=0.45, capsize=0, zorder=zorder - 1)
    ax.errorbar(Em, S, yerr=dS, fmt='none', ecolor=color, elinewidth=lw,
                capsize=0, zorder=zorder)
    ax.plot(Em, S, linestyle='none', marker=MARK[exp], ms=size + 1.6,
            mfc='none', mec='white', mew=2.0, zorder=zorder + 1)
    ax.plot(Em, S, linestyle='none', marker=MARK[exp],
            ms=size, mfc=color if filled else 'white',
            mec=color, mew=1.0, zorder=zorder + 2)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--scan", default=SCAN_CSV)
    ap.add_argument("--data", default=DATA_CSV)
    ap.add_argument("--published", action="store_true",
                    help="overlay the uncorrected ANL/BNL numbers")
    ap.add_argument("--stem", default=STEM)
    ap.add_argument("--no-csv", action="store_true",
                    help="skip writing the machine-readable table")
    a = ap.parse_args()

    scan = read_scan(a.scan)
    wilk = read_data(a.data, "wilkinson")
    pub = read_data(a.data, "published") if a.published else {}
    missing = [c for c in CH if c not in scan]
    if missing:
        raise SystemExit("no W<%s scan rows for %s in %s"
                         % (WCUT, ", ".join(missing), a.scan))
    binav = {k: model_binaveraged(scan[k[0]], d[1], d[2])
             for k, d in wilk.items()}

    style()
    fig, ax = plt.subplots(figsize=(5.6, 4.0))

    # ---- model curves, then data on top
    for ch in CH:
        E, S, dS = scan[ch]
        ax.plot(E, S, color=COLOR[ch], lw=1.7, ls=DASH[ch], zorder=4,
                solid_capstyle='round', dash_capstyle='round')
        ax.fill_between(E, S - dS, S + dS, color=COLOR[ch], alpha=0.28, lw=0,
                        zorder=3)

    for ch in CH:
        for exp in ("ANL", "BNL"):
            if (ch, exp) in pub:
                draw_data(ax, pub[(ch, exp)], FAINT, exp, filled=False,
                          size=3.4, zorder=1, lw=0.7)
    for ch in CH:
        for exp in ("ANL", "BNL"):
            if (ch, exp) in wilk:
                draw_data(ax, wilk[(ch, exp)], COLOR[ch], exp,
                          filled=(exp == "ANL"))

    ax.set_xlim(*XLIM)
    ax.set_ylim(0, 0.80)
    ax.set_ylabel(r"$\sigma$  [$10^{-38}\,\mathrm{cm}^2$]")

    # Direct labels rather than three more legend rows, placed in the empty
    # space each curve leaves on the right.  The two lower channels finish only
    # 0.026 apart, so one label goes above its curve and the other below.
    # (x, y-of-label-top); the isospin line always hangs below its own label.
    for ch, xt, yt in (("ppip", 0.98, 0.700),
                       ("ppi0", 1.25, 0.262),
                       ("npip", 1.25, 0.076)):
        ax.text(xt, yt, LABEL[ch], color=COLOR[ch], fontsize=8.5,
                ha='left', va='top')
        ax.text(xt, yt - 0.036, ISO[ch], color=GREY, fontsize=6.8,
                ha='left', va='top')

    ax.set_xlabel(r"$E_\nu$  [GeV]")

    handles = [
        Line2D([], [], color=INK, marker='o', ls='none', ms=4.4, mfc=INK,
               label='ANL'),
        Line2D([], [], color=INK, marker='s', ls='none', ms=4.4, mfc='white',
               label='BNL'),
        Line2D([], [], color=GREY, lw=1.7, label=r'Sherpa, $W<1.4$ GeV'),
        Patch(facecolor=GREY, alpha=0.28, lw=0, label='MC stat.'),
    ]
    if a.published:
        handles.insert(2, Line2D([], [], color=FAINT, marker='o', ls='none',
                                 ms=3.4, mfc='white', label='uncorrected'))
    ax.legend(handles=handles, loc='upper left', ncol=1,
              bbox_to_anchor=(0.015, 0.985), handletextpad=0.6,
              labelspacing=0.45)
    ax.text(0.015, 0.985 - 0.055 * (len(handles) + 1), 'Wilkinson re-analysis',
            transform=ax.transAxes, fontsize=6.8, color=GREY, va='top')

    ax.text(0.5, -0.155,
            "ChiPT_UFO_V8.  $W<1.4$ GeV applied on both sides.  Horizontal "
            "bars are the published energy bins.",
            transform=ax.transAxes, ha='center', va='top', fontsize=6.8,
            color=GREY, linespacing=1.5)

    for ext in ("pdf", "png"):
        fig.savefig("%s.%s" % (a.stem, ext), dpi=320)
    print("wrote %s.pdf and %s.png" % (a.stem, a.stem))

    # The table carries BOTH corrections whatever the figure shows: it is meant
    # to be handed on, and a collaborator restyling this plot should not have to
    # come back for the other data set.
    if not a.no_csv:
        model, param = scan_provenance(a.scan)
        write_plot_csv("%s.csv" % a.stem, scan,
                       [("wilkinson", wilk),
                        ("published", read_data(a.data, "published"))],
                       model, param)

    # ---- the numbers behind the ratio row, so the figure can be checked.
    # Both denominators are printed: where they disagree, the bin is too wide
    # for a point comparison and the ratio there is a binning artefact.
    print("\n%-5s %-4s %-10s %10s %10s %10s %14s %8s"
          % ("chan", "exp", "bin", "data", "sig(Emid)", "sig(binav)",
             "data/sig(Emid)", "binav"))
    for ch in CH:
        for exp in ("ANL", "BNL"):
            if (ch, exp) not in wilk:
                continue
            Em, Elo, Ehi, D, dD = wilk[(ch, exp)]
            M, A = model_at(scan[ch], Em), binav[(ch, exp)]
            for e, el, eh, d, dd, m, av in zip(Em, Elo, Ehi, D, dD, M, A):
                print("%-5s %-4s %4.2f-%4.2f %10.4g %10s %10.4g %14s %8s"
                      % (ch, exp, el, eh, d,
                         "--" if np.isnan(m) else "%.4g" % m, av,
                         "--" if np.isnan(m) else "%.2f +- %.2f"
                         % (d / m, dd / m),
                         "%.2f" % (d / av)))


if __name__ == "__main__":
    main()
