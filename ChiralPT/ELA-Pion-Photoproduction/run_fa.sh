#!/usr/bin/env bash
# Run the ELA UFO export inside a cgroup with a hard memory ceiling.
#
# Without the ceiling a runaway WolframKernel takes the whole machine with it:
# on 2026-07-27 the export exhausted 30 GB and the OOM-killer reaped desktop
# processes (dbus-broker, xdg-document-portal, browser tabs) before it got to
# the kernel.  MemoryMax makes the cgroup the thing that dies instead.
#
# Usage: ./run_ufo.sh [MemoryMax]        (default 12G)

set -euo pipefail

MEM="${1:-12G}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

exec systemd-run --user --scope \
    --unit="ela-fa-$$" \
    -p MemoryMax="$MEM" \
    -p MemorySwapMax=0 \
    --setenv=HOME="$HOME" \
    -- "$HOME/.local/bin/WolframKernel" -noprompt -run "Get[\"$HERE/run_fa.m\"]"
