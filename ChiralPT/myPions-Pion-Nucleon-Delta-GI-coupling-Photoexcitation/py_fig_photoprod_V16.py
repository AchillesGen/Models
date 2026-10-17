#!/usr/bin/env python3
"""Paper figure: total photoproduction cross sections, all four channels,
model vs data. 2x2 grid. Run from data_collection/photoproduction/.

2026-09-07: switched to Josh's V13 scan (scan_results_updated.csv, model ChiPT_UFO_V13)
and dropped the grey dashed "amplitude-level FFs" reference curve
(fig33_reference_scan_grid.csv).  NOTE (Shirley): that reference curve is to be
plotted again in an APPENDIX figure; the reading code is kept below, commented."""
import csv
import sys
from pathlib import Path
from collections import defaultdict
sys.path.insert(0, str(Path(__file__).resolve().parent))  # py_paperstyle.py sits next to this script
import py_paperstyle as ps
import matplotlib.pyplot as plt

def read(path):
    with open(path) as f:
        return list(csv.DictReader(r for r in f if not r.startswith("#")))

# grid_ref = read("fig33_reference_scan_grid.csv")   # appendix figure, later
scan = read("scan_results.csv")   # V16 Sherpa scan

PANELS = [  # column 1 = proton target, column 2 = neutron target;
            # row 1 = charged pions, row 2 = neutral pions
    ("pi-p",  r"$\gamma n \to p\pi^-$",  "said_gn_ppiminus_SGT.csv"),
    ("pi+n",  r"$\gamma p \to n\pi^+$",  "said_gp_npiplus_SGT.csv"),
    ("pi0p",  r"$\gamma p \to p\pi^0$",  "said_gp_ppi0_SGT.csv"),
    ("pi0n",  r"$\gamma n \to n\pi^0$",  "said_gn_npi0_SGT_integrated.csv"),  # 2026-09-08: A2 quasi-free neutron data, integrated by us from the SAID angular distributions (see the csv header)
]
MARKERS = ["o", "s", "^", "v", "D", "p", "*", "<", ">", "h", "X", "d"]
DATA_COLORS = ["#4d4d4d", "#7f7f7f", "#9e9e9e", "#5d5d5d", "#8f8f8f", "#6f6f6f", "#a8a8a8",
               "#606060", "#909090", "#787878", "#525252", "#a0a0a0"]

fig, axes = ps.grid22()
for ax, (ch, title, datafile) in zip(axes.flat, PANELS):
    # data
    if datafile:
        pts = defaultdict(lambda: ([], [], []))
        for r in read(datafile):
            pts[r["experiment"]][0].append(float(r["E_gamma_MeV"]) / 1e3)
            pts[r["experiment"]][1].append(float(r["sigma_exp_ub"]))
            pts[r["experiment"]][2].append(float(r["err_ub"]))
        for (code, (E, s, e)), m, c in zip(sorted(pts.items()), MARKERS, DATA_COLORS):
            ax.errorbar(E, s, yerr=e, fmt=m, ms=3.5, capsize=1.5, lw=0.8,
                        ls="none", markerfacecolor="none", color=c, zorder=2)
    # curves
    # E = [float(r["Egamma_corr"]) for r in grid_ref]               # appendix figure, later
    # ax.plot(E, [float(r[f"{ch}_reference"]) for r in grid_ref],
    #         color=ps.C_REF, lw=1.4, ls="--", zorder=3)
    sh = sorted((float(r["Egamma_corr"]), float(r["sigma_ub"])) for r in scan
                if r["channel"] == ch and r["model"] == "ChiPT_UFO_V16")
    ax.plot([p[0] for p in sh], [p[1] for p in sh],
            color=ps.C_OURS, lw=2.2, zorder=4)
    ax.text(0.95, 0.92, title, transform=ax.transAxes, ha="right",
            va="top", fontsize=ps.FT)

axes[0, 0].set_xlim(0.14, 0.6)
axes[0, 0].set_ylim(0, 419)
# legend once, in the pi0n panel (least crowded)
import matplotlib.lines as mlines
h = [mlines.Line2D([], [], color=ps.C_OURS, lw=2.2, label=r"this work"),
     mlines.Line2D([], [], color="#7f7f7f", marker="o", markerfacecolor="none", ls="none",
                   ms=3.5, label=r"data (refs.\ in caption)")]
axes[0, 1].legend(handles=h, fontsize=ps.FT - 2, loc="upper left",
                  frameon=False, bbox_to_anchor=(0.03, 0.97))
for ax in axes[1, :]:
    ax.set_xlabel(r"$E_\gamma$ (GeV)", fontsize=ps.FT)
    ax.xaxis.set_label_coords(0.5, -0.10)
for ax in axes[:, 0]:
    ax.set_ylabel(r"$\sigma$ ($\mu$b)", fontsize=ps.FT)
    ax.yaxis.set_label_coords(-0.16, 0.5)

fig.savefig("/home/isaacson/Documents/Projects/NeutrinoGenerator/Achilles/sherpa3-0/build/chipt_nuisance/paper_figures/figures/photoprod_channels.pdf")
print("wrote /home/isaacson/Documents/Projects/NeutrinoGenerator/Achilles/sherpa3-0/build/chipt_nuisance/paper_figures/figures/photoprod_channels.pdf")
