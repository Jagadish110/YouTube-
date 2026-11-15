# Scheduled pipeline test: result

- **Run:** Sunday 15 November 2026, 05:30 to 05:33 UTC (11:00 to 11:03 IST)
- **Mode:** scheduled cloud session, unattended, no human listening
- **Overall:** PASS, every step worked end to end

## Steps

| Step | Result | Time |
|---|---|---|
| Repo with push access | PASS, already attached and cloned at `main` (6f8bef1) | n/a |
| `./setup.sh` | PASS (exit 0, printed `setup ok`) | 25 s |
| Kokoro model download from GitHub | PASS: `kokoro-v1.0.onnx` 325.5 MB, `voices-v1.0.bin` 28.2 MB | included above |
| HyperFrames CLI 0.9.45 | PASS (`--version` → 0.9.45), Chrome at `/usr/bin/google-chrome`, ffmpeg present | included above |
| Voiceover (`tools/voiceover.py`, voice `am_eric`) | PASS: 3 lines, 13.8 s of audio | 9 s |
| `build.py` (3 `sl.Scene`s) | PASS: intro 0.00 to 5.22, steps 5.22 to 10.04, works 10.04 to 14.20 | under 1 s |
| `hyperframes check` | PASS (`ok: true`, 0 errors, 0 warnings) | in render time |
| `./render.sh` | PASS | 29 s wall clock (CLI reported 20.7 s render) |
| Snapshot contact sheet | PASS: text visible, no overlaps, nothing off screen | about 15 s |
| Supabase read-only check | PASS, reachable | n/a |

## Output

- File: `videos/test-run/output/test-run.mp4`
- Duration: **14.2 s**
- Size: **733,407 bytes (716 KB)**
- Streams: H.264 1920x1080 video, AAC audio
- Contact sheet: `videos/test-run/contact-sheet.jpg` (frames at 2.5, 4.8, 8.5, 9.8, 12.8, 13.95 s)

## Notes and warnings (nothing failed)

- `hyperframes check` gave one info-level finding (not an error): `container_overflow` on `#works-b`
  at 11.83 s, "Element extends outside a clipping layout container." That is the full-width
  headline box during its scale 1.25 → 1 "pop" entrance. The text itself stays inside the frame
  (confirmed on the contact sheet).
- The renderer fell back to screenshot capture: "Screenshot capture (slower): BeginFrame did not run.
  Needs chrome-headless-shell and no --resolution upscale." Fine at this length. For a 4-minute
  video, expect the roughly 8-minute render noted in CLAUDE.md.
- The CLI says a newer version exists ("This project pins hyperframes@0.9.45 (latest 0.9.52)").
  It was not upgraded, because CLAUDE.md pins 0.9.45.
- pip printed its usual "Running pip as the 'root' user" warning. It does no harm.
- Nobody in the pipeline can hear audio. The voiceover still needs a human listen.

## Supabase

Reachable through the connector (read-only `list_projects`; nothing was created, changed or deleted).
Projects: **Distaura**, **agency**, **readyus**.
