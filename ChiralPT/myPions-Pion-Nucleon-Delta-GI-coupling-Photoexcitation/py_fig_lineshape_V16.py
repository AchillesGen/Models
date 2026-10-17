#!/usr/bin/env python3
"""Paper Fig. A3 (figures_appendix/lineshape.pdf), model V16: line shape of the
Delta term alone in gamma p -> p pi0.
  solid blue     this work: constant Gamma = 102 MeV at the pole mass 1.209 GeV
  dashed black   the Breit-Wigner cross section, Eq. (E2), same pole and widths,
                 Gamma_Npi ~ k^3, Gamma_Ngamma ~ q^3
  dashed red     this work with that energy-dependent width in the propagator,
                 nothing else changed
All three from py_photoprod_variants_V16.py (Delta diagrams of the V16 UFO)."""
import csv, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import py_paperstyle as ps
import numpy as np
import matplotlib.lines as mlines

OUT = "/home/isaacson/Documents/Projects/NeutrinoGenerator/Achilles/sherpa3-0/build/chipt_nuisance/paper_figures/figures_appendix/lineshape.pdf"
MN, MD = 0.938272, 1.209

def read(path):
    with open(path) as f:
        return list(csv.DictReader(r for r in f if not r.startswith("#")))

var = read("photoprod_variants_V16.csv")
def curve(name):
    pts = sorted((float(r["Egamma"]), float(r["sigma_ub"])) for r in var
                 if r["channel"] == "pi0p" and r["curve"] == name and float(r["sigma_ub"]) > 0)
    return [p[0] for p in pts], [p[1] for p in pts]

fig, ax = ps.newfig()
egM = (MD ** 2 - MN ** 2) / (2 * MN)
ax.axvline(egM, color="#999999", lw=0.8, zorder=1)
ax.text(egM - 0.004, 25, r"$W = M_\Delta$", rotation=90, ha="right", va="bottom",
        color="#999999", fontsize=ps.FT - 4)
ax.plot(*curve("bw_formula"), color="k", lw=1.6, ls=(0, (3, 2)), zorder=3)
ax.plot(*curve("delta_k3"), color="#C62828", lw=2.2, ls=(0, (6, 2)), zorder=4)
ax.plot(*curve("delta_const"), color=ps.C_OURS, lw=2.2, zorder=5)
ax.set_xlim(0.14, 0.6)
ax.set_ylim(0, 580)
h = [mlines.Line2D([], [], color=ps.C_OURS, lw=2.2, label=r"$\Delta$ only, constant $\Gamma_\Delta$ (this work)"),
     mlines.Line2D([], [], color="k", lw=1.6, ls=(0, (3, 2)), label=r"unitary Breit-Wigner, $\Gamma_\Delta \propto k^3$"),
     mlines.Line2D([], [], color="#C62828", lw=2.2, ls=(0, (6, 2)), label=r"$\Delta$ only, $\Gamma_\Delta \propto k^3$")]
ax.legend(handles=h, fontsize=ps.FT - 2, loc="upper right", frameon=False,
          handlelength=2.4, labelspacing=0.3, borderaxespad=0.4)
ps.label_axes(ax, r"$E_\gamma$ (GeV)", r"$\sigma_\Delta(\gamma p \to p\pi^0)$ ($\mu$b)")
fig.savefig(OUT)
print("wrote", OUT)
