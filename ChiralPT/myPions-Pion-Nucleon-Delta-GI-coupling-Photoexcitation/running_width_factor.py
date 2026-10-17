#!/usr/bin/env python3
"""running_width_factor.py -- the running-width correction w(E_nu), per channel.

    w_ch(E_nu) = sigma_ch(E_nu; Breit-Wigner M_Delta, Gamma_0, Gamma ~ k^3)
               / sigma_ch(E_nu; pole M_Delta, Gamma_Delta, constant width)

This is the ratio of the thin to the thick curves of the paper's App. F
CC1pi figure (figures_appendix/cc1pi_appendix.pdf).  Sherpa can only carry a
constant Delta width, so the running width is computed with the semi-analytic
amplitude, width_study.py, on the same UFO:

  denominator  PSET=pole, edw=''     M = 1.209, Gamma = 102 MeV, constant
  numerator    PSET=bw,   edw='hnv'  M = 1.232, Gamma_0 = 117.7 MeV,
               Gamma(W) = Gamma_0 (M/W)(k/k_0)^3, and hD, G1, G2 re-derived
               from the Breit-Wigner widths

Both are evaluated with the same quadrature grid, so most of the grid error
cancels in the ratio.  Multiplying a Sherpa constant-width curve (or each of
its events, at that event's E_nu) by w gives the running-width prediction.

BUILD THE TABLE
    UFO=ChiPT_UFO_V15 PSET=pole EDWS=     WMAXES=1.4,none EXTRAS=0 \\
        ENERGIES=0.3,...,3.0 OUT=width_study_V15.csv    python3 width_study.py
    UFO=ChiPT_UFO_V15 PSET=bw   EDWS=hnv  WMAXES=1.4,none EXTRAS=0 \\
        ENERGIES=0.3,...,3.0 OUT=width_study_V15_BW.csv python3 width_study.py
    python3 running_width_factor.py --pole width_study_V15.csv \\
        --bw width_study_V15_BW.csv --out running_width_factor_V15.csv

  writes running_width_factor_V15.csv  (channel, wmax, E_nu, w)
         running_width_factor_V15.pdf/.png  (w(E_nu) per channel, paper style)

USE IT
    from running_width_factor import RunningWidthFactor
    rw = RunningWidthFactor("running_width_factor_V15.csv", wmax="1.4")
    w = rw("ppip", 1.2)              # one event
    w = rw("ppip", E_array)          # a scan

WHICH W CUT.  wmax "1.4" is the ANL/BNL comparison: both sigmas carry
W < 1.4 GeV.  wmax "none" is the uncut ratio, the one to use for event samples
with no W cut (nuclear targets).  They differ because the running width moves
strength between the peak and the region above it.

INTERPOLATION.  Linear in E_nu between the computed energies.  Outside the
table, the value at the nearest end is held: below the lowest energy the
channel is within ~20 MeV of threshold and carries almost no rate, and above
the highest energy the W < 1.4 ratio has stopped changing (the cut fixes the
W range).  The uncut ratio still drifts slowly at 3 GeV; check the table's
last points before using it far above that.
"""

import argparse
import csv
import os
import re

import numpy as np

CHANNELS = ("ppip", "ppi0", "npip")
LEGEND = r"+ Breit--Wigner $M_\Delta, \Gamma_0$, $\Gamma_\Delta \propto k^3$"


def _wkey(w):
    """'1.4', '1.40', 1.4 -> '1.4';  None, '', 'none' -> 'none'."""
    if w is None or str(w).strip().lower() in ("", "none"):
        return "none"
    return "%g" % float(w)


_LOG = re.compile(r"^\s+(\w+)\s+E=([\d.]+)\s+(\S+)\s+wmax=(\S+)\s+"
                  r"R=(\S+)\s+->\s+(\S+)")


def _read_log(path, edw):
    """The progress lines width_study.py prints, for a run still in flight
    (it writes its CSV only at the end)."""
    out = {}
    for line in open(path):
        m = _LOG.match(line)
        if not m:
            continue
        ch, e, ew, wm, bwr, sig = m.groups()
        ew = "" if ew == "fixed" else ew
        if ew != edw or bwr not in ("1.0", "1"):
            continue
        out[(ch, _wkey(wm), float(e))] = float(sig)
    return out


def _read_study(path, edw):
    if path.endswith(".log"):
        return _read_log(path, edw)
    out = {}
    for r in csv.DictReader(l for l in open(path) if not l.startswith("#")):
        if r["edw"] != edw or r.get("bwr_fm", "1.0") not in ("1.0", "1"):
            continue
        out[(r["channel"], _wkey(r["wmax"]), float(r["E_nu"]))] = \
            float(r["sigma"])
    return out


def _read_many(paths, edw):
    """Several studies of one prescription; a later file overrides an earlier
    one point by point (e.g. a finer-grid rerun of some energies)."""
    out = {}
    for path in str(paths).split(","):
        out.update(_read_study(path.strip(), edw))
    return out


def build(pole_csv, bw_csv):
    """{(channel, wmax): (E array, w array)} from a width_study pair.  Each
    argument may be a comma-separated list, later files taking precedence."""
    den = _read_many(pole_csv, "")
    num = _read_many(bw_csv, "hnv")
    tab = {}
    for (ch, wm, e), s0 in den.items():
        s1 = num.get((ch, wm, e))
        if s1 is None or s0 <= 0.0:
            continue
        tab.setdefault((ch, wm), []).append((e, s1 / s0))
    return {k: tuple(np.array(c) for c in zip(*sorted(v)))
            for k, v in tab.items()}


def write(tab, path, pole_csv, bw_csv):
    hdr = []
    for f in [x.strip() for x in f"{pole_csv},{bw_csv}".split(",")]:
        first = open(f).readline().strip()
        if f.endswith(".log"):
            first = "progress log of a width_study.py run"
        hdr.append("# %s: %s" % (os.path.basename(f), first.lstrip("# ")))
    with open(path, "w", newline="") as f:
        f.write("# Running-width correction w(E_nu) = sigma(BW, Gamma ~ k^3) /"
                " sigma(pole, constant Gamma),\n# per CC1pi channel and W cut."
                "  Written by running_width_factor.py from\n")
        f.write("\n".join(hdr) + "\n")
        f.write("# Interpolate linearly in E_nu; hold the end values outside"
                " the table.\n")
        w = csv.writer(f)
        w.writerow(["channel", "wmax", "E_nu", "w"])
        for (ch, wm), (E, R) in sorted(tab.items()):
            for e, r in zip(E, R):
                w.writerow([ch, wm, "%.4f" % e, "%.6f" % r])
    print("wrote", path)


class RunningWidthFactor:
    """w(channel, E_nu) from a running_width_factor_*.csv table."""

    def __init__(self, path, wmax="1.4"):
        self.wmax = _wkey(wmax)
        tab = {}
        for r in csv.DictReader(l for l in open(path)
                                if not l.startswith("#")):
            if _wkey(r["wmax"]) != self.wmax:
                continue
            tab.setdefault(r["channel"], []).append(
                (float(r["E_nu"]), float(r["w"])))
        if not tab:
            raise ValueError("no rows with wmax=%s in %s" % (self.wmax, path))
        self.table = {ch: tuple(np.array(c) for c in zip(*sorted(v)))
                      for ch, v in tab.items()}

    def __call__(self, channel, E_nu):
        """w at E_nu (GeV).  1 for a channel the table does not cover."""
        if channel not in self.table:
            return np.ones_like(np.asarray(E_nu, float)) \
                if np.ndim(E_nu) else 1.0
        E, R = self.table[channel]
        out = np.interp(E_nu, E, R)          # holds the end values
        return out if np.ndim(E_nu) else float(out)


def plot(tab, stem):
    import paper_style as ps
    import matplotlib.pyplot as plt
    from matplotlib.lines import Line2D
    ps.apply()
    fig, ax = ps.figure()
    for ch in CHANNELS:
        for wm, ls in (("1.4", "-"), ("none", (0, (4, 2)))):
            if (ch, wm) not in tab:
                continue
            E, R = tab[(ch, wm)]
            ax.plot(E, R, color=ps.COLOR[ch], ls=ls,
                    lw=ps.LW_MAIN if wm == "1.4" else ps.LW_VARIANT,
                    marker="o", ms=3.0)
    ax.axhline(1.0, color=ps.GREY, lw=0.8, zorder=0)
    ax.set_xlabel(r"$E_\nu$ (GeV)")
    ax.set_ylabel(r"$w(E_\nu) = \sigma_{\rm running}/\sigma_{\rm constant}$")
    emax = max(E.max() for E, _ in tab.values())
    ax.set_xlim(0.3, emax)
    ink = "#3a3a3a"
    h = [Line2D([], [], color=ps.COLOR[ch], lw=ps.LW_MAIN, label=ps.LABEL[ch])
         for ch in CHANNELS]
    h += [Line2D([], [], color=ink, lw=ps.LW_MAIN, label=r"$W < 1.4$ GeV"),
          Line2D([], [], color=ink, lw=ps.LW_VARIANT, ls=(0, (4, 2)),
                 label="no $W$ cut")]
    ax.legend(handles=h, loc="upper right", fontsize=10.5)
    for ext in ("pdf", "png"):
        fig.savefig("%s.%s" % (stem, ext), dpi=300)
    print("wrote %s.pdf and %s.png" % (stem, stem))


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--pole", required=True,
                    help="width_study CSV(s) or .log(s), PSET=pole, edw='' rows; "
                         "comma-separated, later files override earlier")
    ap.add_argument("--bw", required=True,
                    help="width_study CSV(s) or .log(s), PSET=bw, edw='hnv' rows; "
                         "comma-separated, later files override earlier")
    ap.add_argument("--out", required=True, help="output table (.csv)")
    ap.add_argument("--no-plot", action="store_true")
    a = ap.parse_args()
    tab = build(a.pole, a.bw)
    if not tab:
        raise SystemExit("no matching (channel, wmax, E_nu) rows in the pair")
    for (ch, wm), (E, R) in sorted(tab.items()):
        print("%-5s W<%-4s " % (ch, wm)
              + " ".join("%.2f:%.3f" % (e, r) for e, r in zip(E, R)))
    write(tab, a.out, a.pole, a.bw)
    if not a.no_plot:
        plot(tab, os.path.splitext(a.out)[0])


if __name__ == "__main__":
    main()
