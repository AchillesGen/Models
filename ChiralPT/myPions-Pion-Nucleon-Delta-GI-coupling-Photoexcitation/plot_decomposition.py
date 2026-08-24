"""
plot_decomposition.py -- what each diagram class contributes to sigma(gamma N -> pi N).

The amplitude is a sum of three classes, M = B + D + V (Born, Delta(1232),
t-channel omega/rho), so the cross section is six terms: three squares and three
interferences.  fig33_decomposition.m computes them on scan.py's photon grid and
writes fig33_decomposition.csv; this script only draws it, and runs nothing.

    math -script fig33_decomposition.m     # build the csv (a few minutes)
    python3 plot_decomposition.py          # draw it

WHY LINES AND NOT A STACKED AREA.  The six terms are additive, which normally
argues for a stack -- but three of them go NEGATIVE (the Born-Delta interference
strongly so above the resonance, which is exactly what pulls the tail down).
Stacking mixed signs draws segments whose lengths no longer read as their values,
so the terms are drawn as lines against a zero rule and the black curve carries
their sum.

THE VECTOR SECTOR IS SPLIT BY MESON.  |V|^2 is drawn with its omega and rho
pieces underneath it, in the same hue at a lighter weight -- they are the inside
of that series, not two more categories.  They are what answers "why is the
vector contribution so small for charged pions": the t-channel vertex is
gamma -> pi + V, so the exchanged meson carries the pion's charge, and the
neutral isoscalar omega can only appear when the pion is neutral.  It then
dominates, F_omega = 21.11 against F_rho = 2.6, and is identically zero in the
charged channels.  `--no-split-vector` draws |V|^2 whole.

COLOUR.  The six categorical slots are the leading six of a documented,
pre-validated order (blue, orange, aqua, yellow, magenta, green), used unmodified
and in order rather than re-stepped, so its colourblind-safety gates carry over;
a line chart is judged on adjacent pairs, which that order clears.  Identity does
not rest on colour alone: the three squares are solid and the three interference
terms dashed, the legend is always drawn, and fig33_decomposition.csv is the
table view of the same numbers.

Run:  python3 plot_decomposition.py [-h] [--channels pi0p,...]
"""

import argparse
import collections
import os
import sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import scan as S

DECOMP_CSV = "fig33_decomposition.csv"
OUT_STEM = "fig33_decomposition"
FORMATS = ('pdf', 'png')
DPI = 600

INK = '#111111'
ZERO = '0.55'                       # the y = 0 rule

# (csv column, legend label, colour, line style).  Colours are slots 1-6 of the
# documented categorical order, in order; line style groups squares against
# interferences and is the secondary encoding.
SOLID = (0, ())
DASH = (0, (4.5, 2.2))
TERMS = [
    ("born2",      r'$|B|^2$',                       '#2a78d6', SOLID),
    ("delta2",     r'$|\Delta|^2$',                  '#eb6834', SOLID),
    ("vec2",       r'$|V|^2$',                       '#1baf7a', SOLID),
    ("born_delta", r'$2\,\mathrm{Re}\,B\Delta^{*}$', '#eda100', DASH),
    ("born_vec",   r'$2\,\mathrm{Re}\,BV^{*}$',      '#e87ba4', DASH),
    ("delta_vec",  r'$2\,\mathrm{Re}\,\Delta V^{*}$', '#008300', DASH),
]
TOTAL = ("total", 'sum (total $\\sigma$)', INK, SOLID)

# |V|^2 broken into its two exchanged mesons, |V|^2 = |om|^2 + |rho|^2 + 2Re(om rho*).
#
# These are NOT new categorical identities -- they are the inside of the |V|^2
# series -- so they carry ITS hue at a lighter weight rather than consuming two
# more slots, and they are indented in the legend.  The point they make: the
# omega is isoscalar and neutral, so the t-channel vertex gamma -> pi + V can
# only exchange it when the pion is neutral.  It carries the pi0 channels'
# vector contribution almost entirely (F_omega = 21.11 against F_rho = 2.6),
# and it is identically zero for charged pions, which is why their |V|^2 is
# ~30x smaller.  The omega-rho cross term is left out of the drawing: it is the
# small remainder, it is in the csv, and a third line here would not be read.
VEC_COLOUR = '#1baf7a'
VEC_PARTS = [
    ("omega2", r'   $|\omega|^2$', (0, (1.2, 1.6))),
    ("rho2",   r'   $|\rho|^2$',   (0, (3.0, 1.4, 0.8, 1.4))),
]
LW_PART = 0.9

LW = 1.1
LW_TOTAL = 1.4
XMIN_EG, XMAX_EG = 0.10, S.XMAX_EG
YPAD = 1.06                         # headroom over the extreme values drawn
YSTEP = 100                         # tick spacing in ub


def read_decomposition(path=DECOMP_CSV):
    """{channel: {column: array}} plus 'Egamma_corr', from the long-format csv."""
    if not os.path.exists(path):
        sys.exit(f"{path} not found -- build it first with:\n"
                 f"    math -script fig33_decomposition.m")
    with open(path) as f:
        head = [c.strip().strip('"') for c in f.readline().strip().split(",")]
        rows = collections.defaultdict(list)
        for line in f:
            c = [x.strip().strip('"') for x in line.strip().split(",")]
            if len(c) < len(head):
                continue
            rows[c[0]].append([float(x) for x in c[1:]])
    out = {}
    for ch, v in rows.items():
        a = np.array(sorted(v))
        out[ch] = {n: a[:, i] for i, n in enumerate(head[1:])}
    print(f"{path}: " + ", ".join(f"{c} ({len(out[c]['Egamma_corr'])} pts)"
                                  for c in sorted(out)))
    return out


def make_figure(data, channels, stem=OUT_STEM, xmax=XMAX_EG, ylim=None,
                split_vector=True, formats=FORMATS, dpi=DPI):
    S._journal_style()
    order = [k for k in ['pi-p', 'pi+n', 'pi0p', 'pi0n'] if k in channels]
    parts = VEC_PARTS if split_vector and all(
        c in data[k] for k in order for c, *_ in VEC_PARTS) else []
    if split_vector and not parts:
        print("note: no omega/rho columns in the csv -- rebuild it with "
              "`math -script fig33_decomposition.m` to split |V|^2")
    ncol = 2 if len(order) > 1 else 1
    nrow = int(np.ceil(len(order) / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(7.0, 2.6 * nrow + 0.1),
                             sharex=True, sharey=True, squeeze=False)
    panel = ['(a)', '(b)', '(c)', '(d)']

    # One shared scale, so the channels can be compared directly.  Taken from
    # what is actually inside the plotted x-window, not the whole grid.
    if ylim is None:
        lo, hi = 0.0, 0.0
        for key in order:
            d = data[key]
            win = d['Egamma_corr'] <= xmax
            for col in [c for c, *_ in TERMS + [TOTAL]] + [c for c, *_ in parts]:
                lo = min(lo, np.nanmin(d[col][win]))
                hi = max(hi, np.nanmax(d[col][win]))
        ylim = (YPAD * lo, YPAD * hi)

    for n, (ax, key) in enumerate(zip(axes.ravel(), order)):
        ch = S.CHANNELS[key]
        d = data[key]
        eg = d['Egamma_corr']
        ax.axhline(0.0, color=ZERO, lw=0.7, zorder=1)
        for col, label, colour, ls in TERMS:
            ax.plot(eg, d[col], color=colour, ls=ls, lw=LW, zorder=3,
                    solid_joinstyle='round')
        # under |V|^2, and under the other curves, so it never hides a term
        for col, label, ls in parts:
            ax.plot(eg, d[col], color=VEC_COLOUR, ls=ls, lw=LW_PART, zorder=2)
        ax.plot(eg, d[TOTAL[0]], color=TOTAL[2], ls=TOTAL[3], lw=LW_TOTAL,
                zorder=4, solid_joinstyle='round')

        ax.set_xlim(XMIN_EG, xmax)
        ax.set_ylim(*ylim)
        ax.set_yticks(np.arange(YSTEP * np.ceil(ylim[0] / YSTEP),
                                YSTEP * np.floor(ylim[1] / YSTEP) + 1, YSTEP))
        ax.text(0.035, 0.95, panel[n], transform=ax.transAxes, va='top',
                fontsize=8.5)
        ax.text(0.965, 0.95, r'$%s$' % ch.label, transform=ax.transAxes,
                va='top', ha='right', fontsize=11)
        if n // ncol == nrow - 1:
            ax.set_xlabel(r'$E_{\gamma}$  (GeV)')
        if n % ncol == 0:
            ax.set_ylabel(r'contribution to $\sigma$  ($\mu$b)')
    for ax in axes.ravel()[len(order):]:
        ax.set_visible(False)

    # More entries than any panel corner could hold without landing on a curve,
    # so the key goes above the grid where it collides with nothing.  A legend
    # fills COLUMN-major, so the handles are ordered to make each column one
    # group: the two big squares with their interference, then the vector
    # sector with the mesons inside it, then the vector interferences and sum.
    h = {col: Line2D([], [], color=c, ls=ls, lw=LW, label=lab)
         for col, lab, c, ls in TERMS}
    h.update({col: Line2D([], [], color=VEC_COLOUR, ls=ls, lw=LW_PART,
                          label=lab) for col, lab, ls in parts})
    h[TOTAL[0]] = Line2D([], [], color=TOTAL[2], ls=TOTAL[3], lw=LW_TOTAL,
                         label=TOTAL[1])
    columns = [["born2", "delta2", "born_delta"],
               ["vec2"] + [c for c, *_ in parts],
               ["born_vec", "delta_vec", "total"]]
    handles = [h[c] for col in columns for c in col]
    # top=0.99 first: the legend is anchored to the figure, so without it the
    # default top margin opens a band of white between key and panels.
    fig.subplots_adjust(top=0.99, hspace=0.06, wspace=0.06)
    fig.legend(handles=handles, loc='lower center', ncol=len(columns),
               bbox_to_anchor=(0.5, 1.0), borderaxespad=0.0,
               columnspacing=1.6, handlelength=2.2)
    for ext in formats:
        fig.savefig(f'{stem}.{ext}', dpi=dpi)
    plt.close(fig)
    print(f"wrote {', '.join(f'{stem}.{e}' for e in formats)}")


def summary(data, channels, xmax=XMAX_EG):
    """Each term at the resonance and well above it, plus the closure check."""
    for label, target in (("at the Delta peak", 0.335), ("at 0.80 GeV", 0.800)):
        print(f"\ncontributions to sigma in ub, {label}")
        print("%-6s" % "chan" + "".join("%12s" % n for n, *_ in TERMS)
              + "%12s%10s" % ("sum", "closure"))
        for key in channels:
            d = data[key]
            i = int(np.argmin(np.abs(d['Egamma_corr'] - target)))
            vals = [d[col][i] for col, *_ in TERMS]
            tot = d['total'][i]
            print("%-6s" % key + "".join("%12.2f" % v for v in vals)
                  + "%12.2f%10.1e" % (tot, abs(sum(vals) / tot - 1.0)))

    # The omega/rho split of |V|^2: which meson can be exchanged is what makes
    # the charged channels' vector contribution small, so it gets its own table.
    if not all('omega2' in data[k] for k in channels):
        return
    for label, target in (("at the Delta peak", 0.335), ("at 0.80 GeV", 0.800)):
        print(f"\n|V|^2 by exchanged meson in ub, {label}")
        print("%-6s%12s%12s%12s%12s" % ("chan", "|V|^2", "|omega|^2", "|rho|^2",
                                        "2Re om rho"))
        for key in channels:
            d = data[key]
            i = int(np.argmin(np.abs(d['Egamma_corr'] - target)))
            print("%-6s%12.2f%12.2f%12.2f%12.2f"
                  % (key, d['vec2'][i], d['omega2'][i], d['rho2'][i],
                     d['omega_rho'][i]))


def main():
    p = argparse.ArgumentParser(
        description="Draw the six contributions to sigma(gamma N -> pi N) from "
                    "fig33_decomposition.csv.  Computes nothing.")
    p.add_argument("--channels", default=",".join(S.CHANNELS),
                   help="comma-separated subset of " + ", ".join(S.CHANNELS))
    p.add_argument("--stem", default=OUT_STEM, help="output filename stem")
    p.add_argument("--xmax", type=float, default=XMAX_EG,
                   help="right edge, as a photon energy in GeV")
    p.add_argument("--ymin", type=float, default=None, help="bottom of the axis")
    p.add_argument("--ymax", type=float, default=None, help="top of the axis")
    p.add_argument("--formats", default=",".join(FORMATS),
                   help="comma-separated output extensions")
    p.add_argument("--dpi", type=int, default=DPI, help="raster resolution")
    p.add_argument("--no-split-vector", action="store_true",
                   help="draw |V|^2 whole, without its omega and rho parts")
    args = p.parse_args()

    data = read_decomposition()
    channels = [c.strip() for c in args.channels.split(",") if c.strip()]
    missing = [c for c in channels if c not in data]
    if missing:
        print("note: not in the csv, skipped: " + ", ".join(missing))
    channels = [c for c in channels if c in data]
    if not channels:
        sys.exit("nothing to draw")

    ylim = None
    if args.ymin is not None and args.ymax is not None:
        ylim = (args.ymin, args.ymax)
    formats = tuple(e.strip().lstrip('.') for e in args.formats.split(',')
                    if e.strip())
    make_figure(data, channels, stem=args.stem, xmax=args.xmax, ylim=ylim,
                split_vector=not args.no_split_vector,
                formats=formats, dpi=args.dpi)
    summary(data, channels, xmax=args.xmax)


if __name__ == "__main__":
    main()
