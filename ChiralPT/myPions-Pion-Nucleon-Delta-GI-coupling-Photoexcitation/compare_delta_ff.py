#!/usr/bin/env python3
"""
compare_delta_ff.py -- does the Delta form factor built into ChiPT_UFO_DeltaFF
reproduce the Fig. 33 prescription?

Runs fig33_from_ufo.py's machinery over both UFOs and four schemes:

  reference   ChiPT_UFO          sqrt(X_pi(s,u)) applied at AMPLITUDE level,
                                 running width          <- the Fig. 33 recipe
  ff1         ChiPT_UFO_DeltaFF  every form factor forced to 1, amplitude-level
                                 sqrt(X) as above       <- regression: must equal
                                                           `reference` exactly
  vertexrun   ChiPT_UFO_DeltaFF  FpiNDelta = sqrt(X_pi(p_Delta^2)) INSIDE the
                                 vertex, running width
  vertexfix   ChiPT_UFO_DeltaFF  same, fixed width      <- what Sherpa/Achilles
                                                           computes today
  none        ChiPT_UFO_DeltaFF  FpiNDelta = 1, fixed width  <- no Delta FF

`ff1` is the check that the new UFO changed nothing it should not have.
`vertexrun` is the check of the physics claim: it must land within a few percent
of `reference`, the difference being the u-channel Delta that a vertex-local
form factor cannot damp (it damps it to zero instead, because X_pi(u) = 0
throughout the physical region).

Run:  python3 compare_delta_ff.py
"""

import numpy as np
import fig33_from_ufo as F

KP, KN = 1.792847, -1.913043
NUCFF = {'F1p': lambda q2: 1.0, 'F1n': lambda q2: 0.0,
         'F2p': lambda q2: KP, 'F2n': lambda q2: KN}


def deltaff(ns, on):
    """Form factor callables for the CHIPT_FF=Delta build."""
    Xpi = F.make_Xpi(ns['MNucleon'], ns['MPi0'], ns['MDelta'])
    d = dict(NUCFF)
    d['FpiNDelta'] = (lambda s: np.sqrt(Xpi(s.real if hasattr(s, 'real') else s))) \
        if on else (lambda s: 1.0)
    for nm in ('FgNDeltaPG1', 'FgNDeltaPG2', 'FgNDeltaNG1', 'FgNDeltaNG2'):
        d[nm] = lambda q2: 1.0
    return d


def main():
    Pa, Va = F.load_ufo('ChiPT_UFO')
    Pb, Vb = F.load_ufo('ChiPT_UFO_DeltaFF')
    na, nb = F.parameter_namespace(Pa), F.parameter_namespace(Pb)

    base = dict(born=True, delta=True, ff=True)
    schemes = [
        ('reference', Va, na, NUCFF,               dict(base, edw=True)),
        ('ff1',       Vb, nb, deltaff(nb, False),  dict(base, edw=True)),
        ('vertexrun', Vb, nb, deltaff(nb, True),   dict(base, edw=True, ffD=False)),
        ('vertexfix', Vb, nb, deltaff(nb, True),   dict(base, edw=False)),
        ('none',      Vb, nb, deltaff(nb, False),  dict(base, edw=False)),
    ]

    MN, mpi = na['MNucleon'], na['MPi0']
    Ethr = ((MN + mpi) ** 2 - MN ** 2) / (2 * MN)
    egs = [Ethr + 0.002] + [round(0.16 + 0.02 * i, 4) for i in range(43)]

    out = {}
    for name, V, ns, ff0, opt in schemes:
        for ch in F.CHANNELS:
            sig = [F.sigma_tot(ch, np.sqrt(MN ** 2 + 2 * MN * eg), V, ns, ff0, opt).real
                   for eg in egs]
            out[(name, ch)] = np.array(sig)
        print("  %s done" % name, flush=True)

    with open('compare_delta_ff.csv', 'w') as f:
        f.write("scheme,channel,Eg,sigma_ub\n")
        for (name, ch), sig in out.items():
            for eg, s in zip(egs, sig):
                f.write("%s,%s,%.5f,%.6f\n" % (name, ch, eg, s))

    def at(sig, e):
        return sig[int(np.argmin([abs(x - e) for x in egs]))]

    print("\nsigma_tot (mub), Born + Delta.  ratio to `reference` in brackets")
    print("%-6s %-10s %18s %18s %18s" % ("chan", "scheme", "peak", "0.60 GeV", "1.00 GeV"))
    for ch in F.CHANNELS:
        ref = out[('reference', ch)]
        for name, *_ in schemes:
            sig = out[(name, ch)]
            cols = [(max(sig), max(ref)), (at(sig, 0.60), at(ref, 0.60)),
                    (at(sig, 1.00), at(ref, 1.00))]
            print("%-6s %-10s " % (ch, name)
                  + " ".join("%10.2f [%5.3f]" % (v, v / r) for v, r in cols))
        print()

    d = max(abs(out[('ff1', ch)] / out[('reference', ch)] - 1).max() for ch in F.CHANNELS)
    print("regression  max |ff1/reference - 1| = %.2e  %s"
          % (d, "OK" if d < 1e-10 else "<-- the new UFO is NOT equivalent at FF=1"))
    print("wrote compare_delta_ff.csv")


if __name__ == '__main__':
    main()
