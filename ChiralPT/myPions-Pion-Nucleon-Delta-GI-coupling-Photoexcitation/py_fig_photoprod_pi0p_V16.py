#!/usr/bin/env python3
"""Paper Fig. 2 (figures/photoprod_pi0p.pdf), model V16: gamma p -> p pi0 with
the modifications of the text applied one after another.
  solid blue        this work (Sherpa scan, ChiPT_UFO_V16)
  green dotted      this work + omega/rho exchange (ELA couplings)
  red long dash     + Breit-Wigner M, Gamma_0 and Gamma ~ k^3, h_D, G1, G2 re-derived
The amplitude-level-FF alternative is no longer drawn (still in the CSV as
'ampff'); the piNDelta form-factor comparison is its own appendix figure,
py_fig_photoprod_piNDff_V16.py.
(2026-10-15: omega/rho and Breit-Wigner now build on the vertex-FF model, not on
the amplitude-level one.)
Variants from py_photoprod_variants_V16.py; same colours and data as the
appendix figure (py_fig_photoprod_appendix_V16.py)."""
import csv, sys
from pathlib import Path
from collections import defaultdict
sys.path.insert(0, str(Path(__file__).resolve().parent))
import py_paperstyle as ps
import matplotlib.lines as mlines

OUT = "/home/isaacson/Documents/Projects/NeutrinoGenerator/Achilles/sherpa3-0/build/chipt_nuisance/paper_figures/figures/photoprod_pi0p.pdf"

def read(path):
    with open(path) as f:
        return list(csv.DictReader(r for r in f if not r.startswith("#")))

var = read("photoprod_variants_V16.csv")
scan = read("scan_results.csv")
def curve(name):
    pts = sorted((float(r["Egamma"]), float(r["sigma_ub"])) for r in var
                 if r["channel"] == "pi0p" and r["curve"] == name and float(r["sigma_ub"]) > 0)
    return [p[0] for p in pts], [p[1] for p in pts]

MARKERS = ["o", "s", "^", "v", "D", "p", "*", "<", ">", "h", "X", "d"]
DATA_COLORS = ["#4d4d4d", "#7f7f7f", "#9e9e9e", "#5d5d5d", "#8f8f8f", "#6f6f6f", "#a8a8a8",
               "#606060", "#909090", "#787878", "#525252", "#a0a0a0"]
LS_VEC, LS_K3 = (0, (1.0, 1.3)), (0, (6.0, 2.0))
LS_V15 = (0, (4.0, 1.5, 1.0, 1.5))
C_AMP, C_VEC, C_BW = "#7B3FA0", "#1B9E77", "#C62828"   # as in the appendix figure

fig, ax = ps.newfig()
pts = defaultdict(lambda: ([], [], []))
for r in read("said_gp_ppi0_SGT.csv"):
    pts[r["experiment"]][0].append(float(r["E_gamma_MeV"]) / 1e3)
    pts[r["experiment"]][1].append(float(r["sigma_exp_ub"]))
    pts[r["experiment"]][2].append(float(r["err_ub"]))
for (code, (E, s, e)), m, c in zip(sorted(pts.items()), MARKERS, DATA_COLORS):
    ax.errorbar(E, s, yerr=e, fmt=m, ms=3.5, capsize=1.5, lw=0.8, ls="none",
                markerfacecolor="none", color=c, zorder=2)
ax.plot(*curve("vec"), color=C_VEC, lw=2.4, ls=LS_VEC, zorder=3)
ax.plot(*curve("bw"), color=C_BW, lw=2.4, ls=LS_K3, zorder=5)
sh = sorted((float(r["Egamma_corr"]), float(r["sigma_ub"])) for r in scan
            if r["channel"] == "pi0p" and r["model"] == "ChiPT_UFO_V16")
ax.plot([p[0] for p in sh], [p[1] for p in sh], color=ps.C_OURS, lw=2.2, zorder=4)
ax.set_xlim(0.14, 0.6)
ax.set_ylim(0, 580)
h = [mlines.Line2D([], [], color=ps.C_OURS, lw=2.2, label=r"this work"),
     mlines.Line2D([], [], color=C_VEC, lw=2.4, ls=LS_VEC, label=r"$+\ \omega,\rho$ exchange"),
     mlines.Line2D([], [], color=C_BW, lw=2.4, ls=LS_K3,
                   label=r"$+$ Breit-Wigner $M_\Delta,\Gamma_0$, $\Gamma_\Delta \propto k^3$")]
ax.legend(handles=h, fontsize=ps.FT - 2, loc="upper right", frameon=False,
          handlelength=2.6, labelspacing=0.3, borderaxespad=0.4)
ps.label_axes(ax, r"$E_\gamma$ (GeV)", r"$\sigma(\gamma p \to p\pi^0)$ ($\mu$b)")
fig.savefig(OUT)
print("wrote", OUT)
