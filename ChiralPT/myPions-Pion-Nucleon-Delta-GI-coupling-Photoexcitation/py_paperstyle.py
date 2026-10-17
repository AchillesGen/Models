"""Shared plotting style for the ChiPT paper figures.

*** FROZEN 2026-08-14 (Shirley) — do not change sizes/colors without group sign-off. ***
*** 2026-09-07 (Shirley): grid22 height 8.55 -> 8.85 in so the four panels are exact squares. ***
Inclusion rules: single panels at \columnwidth; 2x2 grid at 0.9\linewidth.
Hierarchy: panel titles & axis labels = FT; legend & ticks = FT-2.
Based on Shirley's default single-panel style (py_plot_full.py):
LaTeX text, Palatino serif, ft=16, 1:1 frame aspect, fixed label offsets,
tick length 6/4 width 1. Import and use newfig()/grid22()/style_ax().

Semantic conventions (keep identical across ALL paper figures):
  - experimental data: small markers, muted colors, one marker shape per experiment
  - our automated result (Sherpa, vertex-level FFs): C_OURS (red), solid, thick — the ONLY colored element
  - reference prescription (amplitude-level FFs, running width): grey dashed, thinner
  - variants (no FF, +vector mesons, ...): grey dotted/dash-dot
  - data: open grey markers; cite original experiments in caption (not SAID)
"""
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['text.usetex'] = True
rcParams['font.family'] = "serif"
rcParams['font.serif'] = "Palatino"

FT = 15                    # base font size (labels); ticks use FT-2 (Palatino runs visually large; 14 ~ CM 16)
C_OURS = "#0057B7"         # this work (automated) — the ONE colored line; everything else grey
C_REF = "#999999"          # reference prescriptions — grey

def style_ax(ax, ft=FT):
    """Shirley's tick conventions."""
    ax.tick_params('both', length=6, width=1, which='major', labelsize=ft - 2)
    ax.tick_params('both', length=4, width=1, which='minor')

def newfig(ft=FT):
    """Single-panel figure, frame aspect exactly 1:1 (original default)."""
    fig = plt.figure(figsize=(5, 4.75))
    ax = fig.add_axes([0.172, 0.137, 0.785, 0.826316])
    style_ax(ax, ft)
    return fig, ax

def label_axes(ax, xlab, ylab, ft=FT):
    """Fixed label offsets from the original style."""
    ax.set_xlabel(xlab, fontsize=ft)
    ax.set_ylabel(ylab, fontsize=ft)
    ax.xaxis.set_label_coords(0.5, -0.10)
    ax.yaxis.set_label_coords(-0.14, 0.5)

def grid22(ft=FT):
    """2x2 grid with shared axes; each panel keeps the 1:1 frame feel."""
    # 9.0 x 8.85 in: with the margins below every panel is an exact 3.885 in square
    # (was 8.55 in, i.e. 3.885 x 3.753, until 2026-09-07 -- Shirley: panels 100% square).
    fig, axes = plt.subplots(2, 2, figsize=(9.0, 8.85), sharex=True, sharey=True)
    fig.subplots_adjust(left=0.095, right=0.98, bottom=0.08, top=0.98,
                        wspace=0.05, hspace=0.05)
    for ax in axes.flat:
        style_ax(ax, ft)
    return fig, axes
