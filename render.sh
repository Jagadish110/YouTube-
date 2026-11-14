#!/usr/bin/env bash
# ./render.sh <project-dir> <output.mp4>   (checks, then renders with the installed Chrome)
set -euo pipefail
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1
export HYPERFRAMES_BROWSER_PATH="${HYPERFRAMES_BROWSER_PATH:-/usr/bin/google-chrome}"
OUT="$(realpath -m "$2")"
cd "$1"
npx -y hyperframes@0.9.45 check --json > /tmp/hf-check.json 2>/dev/null || true
python3 -c "import json;r=json.load(open('/tmp/hf-check.json'));print('check ok:',r.get('ok'))"
npx -y hyperframes@0.9.45 render -o "$OUT"
