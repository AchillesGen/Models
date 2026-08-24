#!/usr/bin/env python3
"""
anl_bnl_data.py -- the ANL and BNL bubble-chamber measurements of single-pion
production as a function of neutrino energy, extracted from a local NUISANCE
checkout into self-contained CSVs.

CHARGED CURRENT, nu_mu p -> mu- p pi+  ->  anl_bnl_cc1pip.csv

    ANL   G.M. Radecky et al., Phys. Rev. D 25, 1161 (1982)
          12-ft bubble chamber, deuterium.
    BNL   T. Kitagaki et al., Phys. Rev. D 34, 2554 (1986)
          7-ft bubble chamber, deuterium.

Both are given twice: as published, and as re-analysed by

    C. Wilkinson et al., Phys. Rev. D 90, 112017 (2014)

which re-derives the flux normalisations and largely removes the long-standing
ANL/BNL discrepancy.  The corrected sets are the ones to compare a model
against; NUISANCE itself defaults to them.

NOTHING HERE IS TYPED IN BY HAND.  The numbers are read out of NUISANCE's own
data files so that the provenance is a file path, not a memory of a paper.  Point
--nuisance at the checkout (or set NUISANCE_DATA); the resulting
anl_bnl_cc1pip.csv is self-contained, so the extraction only has to be run once.

THE FILE FORMAT IS BIN EDGES, NOT BIN CENTRES.  NUISANCE builds these histograms
with PlotUtils::GetTH1DFromFile, which does

    TH1D(name, title, npoints - 1, bins)      bins = column 0

so N rows give N-1 bins: row i is the CONTENT of the bin spanning
[col0[i], col0[i+1]], and the last row contributes only the final upper edge --
its value is written past the last bin and discarded.  Reading column 0 as an
abscissa instead (the obvious thing to do) shifts every point half a bin low and
adds a spurious zero at the end.

THE W CUT MATTERS.  ANL and BNL both publish a hadronic-invariant-mass-cut
version (W < 1.4 GeV, chosen to isolate the Delta) and an uncut one.  A model
curve has to be integrated with the same cut to be compared -- see
wprod_from_ufo.py --wmax and the Mass selector in the Sherpa card.  The
'wcut' column here says which is which.

NEUTRAL CURRENT, nu n -> nu p pi-  ->  anl_nc1pi.csv

    ANL   M. Derrick et al., Phys. Lett. 92B, 363 (1980), deuterium.

That is the ONLY neutral-current sigma(E_nu) on a free nucleon in this
checkout, and it is thin: five bins over 0.25-1.5 GeV with 21-67% errors, from
one experiment, never re-analysed the way Wilkinson et al. re-did the charged
current.  It pins the NC normalisation only weakly.  Treat the CC data as what
constrains the model and this as the consistency check -- which is the useful
role for it anyway, because the NC and CC channels share F_A and C5A, so once
the charged current is fixed the neutral current is a prediction rather than a
second fit.

Two more ANL neutral-current sets are extracted as SHAPES into
anl_nc1pi_shapes.csv: the pion momentum spectrum of nu p -> nu n pi+ (Derrick et
al., Phys. Rev. D 23, 569 (1981)) and the cos(theta*) distribution of
nu n -> nu p pi-.  These are event counts, not cross sections -- NUISANCE
carries them with no normalisation and assigns sqrt(N) errors -- so they can
only be compared shape-to-shape with a floating scale.

WHAT IS DELIBERATELY NOT HERE.  The modern neutral-current pion data in this
checkout (MiniBooNE NC1pi0 on CH2, MicroBooNE NCpi0 on argon, K2K NC1pi0,
MiniBooNE NCEL on carbon) is all on NUCLEI.  Comparing a free-nucleon chiral
model to it needs a nuclear model this calculation does not have, so those sets
are not usable as validation here.  BNL E734 nu p -> nu p elastic scattering
(Ahrens et al. 1987) would be the cleanest probe of the Z-N-N form factors
precisely because it has no Delta in it, and the Gargamelle NC1pi0 measurement
would add a second free-ish target -- neither is in this NUISANCE checkout, and
neither is typed in here from memory.  Point the script at them if you have them.

Run:
    python3 anl_bnl_data.py [--nuisance PATH]
"""

import argparse
import os
import sys

DEFAULT_NUISANCE = os.path.expanduser(
    "~/Documents/Projects/NeutrinoGenerator/Nuisance/nuisance")

# (experiment, correction, W cut, path relative to the NUISANCE data directory)
# All three charged-current single-pion channels.  The channel is carried in
# CHANNEL_OF below rather than in the tuple, to keep the CC1pi+ layout stable.
DATASETS = [
    ("ANL", "published", "1.4",
     "ANL/CC1pip_on_p/anl82-numu-cc1ppip-14Wcut.txt"),
    ("ANL", "published", "1.6",
     "ANL/CC1pip_on_p/anl82-numu-cc1ppip-16Wcut.txt"),
    ("ANL", "published", "none",
     "ANL/CC1pip_on_p/anl82-numu-cc1ppip-noWcut.txt"),
    ("ANL", "wilkinson", "1.4",
     "ANL/CC1pip_on_p/anl82corr-numu-p-to-mu-p-piplus-lowW_edges.txt"),
    ("ANL", "wilkinson", "none",
     "ANL/CC1pip_on_p/anl82corr-numu-p-to-mu-p-piplus-noW_edges.txt"),
    ("BNL", "published", "1.4",
     "BNL/CC1pip_on_p/BNL_CC1pip_on_p_W14_1986.txt"),
    ("BNL", "published", "none",
     "BNL/CC1pip_on_p/BNL_CC1pip_on_p_1986.txt"),
    ("BNL", "wilkinson", "1.4",
     "BNL/CC1pip_on_p/BNL_CC1pip_on_p_W14_1986_corr.txt"),
    ("BNL", "wilkinson", "none",
     "BNL/CC1pip_on_p/BNL_CC1pip_on_p_1986_corr.txt"),
    # ---- nu n -> mu- p pi0 ----
    ("ANL", "published", "1.4",
     "ANL/CC1pi0_on_n/anl82-numu-cc1pi0-14Wcut.txt"),
    ("ANL", "published", "none",
     "ANL/CC1pi0_on_n/anl82-numu-cc1pi0-noWcut.txt"),
    ("ANL", "wilkinson", "1.4",
     "ANL/CC1pi0_on_n/anl82corr-numu-n-to-mu-p-pi0-lowW_edges.txt"),
    ("ANL", "wilkinson", "none",
     "ANL/CC1pi0_on_n/anl82corr-numu-n-to-mu-p-pi0-noW_edges.txt"),
    ("BNL", "published", "none",
     "BNL/CC1pi0_on_n/BNL_CC1pi0_on_n_1986.txt"),
    ("BNL", "wilkinson", "none",
     "BNL/CC1pi0_on_n/BNL_CC1pi0_on_n_1986_corr.txt"),
    # ---- nu n -> mu- n pi+ ----
    ("ANL", "published", "1.4",
     "ANL/CC1pip_on_n/anl82-numu-cc1npip-14Wcut.txt"),
    ("ANL", "published", "none",
     "ANL/CC1pip_on_n/anl82-numu-cc1npip-noWcut.txt"),
    ("ANL", "wilkinson", "1.4",
     "ANL/CC1pip_on_n/anl82corr-numu-n-to-mu-n-piplus-lowW_edges.txt"),
    ("ANL", "wilkinson", "none",
     "ANL/CC1pip_on_n/anl82corr-numu-n-to-mu-n-piplus-noW_edges.txt"),
    ("BNL", "published", "none",
     "BNL/CC1pip_on_n/BNL_CC1pip_on_n_1986.txt"),
    ("BNL", "wilkinson", "none",
     "BNL/CC1pip_on_n/BNL_CC1pip_on_n_1986_corr.txt"),
]

# The channel each file belongs to, keyed by a distinctive path fragment.
# 'ppip' = nu p -> mu- p pi+ (pure I=3/2), 'ppi0' = nu n -> mu- p pi0,
# 'npip' = nu n -> mu- n pi+.
def channel_of(rel):
    if "CC1pi0" in rel or "pi0" in rel.split("/")[-1]:
        return "ppi0"
    if "_on_n" in rel or "cc1npip" in rel or "n-to-mu-n" in rel:
        return "npip"
    return "ppip"

# Neutral current, sigma(E_nu) on a free nucleon.  Same bin-edge convention.
NC_DATASETS = [
    ("ANL", "published", "none", "nu n -> nu p pi-",
     "ANL/NC1ppim/ANL_NC1ppim_Enu_xsec.csv"),
]

# Neutral current shapes: event counts, no cross-section normalisation.
NC_SHAPES = [
    ("ANL", "nu p -> nu n pi+", "p_pi", "MeV",
     "ANL/NC1npip/ANL_ppi_NC1npip_weight.csv"),
    ("ANL", "nu p -> nu n pi+", "p_pi_unweighted", "MeV",
     "ANL/NC1npip/ANL_ppi_NC1npip_unweight.csv"),
    ("ANL", "nu n -> nu p pi-", "cos_theta_star", "",
     "ANL/NC1ppim/ANL_NC1ppim_cosMuStar.csv"),
]

REFERENCES = {
    ("ANL", "published"): "Radecky et al., Phys. Rev. D 25, 1161 (1982)",
    ("BNL", "published"): "Kitagaki et al., Phys. Rev. D 34, 2554 (1986)",
    ("ANL", "wilkinson"): "Radecky 1982 re-analysed, Wilkinson et al., "
                          "Phys. Rev. D 90, 112017 (2014)",
    ("BNL", "wilkinson"): "Kitagaki 1986 re-analysed, Wilkinson et al., "
                          "Phys. Rev. D 90, 112017 (2014)",
}

NC_REFERENCES = {
    "nu n -> nu p pi-": "Derrick et al., Phys. Lett. 92B, 363 (1980)",
    "nu p -> nu n pi+": "Derrick et al., Phys. Rev. D 23, 569 (1981)",
}

CM2_TO_UB = 1.0e30      # 1 ub = 1e-30 cm^2


def read_binned(path):
    """Rows of (E_lo, E_hi, sigma_cm2, dsigma_cm2), NUISANCE's edge convention."""
    rows = []
    for line in open(path):
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        f = line.split()
        rows.append((float(f[0]), float(f[1]), float(f[2]) if len(f) > 2 else 0.0))
    out = []
    for i in range(len(rows) - 1):        # last row is the final edge only
        out.append((rows[i][0], rows[i + 1][0], rows[i][1], rows[i][2]))
    return out


def collect_nc(data):
    """Neutral-current sigma(E_nu), same edge convention as the CC files."""
    rows, missing = [], []
    for exp, corr, wcut, channel, rel in NC_DATASETS:
        path = os.path.join(data, rel)
        if not os.path.exists(path):
            missing.append(rel)
            continue
        for elo, ehi, xs, dxs in read_binned(path):
            rows.append(dict(experiment=exp, correction=corr, wcut=wcut,
                             channel=channel,
                             E_lo=elo, E_hi=ehi, E_mid=0.5 * (elo + ehi),
                             sigma_ub=xs * CM2_TO_UB, dsigma_ub=dxs * CM2_TO_UB,
                             sigma_cm2=xs, dsigma_cm2=dxs, source=rel))
    return rows, missing


def collect_nc_shapes(data):
    """Event-count distributions: two columns, no cross-section normalisation.

    NUISANCE reads these with the same edge convention and, seeing no third
    column, assigns sqrt(N) errors.  That is reproduced here so the numbers
    match what NUISANCE would plot, but they stay flagged as counts: the only
    honest comparison is shape-to-shape with a free scale.
    """
    rows, missing = [], []
    for exp, channel, observable, unit, rel in NC_SHAPES:
        path = os.path.join(data, rel)
        if not os.path.exists(path):
            missing.append(rel)
            continue
        for lo, hi, val, err in read_binned(path):
            rows.append(dict(experiment=exp, channel=channel,
                             observable=observable, unit=unit,
                             x_lo=lo, x_hi=hi, x_mid=0.5 * (lo + hi),
                             counts=val,
                             dcounts=err if err else (val ** 0.5 if val > 0 else 0.0),
                             source=rel))
    return rows, missing


def collect(nuisance):
    data = os.path.join(nuisance, "data")
    if not os.path.isdir(data):
        raise SystemExit(
            "no NUISANCE data directory at %s\n"
            "pass --nuisance /path/to/nuisance or set NUISANCE_DATA" % data)
    rows, missing = [], []
    for exp, corr, wcut, rel in DATASETS:
        path = os.path.join(data, rel)
        if not os.path.exists(path):
            missing.append(rel)
            continue
        for elo, ehi, xs, dxs in read_binned(path):
            rows.append(dict(experiment=exp, correction=corr, wcut=wcut,
                             channel=channel_of(rel),
                             E_lo=elo, E_hi=ehi, E_mid=0.5 * (elo + ehi),
                             sigma_ub=xs * CM2_TO_UB, dsigma_ub=dxs * CM2_TO_UB,
                             sigma_cm2=xs, dsigma_cm2=dxs, source=rel))
    if missing:
        print("WARNING: not found in this checkout:", *missing, sep="\n  ")
    return rows


def write_csv(rows, out, nuisance):
    cols = ["experiment", "channel", "correction", "wcut", "E_lo", "E_hi", "E_mid",
            "sigma_ub", "dsigma_ub", "sigma_cm2", "dsigma_cm2", "source"]
    with open(out, "w") as f:
        f.write("# sigma(nu_mu p -> mu- p pi+) vs neutrino energy.\n")
        for k, v in sorted(REFERENCES.items()):
            f.write("#   %-4s %-10s %s\n" % (k[0], k[1], v))
        f.write("# Extracted by anl_bnl_data.py from %s\n" % nuisance)
        f.write("# E_lo/E_hi are the published bin edges in GeV; the quoted\n"
                "# cross section is the flux-averaged value over that bin, so a\n"
                "# model should be compared to it at E_mid (or averaged over the\n"
                "# bin).  wcut is the hadronic invariant mass cut in GeV.\n")
        f.write(",".join(cols) + "\n")
        for r in rows:
            f.write(",".join(
                ("%.6g" % r[c]) if isinstance(r[c], float) else str(r[c])
                for c in cols) + "\n")


def write_simple(rows, cols, out, header):
    with open(out, "w") as f:
        f.write(header)
        f.write(",".join(cols) + "\n")
        for r in rows:
            f.write(",".join(
                ("%.6g" % r[c]) if isinstance(r[c], float) else str(r[c])
                for c in cols) + "\n")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--nuisance",
                    default=os.environ.get("NUISANCE_DATA", DEFAULT_NUISANCE))
    ap.add_argument("--out", default="anl_bnl_cc1pip.csv")
    ap.add_argument("--nc-out", default="anl_nc1pi.csv")
    ap.add_argument("--nc-shapes-out", default="anl_nc1pi_shapes.csv")
    a = ap.parse_args()

    rows = collect(a.nuisance)
    write_csv(rows, a.out, a.nuisance)
    print("wrote %s  (%d points)" % (a.out, len(rows)))
    for exp, corr, wcut, rel in DATASETS:
        ch = channel_of(rel)
        sel = [r for r in rows if (r["experiment"], r["correction"], r["wcut"],
                                   r["channel"]) == (exp, corr, wcut, ch)]
        if sel:
            print("  %-5s %-4s %-10s W<%-5s %2d pts, E = %.2f - %.2f GeV"
                  % (ch, exp, corr, wcut, len(sel), sel[0]["E_lo"], sel[-1]["E_hi"]))

    data = os.path.join(a.nuisance, "data")
    nc, miss = collect_nc(data)
    if nc:
        write_simple(nc, ["experiment", "channel", "correction", "wcut",
                          "E_lo", "E_hi", "E_mid", "sigma_ub", "dsigma_ub",
                          "sigma_cm2", "dsigma_cm2", "source"],
                     a.nc_out,
                     "# Neutral-current single-pion production on a free nucleon.\n"
                     + "".join("#   %-18s %s\n" % (k, v)
                               for k, v in sorted(NC_REFERENCES.items()))
                     + "# Extracted by anl_bnl_data.py from %s\n" % a.nuisance
                     + "# E_lo/E_hi are published bin edges in GeV; there is no\n"
                       "# flux re-analysis for this set and no W cut variant.\n")
        print("\nwrote %s  (%d points)" % (a.nc_out, len(nc)))
        for r in nc:
            print("  %-4s %-16s E = %.2f - %.2f GeV  %9.3g +- %-9.3g cm^2 (%2.0f%%)"
                  % (r["experiment"], r["channel"], r["E_lo"], r["E_hi"],
                     r["sigma_cm2"], r["dsigma_cm2"],
                     100 * r["dsigma_cm2"] / r["sigma_cm2"] if r["sigma_cm2"] else 0))

    sh, miss2 = collect_nc_shapes(data)
    if sh:
        write_simple(sh, ["experiment", "channel", "observable", "unit",
                          "x_lo", "x_hi", "x_mid", "counts", "dcounts", "source"],
                     a.nc_shapes_out,
                     "# Neutral-current SHAPES: event counts, NOT cross sections.\n"
                     "# No normalisation is carried with them, so compare shape to\n"
                     "# shape with a floating scale.  Errors are sqrt(N), which is\n"
                     "# what NUISANCE assumes for a two-column file.\n"
                     + "# Extracted by anl_bnl_data.py from %s\n" % a.nuisance)
        print("\nwrote %s  (%d bins)" % (a.nc_shapes_out, len(sh)))
        for exp, channel, obs, unit, rel in NC_SHAPES:
            n = len([r for r in sh if r["observable"] == obs
                     and r["channel"] == channel])
            if n:
                print("  %-4s %-16s %-16s %2d bins" % (exp, channel, obs, n))
    for m in miss + miss2:
        print("  (not in this checkout: %s)" % m)


if __name__ == "__main__":
    main()
