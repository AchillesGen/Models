#!/usr/bin/env python3
"""pin_data.py -- pi N elastic and total cross sections from the PDG compilation.

Parses the PDG's hadronic cross-section tables into one long-format CSV keyed by
(reaction, kind), with the pi-N centre-of-mass energy W computed alongside the
beam momentum, because W is what the model is a function of.

    python3 pin_data.py            ->  pin_data.csv

SOURCE.  The four files in data/pdg/ are the 2022 edition of the PDG's
`hadronic-xsections' compilation, mirrored from

    https://pdg.lbl.gov/2023/hadronic-xsections/rpp2022-<name>.dat

and kept in the repository so the pipeline runs offline.  They are fixed-format
tables; the header declares FORMAT(I5,1X,4F11.5,2F8.4,1X,2F6.1,A) and the data
begin after the line that gives the number of points.

WHY BOTH CHARGE STATES.  pi+ p is pure I = 3/2, so at the Delta it is the clean
test -- the resonance saturates it and the peak is pinned by unitarity at
8 pi / k^2.  pi- p is a 1/3 : 2/3 mixture of I = 3/2 and I = 1/2, so its
Delta peak is a third the size and it carries the I = 1/2 background the model
does NOT contain (no Roper, no D13).  Plotting both makes the omission visible
rather than hidden: the model should track pi+ p through the resonance and
undershoot pi- p away from it.

WHY BOTH TOTAL AND ELASTIC.  Below about W = 1.35 GeV the Delta is elastic and
the two data sets coincide; where they separate, inelasticity has opened and a
tree-level elastic model cannot follow the total any more.  The gap between the
two curves is therefore the honest upper bound on where the comparison means
anything.
"""
import csv
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, 'data', 'pdg')
OUT = os.path.join(HERE, 'pin_data.csv')

MPIC, MN = 0.1395704, 0.938272

FILES = [
    ('pi+p', 'total',   'pdg_pipp_total.dat'),
    ('pi+p', 'elastic', 'pdg_pipp_elastic.dat'),
    ('pi-p', 'total',   'pdg_pimp_total.dat'),
    ('pi-p', 'elastic', 'pdg_pimp_elastic.dat'),
]


def W_of_plab(plab):
    """pi-N invariant mass from the pion beam momentum on a nucleon at rest."""
    E = math.sqrt(plab ** 2 + MPIC ** 2)
    return math.sqrt(MPIC ** 2 + MN ** 2 + 2 * MN * E)


def parse(path):
    """Yield (plab, sigma_mb, stat+, stat-, sys+%, sys-%, reference)."""
    lines = open(path, errors='replace').read().splitlines()
    # the data start on the line after the one holding the point count, which is
    # the first bare integer following the masses line
    start = None
    for i, l in enumerate(lines):
        if l.strip().isdigit() and i > 5:
            start = i + 1
            break
    if start is None:
        raise SystemExit('no point count found in %s' % path)
    for l in lines[start:]:
        if not l.strip():
            continue
        f = l.split()
        if len(f) < 9 or not f[0].isdigit():
            continue
        try:
            plab = float(f[1]); sig = float(f[4])
            sp, sm = float(f[5]), float(f[6])
            yp, ym = float(f[7]), float(f[8])
        except ValueError:
            continue
        ref = ' '.join(f[9:]).strip()
        yield plab, sig, sp, sm, yp, ym, ref


def main():
    rows = []
    for react, kind, fn in FILES:
        path = os.path.join(RAW, fn)
        n = 0
        for plab, sig, sp, sm, yp, ym, ref in parse(path):
            # combine statistical and percentage systematic errors in quadrature
            ep = math.hypot(sp, 0.01 * yp * sig)
            em = math.hypot(sm, 0.01 * ym * sig)
            rows.append(dict(reaction=react, kind=kind, plab_GeV='%.5f' % plab,
                             W_GeV='%.6f' % W_of_plab(plab),
                             sigma_mb='%.5g' % sig,
                             err_hi_mb='%.5g' % ep, err_lo_mb='%.5g' % em,
                             reference=ref))
            n += 1
        print('%-5s %-8s %3d points   %s' % (react, kind, n, fn))
    rows.sort(key=lambda r: (r['reaction'], r['kind'], float(r['W_GeV'])))
    with open(OUT, 'w', newline='') as f:
        f.write('# pi N elastic and total cross sections, PDG 2022 hadronic-xsections\n')
        f.write('# https://pdg.lbl.gov/2023/hadronic-xsections/  (raw files in data/pdg/)\n')
        f.write('# W is the pi-N centre-of-mass energy computed from plab on a nucleon at rest.\n')
        f.write('# err_* combine the quoted statistical error and the percentage systematic in quadrature.\n')
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader(); w.writerows(rows)
    print('wrote %s (%d rows)' % (OUT, len(rows)))


if __name__ == '__main__':
    main()
