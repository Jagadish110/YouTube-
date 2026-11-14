#!/usr/bin/env bash
# One-time setup per fresh session. Everything comes from PyPI, npm and GitHub.
set -euo pipefail
cd "$(dirname "$0")"
pip install --break-system-packages -q kokoro-onnx soundfile numpy
mkdir -p models
for f in kokoro-v1.0.onnx voices-v1.0.bin; do
  [ -s "models/$f" ] || curl -sSL -o "models/$f" "https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/$f"
done
which ffmpeg >/dev/null || { echo "ffmpeg missing"; exit 1; }
export HYPERFRAMES_NO_TELEMETRY=1 DO_NOT_TRACK=1
npx -y hyperframes@0.9.45 --version >/dev/null 2>&1 || true
echo "setup ok"
