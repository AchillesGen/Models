"""
plot_scan.py -- standalone publication figures for sigma(gamma N -> pi N).

This is scan.py's `--plot-only` path in a single-panel layout and nothing else.
It reads results that already exist on disk and draws them; it never launches
Sherpa, never touches Process/ or Results.zip, and never recomputes the
semi-analytic curves.  Every input is a plain file:

    scan_results.csv               Sherpa points, all channels, from scan.py
    beam_scan_pA_pPi0.txt          the older pi0p-only layout, used if the csv
                                   is not there
    fig33_reference_scan_grid.csv  semi-analytic curves on the same grid
    fig33_vecmeson_scan_grid.csv   ... plus omega/rho exchange (optional)
    ../ELA-Pion-Photoproduction/pi0p_data.m   the measured points of Fig. 33

If any of them is stale or missing, this script says so and leaves that piece
out of the figure -- it will not regenerate it.  Rebuild inputs deliberately:

    python3 scan.py                # re-run the Sherpa scan (slow)
    math -script fig33_vecmeson.m  # vector-meson curves on the current grid

The channel table, the csv layouts and the readers all live in scan.py, which
is imported for them; importing it runs nothing.  One figure per channel against
sqrt(s) and against Egamma, plus a 2x2 sheet of all channels.  No ratio panel --
that is scan.py's layout.

Run:  python3 plot_scan.py [-h] [--channels pi0p,pi+n,...]
"""

import argparse
import os
import sys

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

import scan as S

HERE = os.path.dirname(os.path.abspath(__file__))

# === INPUTS (read-only; nothing here is ever written or rebuilt) ===
SCAN_CSV = S.SCAN_CSV
REFERENCE_CACHE = S.REFERENCE_CACHE
VECMESON_CSV = S.VECMESON_CSV
DATA_FILE = S.DATA_FILE

# === FIGURE TUNING ===
# Colours are the two categorical slots of the palette validated in
# fig33_from_ufo.py (#2a78d6 / #eb6834: CVD dE 24.7 protan, 33.6 normal
# vision).  Line style and marker shape carry the same distinction, so nothing
# rests on colour alone.  The model table itself is scan.py's:
#   (model dir, param card, legend label, semi-analytic scheme, colour, ls, marker)
MODELS = S.MODELS

# The Fig. 33 prescription itself: sqrt(X_pi(s,u)) at amplitude level with a
# running Delta width.  Drawn as the solid black reference curve.
REFERENCE_KEY = S.DENOMINATOR
REFERENCE_LABEL = S.REFERENCE_LABEL
VECMESON_KEY = S.VECMESON_KEY

# Measured sigma(gamma p -> pi0 p), the points Fig. 33 itself shows -- pi0p
# only; the other three channels are drawn without data.
#
# CAVEAT on the high set: its rows carry cos(theta) limits (-0.85 to
# 0.65/0.75), so it is an angle-RESTRICTED integral, not a full total cross
# section -- which is why it sits ~25% under the low set where the two
# overlap.  Only the low set is strictly commensurate with the curves, and it
# is the only one enabled below.
DATA_STYLE = {                       # set -> (label, marker, filled)
    'low':  (r'data', 'o', True),
#   'high': ('data, higher res.', '^', False),
}

FIGSIZE = (3.5, 2.7)                 # single-column PRC/PRD width
INK = '#111111'
YMAX_SIGMA = None                    # None -> the channel's own ymax
YTICK_STEP = 100
XMAX_EG = S.XMAX_EG                  # figures stop where Fig. 33 does
XMIN_EG = 0.10
LW_REFERENCE = 1.3
LW_CURVE = 1.1
MS_SHERPA = 2.8
MS_DATA = 2.6                        # filled sets; open sets get +0.4
LEGEND_LOC = 'upper right'           # models + semi-analytic curves
DATA_LEGEND_LOC = 'upper left'
# How the analytic-vs-Sherpa distinction is spelled out.
#
# LEGEND_SPLIT False: one row per model, its handle showing the dashed line
# with the marker on it, and the convention stated once in the legend title.
# Four rows instead of six, and the model labels are not repeated.
#
# LEGEND_SPLIT True: two rows per model, line and marker named separately.
# Wordier, but leaves nothing to a header if the figure travels without its
# caption.  {label} is the model's entry in MODELS.
LEGEND_SPLIT = False
LEGEND_TITLE = 'lines: analytic,  points: Sherpa'
LEGEND_TITLE_SIZE = 7
LEGEND_TITLE_COLOUR = '0.35'
ANALYTIC_LABEL = "{label}, analytic"
SHERPA_LABEL = "{label}, Sherpa"
# In scan.py this note sat in the ratio panel; with a single panel there is no
# corner it does not collide with, and the legend glyphs (dashed line + marker
# on one handle) already say it.  Left as a knob: set it to a string to draw
# it, otherwise it belongs in the caption.
NOTE = ''                            # e.g. 'lines: semi-analytic,  markers: Sherpa'
NOTE_XY = (0.985, 0.06)              # axes fraction; ha/va are right/bottom
OVERVIEW_STEM = 'plot_all_channels'  # the 2x2 sheet
FORMATS = ('pdf', 'png')
DPI = 600

MN_FALLBACK = S.MN_FALLBACK
MPI0 = S.MPI0
MDELTA = S.MDELTA                    # sqrt(s) marker on the sqrt(s) figure

# === END CONFIGURATION ===


def eg_to_w(eg, mn):
    return np.sqrt(mn ** 2 + 2.0 * mn * np.asarray(eg))


def read_curves(path, eg_corr):
    """{(channel, name): sigma_ub} from one of the cached csv files."""
    if not os.path.exists(path):
        print(f"note: {path} not found -- those curves are omitted")
        return {}
    out = S.read_wide_csv(path, eg_corr)
    if out:
        print(f"{path}: " + ", ".join(f"{c}/{n}" for c, n in sorted(out)))
    return out


def read_pi0p_data(path, mn, channel):
    """{'low'|'high': (Eg, sigma_ub, err)} -- the points plotted in Fig. 33."""
    if channel != S.DATA_CHANNEL or not os.path.exists(path):
        return {}
    txt = open(path).read()

    def block(name, ncol):
        i = txt.index(name)
        i = txt.index('{', i) + 1
        j = txt.index('}', i)
        nums = [float(x) for x in txt[i:j].replace('\n', ' ').split(',')
                if x.strip()]
        return np.array(nums).reshape(-1, ncol)

    try:
        hi = block('dHiRaw = Partition[', 6)
        lo = block('dLoRaw = Partition[', 4)
    except (ValueError, IndexError) as exc:
        print(f"note: cannot parse {path} ({exc}) -- no measured data")
        return {}
    both = {
        'low': np.column_stack([(lo[:, 0] ** 2 - mn ** 2) / (2 * mn),
                                lo[:, 1], lo[:, 2]]),
        'high': np.column_stack([hi[:, 0] / 1000.0, hi[:, 1], hi[:, 2]]),
    }
    return {k: v for k, v in both.items() if k in DATA_STYLE}


def journal_style():
    """PRC/PRD conventions: serif face, inward ticks all round, hairline axes."""
    plt.rcParams.update({
        'font.family': 'serif',
        'font.serif': ['STIXGeneral', 'DejaVu Serif'],
        'mathtext.fontset': 'stix',
        'font.size': 9, 'axes.labelsize': 9,
        'xtick.labelsize': 8, 'ytick.labelsize': 8, 'legend.fontsize': 7.5,
        'axes.linewidth': 0.7,
        'xtick.direction': 'in', 'ytick.direction': 'in',
        'xtick.top': True, 'ytick.right': True,
        'xtick.minor.visible': True, 'ytick.minor.visible': True,
        'xtick.major.width': 0.7, 'ytick.major.width': 0.7,
        'xtick.minor.width': 0.5, 'ytick.minor.width': 0.5,
        'xtick.major.size': 3.4, 'ytick.major.size': 3.4,
        'xtick.minor.size': 1.9, 'ytick.minor.size': 1.9,
        'legend.frameon': False, 'legend.handlelength': 2.4,
        'legend.labelspacing': 0.35, 'legend.borderpad': 0.0,
        'savefig.bbox': 'tight', 'savefig.pad_inches': 0.02,
    })


def draw(ax, ch, eg_grid, scans, refs, x_of_eg, data=()):
    """One channel's curves, Sherpa points and measured points on one axis.

    `eg_grid` is the corrected photon energy the semi-analytic curves live on
    and `x_of_eg` maps a corrected photon energy onto the abscissa.  The Sherpa
    points carry their own corrected energies -- a subset of eg_grid for the
    charged channels, whose threshold is higher.
    """
    xgrid = x_of_eg(eg_grid)

    ref = refs.get((ch.key, REFERENCE_KEY))
    if ref is not None:
        ax.plot(xgrid, ref, color=INK, ls='-', lw=LW_REFERENCE, zorder=4,
                solid_joinstyle='round')

    vec = refs.get((ch.key, VECMESON_KEY))
    if vec is not None:
        ax.plot(xgrid, vec, color=INK, ls=(0, (5.0, 2.0)), lw=LW_CURVE, zorder=4)

    # Measured points, drawn first so the curves read on top of them.
    for name, (label, marker, filled) in DATA_STYLE.items():
        if name not in data:
            continue
        eg, sig, err = data[name].T
        ax.errorbar(x_of_eg(eg), sig, yerr=err, ls='none', marker=marker,
                    ms=MS_DATA if filled else MS_DATA + 0.4,
                    mfc=INK if filled else 'none', mec=INK, mew=0.7,
                    ecolor=INK, elinewidth=0.5, capsize=0, zorder=2)

    for model, card, label, scheme, colour, ls, marker in MODELS:
        curve = refs.get((ch.key, scheme))
        if curve is not None:
            ax.plot(xgrid, curve, color=colour, ls=ls, lw=LW_CURVE, zorder=3)
        sc = scans.get((ch.key, model))
        if sc is not None:
            ax.errorbar(x_of_eg(sc.eg_corr), sc.sigma, yerr=sc.err, ls='none',
                        marker=marker, ms=MS_SHERPA,
                        mfc=colour if marker == 'o' else 'none', mec=colour,
                        mew=0.7, ecolor=colour, elinewidth=0.6, capsize=0,
                        zorder=5)


def legend(ax, ch, scans, refs, data, loc=LEGEND_LOC, bbox=None,
           data_loc=DATA_LEGEND_LOC, data_bbox=None):
    """Curve/model key, plus the measured-set key when there is data.

    `bbox`/`data_bbox` (axes fraction) let a caller tuck a box under a panel
    label instead of into the corner the label already holds.
    """
    handles = []
    if (ch.key, REFERENCE_KEY) in refs:
        handles.append(Line2D([], [], color=INK, ls='-', lw=LW_REFERENCE,
                              label=REFERENCE_LABEL))
    if (ch.key, VECMESON_KEY) in refs:
        handles.append(Line2D([], [], color=INK, ls=(0, (5.0, 2.0)),
                              lw=LW_CURVE, label=r'  $+\ \omega,\rho$ exchange'))
    for mo, _, lab, scheme, c, ls, m in MODELS:
        if (ch.key, mo) not in scans and (ch.key, scheme) not in refs:
            continue
        mfc = c if m == 'o' else 'none'
        if LEGEND_SPLIT:
            # Line and marker named separately, adjacent so colour pairs them.
            handles.append(Line2D([], [], color=c, ls=ls, lw=LW_CURVE,
                                  label=ANALYTIC_LABEL.format(label=lab)))
            handles.append(Line2D([], [], ls='none', marker=m, ms=MS_SHERPA,
                                  mfc=mfc, mec=c, mew=0.7,
                                  label=SHERPA_LABEL.format(label=lab)))
        else:
            # One row, the handle carrying both: dashes with the marker on them.
            handles.append(Line2D([], [], color=c, ls=ls, lw=LW_CURVE, marker=m,
                                  ms=MS_SHERPA, mfc=mfc, mec=c, mew=0.7,
                                  label=lab))
    leg = None
    if handles:
        title = None if LEGEND_SPLIT else LEGEND_TITLE
        leg = ax.legend(handles=handles, loc=loc, bbox_to_anchor=bbox,
                        borderaxespad=0.7, title=title)
        if title:
            leg.get_title().set(fontsize=LEGEND_TITLE_SIZE,
                                color=LEGEND_TITLE_COLOUR)
    dh = [Line2D([], [], ls='none',
                 marker=m, ms=MS_SHERPA if f else MS_SHERPA + 0.4,
                 mfc=INK if f else 'none', mec=INK, mew=0.7, label=lab)
          for k, (lab, m, f) in DATA_STYLE.items() if k in data]
    if dh:
        if leg is not None:
            ax.add_artist(leg)
        ax.legend(handles=dh, loc=data_loc, bbox_to_anchor=data_bbox,
                  borderaxespad=0.7)


def make_figure(ch, eg_grid, xlabel, xlim, scans, refs, stem, x_of_eg, data=(),
                mark_delta=False, ymax=None, formats=FORMATS, dpi=DPI):
    """One publication figure: sigma on a single panel."""
    journal_style()
    fig, ax = plt.subplots(figsize=FIGSIZE)

    draw(ax, ch, eg_grid, scans, refs, x_of_eg, data)

    if mark_delta:
        ax.axvline(MDELTA, color='0.75', lw=0.7, ls=':', zorder=0)
        # low, not high: the upper-left corner belongs to the data legend
        ax.annotate(r'$M_\Delta$', (MDELTA, 0.02),
                    xycoords=('data', 'axes fraction'), ha='left', va='bottom',
                    fontsize=8, color='0.45', xytext=(2.5, 0),
                    textcoords='offset points')

    legend(ax, ch, scans, refs, data)
    if NOTE:
        ax.text(*NOTE_XY, NOTE, transform=ax.transAxes, va='bottom',
                ha='right', fontsize=7, color='0.35')

    ymax = ymax or ch.ymax
    ax.set_ylabel(r'$\sigma(%s)$  [$\mu$b]' % ch.label)
    ax.set_ylim(0, ymax)
    ax.set_yticks(np.arange(0, ymax - YTICK_STEP // 2, YTICK_STEP))
    ax.set_xlabel(xlabel)
    ax.set_xlim(*xlim)

    for ext in formats:
        fig.savefig(f'{stem}.{ext}', dpi=dpi)
    plt.close(fig)
    print(f"wrote {', '.join(f'{stem}.{e}' for e in formats)}")


def make_overview(channels, eg_grid, scans, refs, mn, stem=OVERVIEW_STEM,
                  xmax=XMAX_EG, ymax=None, formats=FORMATS, dpi=DPI):
    """All the channels on one 2x2 sheet, in the layout of Fig. 33 itself."""
    journal_style()
    order = [k for k in ['pi-p', 'pi+n', 'pi0p', 'pi0n'] if k in channels]
    ymax = ymax or max(S.CHANNELS[k].ymax for k in order)
    ncol = 2 if len(order) > 1 else 1
    nrow = int(np.ceil(len(order) / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(7.0, 2.5 * nrow + 0.1),
                             sharex=True, sharey=True, squeeze=False)
    panel = ['(a)', '(b)', '(c)', '(d)']

    panel_ax = {}
    for n, (ax, key) in enumerate(zip(axes.ravel(), order)):
        ch = S.CHANNELS[key]
        panel_ax[key] = ax
        draw(ax, ch, eg_grid, scans, refs, np.asarray,
             read_pi0p_data(DATA_FILE, mn, key))
        ax.set_xlim(XMIN_EG, xmax)
        ax.set_ylim(0, ymax)
        ax.set_yticks(np.arange(0, ymax - YTICK_STEP // 2, YTICK_STEP))
        ax.text(0.035, 0.93, panel[n], transform=ax.transAxes, va='top',
                fontsize=8.5)
        ax.text(0.965, 0.93, r'$%s$' % ch.label, transform=ax.transAxes,
                va='top', ha='right', fontsize=11)
        if n // ncol == nrow - 1:
            ax.set_xlabel(r'$E_{\gamma}$  [GeV]')
        if n % ncol == 0:
            ax.set_ylabel(r'$\sigma$  [$\mu$b]')
    for ax in axes.ravel()[len(order):]:
        ax.set_visible(False)

    # The legend is a whole panel's worth of text, so it goes where there is
    # actually room: the channel that runs lowest to the right of the
    # resonance, anchored below that panel's channel label rather than in the
    # corner the label already holds.
    host = min(order, key=lambda k: S._headroom(k, eg_grid, scans, refs,
                                                S.LEGEND_EG_MIN))
    legend(panel_ax[host], S.CHANNELS[host], scans, refs, {},
           bbox=S.LEGEND_BBOX)
    # The measured points are pi0p's alone, so their key belongs on that panel.
    if S.DATA_CHANNEL in panel_ax:
        data = read_pi0p_data(DATA_FILE, mn, S.DATA_CHANNEL)
        dh = [Line2D([], [], ls='none',
                     marker=m, ms=MS_SHERPA if f else MS_SHERPA + 0.4,
                     mfc=INK if f else 'none', mec=INK, mew=0.7, label=lab)
              for k, (lab, m, f) in DATA_STYLE.items() if k in data]
        if dh:
            panel_ax[S.DATA_CHANNEL].legend(
                handles=dh, loc='upper left', borderaxespad=0.7,
                bbox_to_anchor=S.LEGEND_BBOX_LEFT)
    fig.subplots_adjust(hspace=0.06, wspace=0.06)
    for ext in formats:
        fig.savefig(f'{stem}.{ext}', dpi=dpi)
    plt.close(fig)
    print(f"wrote {', '.join(f'{stem}.{e}' for e in formats)}")


def summary(channels, eg_grid, scans, refs, mn, xmax):
    """Peak of every curve inside the plotted window."""
    print("\n%-6s %-22s %10s %10s %12s   (Delta region)"
          % ("chan", "curve", "peak (ub)", "at Eg", "at sqrt(s)"))
    win = eg_grid <= xmax
    for key in channels:
        for model, *_ in MODELS:
            sc = scans.get((key, model))
            if sc is None:
                continue
            i = int(np.argmax(np.where(sc.eg_corr <= xmax, sc.sigma, -np.inf)))
            print("%-6s %-22s %10.1f %10.4f %12.4f"
                  % (key, model, sc.sigma[i], sc.eg_corr[i],
                     eg_to_w(sc.eg_corr[i], mn)))
        for name in S.SCHEMES + (VECMESON_KEY,):
            sig = refs.get((key, name))
            if sig is None:
                continue
            i = int(np.argmax(np.where(win, sig, -np.inf)))
            print("%-6s %-22s %10.1f %10.4f %12.4f"
                  % (key, name, sig[i], eg_grid[i], eg_to_w(eg_grid[i], mn)))
        print()


def main():
    p = argparse.ArgumentParser(
        description="Redraw the gamma N -> pi N scan figures from files on "
                    "disk.  Runs no simulation.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    p.add_argument("--channels", default=",".join(S.CHANNELS),
                   help="comma-separated subset of " + ", ".join(S.CHANNELS))
    p.add_argument("--scan", default=SCAN_CSV, help="Sherpa scan results")
    p.add_argument("--stem", default=None,
                   help="output filename stem; default is scan.py's per-channel "
                        "one, plot_<channel stem>")
    p.add_argument("--formats", default=",".join(FORMATS),
                   help="comma-separated output extensions")
    p.add_argument("--dpi", type=int, default=DPI, help="raster resolution")
    p.add_argument("--xmax", type=float, default=XMAX_EG,
                   help="right edge, as a photon energy in GeV")
    p.add_argument("--ymax", type=float, default=YMAX_SIGMA,
                   help="top of the sigma axis in ub; default per channel")
    p.add_argument("--no-data", action="store_true",
                   help="drop the measured points")
    p.add_argument("--no-overview", action="store_true",
                   help="skip the 2x2 all-channel sheet")
    args = p.parse_args()

    channels = [c.strip() for c in args.channels.split(",") if c.strip()]
    bad = [c for c in channels if c not in S.CHANNELS]
    if bad:
        sys.exit("unknown channel(s): %s;  known: %s"
                 % (", ".join(bad), ", ".join(S.CHANNELS)))

    formats = tuple(e.strip().lstrip('.') for e in args.formats.split(',')
                    if e.strip())

    mn = MN_FALLBACK
    eg_grid = np.array([S.kinematics(e, mn)[1] for e in S.photon_grid(mn)])
    scans = S.read_scan_csv(args.scan)

    refs = read_curves(REFERENCE_CACHE, eg_grid)
    refs.update(read_curves(VECMESON_CSV, eg_grid))

    drawn = []
    for key in channels:
        ch = S.CHANNELS[key]
        if not any((key, m) in scans for m, *_ in MODELS) \
                and not any((key, s) in refs for s in S.SCHEMES):
            print(f"note: nothing on disk for {key} -- skipped")
            continue
        drawn.append(key)
        data = {} if args.no_data else read_pi0p_data(DATA_FILE, mn, key)
        stem = args.stem or 'plot_' + ch.stem
        make_figure(ch, eg_grid, r'$\sqrt{s}$  [GeV]',
                    (mn + MPI0, eg_to_w(args.xmax, mn)), scans, refs,
                    f'{stem}_sqrts', x_of_eg=lambda eg: eg_to_w(eg, mn),
                    data=data, mark_delta=True, ymax=args.ymax,
                    formats=formats, dpi=args.dpi)
        make_figure(ch, eg_grid, r'$E_{\gamma}$  [GeV]', (XMIN_EG, args.xmax),
                    scans, refs, f'{stem}_Egamma', x_of_eg=np.asarray,
                    data=data, ymax=args.ymax, formats=formats, dpi=args.dpi)

    if drawn and len(drawn) > 1 and not args.no_overview:
        make_overview(drawn, eg_grid, scans, refs, mn, xmax=args.xmax,
                      ymax=args.ymax, formats=formats, dpi=args.dpi)

    summary(drawn, eg_grid, scans, refs, mn, args.xmax)


if __name__ == "__main__":
    main()
