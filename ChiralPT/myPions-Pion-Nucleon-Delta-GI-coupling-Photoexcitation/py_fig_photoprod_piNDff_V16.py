#!/usr/bin/env python3
"""Appendix figure: the effect of the V16 piNDelta vertex form factor
F(p_Delta^2) = Lambda^4/(Lambda^4 + (p_Delta^2 - M_Delta^2)^2), Lambda = 1.121 GeV,
on total photoproduction, all four channels.
  solid blue        this work (V16, vertex form factors, fixed width)
  blue dash-dot     the same with F_piNDelta = 1 (the V15 mode), couplings unchanged
Both curves are the Python engine (py_photoprod_variants_V16.py, curves 'base' and
'v15'), so their difference is the form factor alone; 'base' reproduces the Sherpa
V16 scan to ~1%.  Same layout and data as py_fig_photoprod_appendix_V16.py."""
import csv
import sys
from pathlib import Path
from collections import defaultdict
sys.path.insert(0, str(Path(__file__).resolve().parent))  # py_paperstyle.py sits next to this script
import py_paperstyle as ps
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

def read(path):
    with open(path) as f:
        return list(csv.DictReader(r for r in f if not r.startswith("#")))

# V16: all three variants from py_photoprod_variants_V16.py (photoprod_variants_V16.csv)
_var = read("photoprod_variants_V16.csv")
def _curve(ch, name):
    pts = sorted((float(r["Egamma"]), float(r["sigma_ub"])) for r in _var
                 if r["channel"] == ch and r["curve"] == name and float(r["sigma_ub"]) > 0)
    return [p[0] for p in pts], [p[1] for p in pts]
# grid_run = read("fig33_vecmeson_scan_grid_V13.csv")            # Fig. 33 running width Gamma_0 X_pi(W): dropped 2026-09-07, indistinguishable from fixed width at the peak
# grid_k3 = read("fig33_vecmeson_scan_grid_V13_kcube.csv")       # k^3 width at the POLE parameters: dropped 2026-09-07 (mixed prescription; one sentence in the text)

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
LS_V15 = (0, (5.0, 1.5, 1.0, 1.5))   # dash-dot: F_piNDelta = 1
LS_VEC = (0, (1.0, 1.3))   # dense dots
LS_RUN = (0, (4.0, 1.5, 1.0, 1.5))   # dash-dot: running width (Fig. 33 X_pi)
LS_K3 = (0, (6.0, 2.0))               # long dash: P-wave width
C_AMP = "#7B3FA0"           # amplitude-level FFs (purple; blue/maroon/orange are reserved for the CC1pi channels)
C_VEC = "#1B9E77"           # + omega/rho (teal green)
C_K3 = "#A0522D"            # + omega/rho, k^3 width (sienna)
C_BW = "#C62828"            # + omega/rho, k^3 width, Breit-Wigner parameters (red: must stand out on the grey data)
# STYLE DEVIATION from py_paperstyle (grey for variants): the two variants are on
# equal footing here and need to be told apart -- Shirley, 2026-09-07.

fig, axes = ps.grid22()
for ax, (ch, title, datafile) in zip(axes.flat, PANELS):
    if datafile:
        pts = defaultdict(lambda: ([], [], []))
        for r in read(datafile):
            pts[r["experiment"]][0].append(float(r["E_gamma_MeV"]) / 1e3)
            pts[r["experiment"]][1].append(float(r["sigma_exp_ub"]))
            pts[r["experiment"]][2].append(float(r["err_ub"]))
        for (code, (E, s, e)), m, c in zip(sorted(pts.items()), MARKERS, DATA_COLORS):
            ax.errorbar(E, s, yerr=e, fmt=m, ms=3.5, capsize=1.5, lw=0.8,
                        ls="none", markerfacecolor="none", color=c, zorder=2)
    ax.plot(*_curve(ch, "v15"), color=ps.C_OURS, lw=1.8, ls=LS_V15, zorder=3)
    ax.plot(*_curve(ch, "base"), color=ps.C_OURS, lw=2.2, zorder=4)
    ax.text(0.95, 0.92, title, transform=ax.transAxes, ha="right",
            va="top", fontsize=ps.FT)

axes[0, 0].set_xlim(0.14, 0.6)
axes[0, 0].set_ylim(0, 419)
h = [mlines.Line2D([], [], color=ps.C_OURS, lw=2.2, label=r"this work"),
     mlines.Line2D([], [], color=ps.C_OURS, lw=1.8, ls=LS_V15, label=r"$F_{\pi N\Delta} = 1$"),
     mlines.Line2D([], [], color="#7f7f7f", marker="o", markerfacecolor="none", ls="none",
                   ms=3.5, label=r"data (refs.\ in caption)")]
# Geometry: grid22() gives 3.885 in square panels on a 9.0 x 8.85 in figure.  Make room for the legend strip by growing the figure HEIGHT, not by
# squeezing the panels: keep the same absolute bottom margin, and set the top so
# that every panel is an exact 3.885 in square.
W0, H0 = fig.get_size_inches()                 # grid22 figure (9.0 x 8.85 in, square panels)
W_IN, H_IN = W0, H0 + 0.80                     # +0.80 in strip for the legend
PANEL = (0.98 - 0.095) * W0 / 2.05             # panel width in inches (grid22, wspace 0.05)
BOT = 0.08 * H0 / H_IN                         # same absolute bottom margin as grid22
TOP = BOT + PANEL * 2.05 / H_IN                # two panels + hspace, all square
fig.set_size_inches(W_IN, H_IN)
fig.subplots_adjust(bottom=BOT, top=TOP)
fig.legend(handles=h, fontsize=ps.FT - 2, loc="upper center", ncol=3, frameon=False,
           bbox_to_anchor=(0.5375, 0.997), columnspacing=1.6, handlelength=2.6)
for ax in axes[1, :]:
    ax.set_xlabel(r"$E_\gamma$ (GeV)", fontsize=ps.FT)
    ax.xaxis.set_label_coords(0.5, -0.10)
for ax in axes[:, 0]:
    ax.set_ylabel(r"$\sigma$ ($\mu$b)", fontsize=ps.FT)
    ax.yaxis.set_label_coords(-0.16, 0.5)

fig.savefig("/home/isaacson/Documents/Projects/NeutrinoGenerator/Achilles/sherpa3-0/build/chipt_nuisance/paper_figures/figures_appendix/photoprod_piNDelta_ff.pdf")
print("wrote /home/isaacson/Documents/Projects/NeutrinoGenerator/Achilles/sherpa3-0/build/chipt_nuisance/paper_figures/figures_appendix/photoprod_piNDelta_ff.pdf")
