#!/usr/bin/env python3
"""vm_width_table.py -- electron 1pi responses with and without the rho/omega
exchange (vecmeson.py), at the fixed pole width and with the running width.

Writes, per channel and (W, Q^2), S_T and S_L (as eprod_from_ufo.responses) for

    pole_novec   V16 as generated (fixed width, no vector mesons) -- the baseline
    pole_vec     + rho/omega exchange
    bw_novec     + PDG BW parameters and the HNV k^3 running width
    bw_vec       both

and, from them, two tables in the eprod_width format that running_width.EFactor
reads (ST_pole/SL_pole = baseline, ST_bw/SL_bw = variant):

    <stem>_vm.csv      vector mesons only
    <stem>_rwvm.csv    running width + vector mesons

Run:  python3 vm_width_table.py --channels ppi0 --out vmparts/ppi0  [--vmff monopole]
"""
import argparse, csv, time
import numpy as np
import eprod_from_ufo as E

ap = argparse.ArgumentParser()
ap.add_argument('--ufo', default='ChiPT_UFO_V16')
ap.add_argument('--channels', default='ppi0,npip,nnpi0,ppim')
ap.add_argument('--W', default='1.08:1.80:0.01')
ap.add_argument('--Q2', default='0,0.05,0.1,0.15,0.2,0.3,0.4,0.55,0.7,0.85,1.0')
ap.add_argument('--nth', type=int, default=16)
ap.add_argument('--vmff', default='monopole')
ap.add_argument('--out', required=True)
a = ap.parse_args()
S = {p: E.setup(a.ufo, p) for p in ('pole', 'bw')}
vec = {'vmff': a.vmff}
rows, t0 = [], time.time()
for ch in a.channels.split(','):
    for Q2 in E._grid(a.Q2):
        for Wh in E._grid(a.W):
            r = dict(channel=ch, W=Wh, Q2=Q2)
            for p in ('pole', 'bw'):
                for tag, v in (('novec', None), ('vec', vec)):
                    t, l, _ = E.responses(ch, Wh, Q2, S[p], a.nth, False, vec=v)
                    r[f'ST_{p}_{tag}'], r[f'SL_{p}_{tag}'] = t, l
            rows.append(r)
        print(f"{ch} Q2={Q2:.2f} done [{time.time()-t0:.0f}s]", flush=True)
hdr = "# vm_width_table.py, UFO %s, vmff %s\n" % (a.ufo, a.vmff)
with open(a.out + '_all.csv', 'w', newline='') as f:
    f.write(hdr); w = csv.DictWriter(f, fieldnames=list(rows[0])); w.writeheader(); w.writerows(rows)
for name, var in (('vm', 'pole_vec'), ('rwvm', 'bw_vec')):
    with open(f'{a.out}_{name}.csv', 'w', newline='') as f:
        f.write(hdr.rstrip() + f"; ST_pole/SL_pole = pole_novec, ST_bw/SL_bw = {var}\n")
        w = csv.writer(f); w.writerow(['channel', 'W', 'Q2', 'ST_pole', 'SL_pole', 'ST_bw', 'SL_bw'])
        for r in rows:
            w.writerow([r['channel'], r['W'], r['Q2'], r['ST_pole_novec'], r['SL_pole_novec'],
                        r[f'ST_{var}'], r[f'SL_{var}']])
print("wrote", a.out + "_{all,vm,rwvm}.csv")
