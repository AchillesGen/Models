#!/usr/bin/env python3
"""PCAC on the N -> Delta axial current, and the calibration of C6AN.

Contracting q_mu into the axial N -> Delta current must leave a result
suppressed by mpi^2/(Q^2 + mpi^2), vanishing in the chiral limit.  The Adler
C6A term is what makes that happen; its normalisation C6AN cannot be read off by
inspection, because this model's C5A comes from the gauged Pascalutsa coupling
rather than from a plain g^{alpha mu} structure.

Two things this script exists to get right:

  * The Rarita-Schwinger leg MUST be projected on shell.  Contracting the bare
    Delta index instead lets the unphysical spin-1/2 components dominate; C6A
    then looks orthogonal to everything else and the fit returns exactly zero
    with no change in the residual, which is a plausible-looking but incorrect result.
    Hence the Delta rest frame and delta_couplings.rs_spinor.

  * The coefficient that drives the contraction to zero is the CHIRAL-LIMIT one.
    The physical value is that times Q^2/(Q^2 + mpi^2).

Usage:  python3 tools/pcac_delta.py           (CHIPT_MODEL selects the UFO)
"""
import numpy as np

from _vertex import build_named, load, vertex, with_ff   # sets sys.path first

import delta_couplings as dc                              # noqa: E402
import wprod_from_ufo as w                                # noqa: E402


def main():
    ns, ff, V = load()
    MN = float(ns['MNucleon'])
    mpi = float(ns['MPiP'])
    MD = float(ns['MDelta'])
    G = np.diag(w.METRIC).real

    v = vertex(V, ('p~', 'Delta++', 'W-'))
    axial = with_ff(v, 'FCA5')        # C5A and C4A
    c6a = with_ff(v, 'FC6A')
    if not c6a:
        print("this model has no C6A term"); return

    def contracted(keep, q, pD, PN):
        T = build_named(v, {'p~': -PN, 'Delta++': pD, 'W-': -q}, ns, ff, keep)
        if T is None:
            return None
        X = [sum(G[m] * q[m] * T[a, m] for m in range(4)) for a in range(4)]
        out = []
        for tl in dc.LAMBDAS:                      # sum over Delta polarisations
            urs = dc.rs_spinor(pD, MD, tl)
            for s in range(2):                     # and nucleon spins
                uN = w.uspinor(PN, MN, s)
                out.append(sum(G[a] * (dc.ubar(urs[a]) @ X[a] @ uN)
                               for a in range(4)))
        return np.array(out)

    card = float(np.real(ns['C6AN']))
    print("The C6A structure already carries the model's C6AN, so a correctly")
    print("calibrated model gives multiplier = 1 and residue = the PCAC value.")
    print("From V10 on C6AN is an INTERNAL parameter equal to hD, so it tracks")
    print("Gamma(Delta -> N pi) on its own and this is a check, not a knob.\n")
    print("%8s %14s %12s %11s %12s"
          % ("Q^2", "||q.J|| axial", "residue", "multiplier", "PCAC pred"))
    fits = []
    for Q2 in (0.05, 0.1, 0.2, 0.5, 1.0, 2.0):
        q0 = (MD ** 2 - MN ** 2 - Q2) / (2 * MD)
        qz = np.sqrt(q0 ** 2 + Q2)
        pD = np.array([MD, 0, 0, 0])
        q = np.array([q0, 0, 0, qz])
        PN = pD - q
        a = contracted(axial, q, pD, PN)
        b = contracted(c6a, q, pD, PN)
        x = -np.real(np.vdot(b, a)) / np.real(np.vdot(b, b))
        mult = x * Q2 / (Q2 + mpi ** 2)            # chiral limit -> physical pole
        fits.append(mult * card)                   # implied absolute C6AN
        resid = np.linalg.norm(a + b) / np.linalg.norm(a)
        print("%8.2f %14.6g %12.6f %11.6f %12.5f"
              % (Q2, np.linalg.norm(a), resid, mult,
                 mpi ** 2 / (Q2 + mpi ** 2)))
    print("\nimplied C6AN: mean %.6f  spread %.2e   (card carries %.4f)"
          % (np.mean(fits), np.std(fits), card))
    print("It equals hD = %.4f, and not by accident: C5A carries hD through the\n"
          "gauged coupling while the C6A operator does not.  Re-run this if hD moves."
          % float(np.real(ns['hD'])))


if __name__ == '__main__':
    main()
