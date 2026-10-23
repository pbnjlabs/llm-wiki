"""Transcribe a training video's audio with faster-whisper.

Usage: ~/.local/share/whisper-venv/bin/python scripts/transcribe.py <audio.wav> <out_dir> [model]
The audio must be a 16 kHz mono 16-bit WAV (ffmpeg -i video.mp4 -ac 1 -ar 16000 audio.wav).
Writes transcript.txt (timestamped segments) and transcript.srt to out_dir.
"""
import sys
import wave

import numpy as np
from faster_whisper import WhisperModel

audio, out = sys.argv[1], sys.argv[2]
model_name = sys.argv[3] if len(sys.argv) > 3 else "medium.en"

def ts(t, srt=False):
    h, rem = divmod(t, 3600)
    m, s = divmod(rem, 60)
    if srt:
        return f"{int(h):02d}:{int(m):02d}:{int(s):02d},{int((s % 1) * 1000):03d}"
    return f"{int(m)}:{int(s):02d}" if not h else f"{int(h)}:{int(m):02d}:{int(s):02d}"

# Read the WAV ourselves: faster-whisper's own decoder (PyAV) breaks on some av versions.
with wave.open(audio) as w:
    assert w.getframerate() == 16000 and w.getnchannels() == 1 and w.getsampwidth() == 2
    samples = np.frombuffer(w.readframes(w.getnframes()), dtype=np.int16).astype(np.float32) / 32768

model = WhisperModel(model_name, device="cpu", compute_type="int8")
segments, info = model.transcribe(samples, beam_size=5, vad_filter=True)
with open(f"{out}/transcript.txt", "w") as txt, open(f"{out}/transcript.srt", "w") as srt:
    for i, seg in enumerate(segments, 1):
        line = f"[{ts(seg.start)}] {seg.text.strip()}"
        print(line, flush=True)
        txt.write(line + "\n")
        srt.write(f"{i}\n{ts(seg.start, True)} --> {ts(seg.end, True)}\n{seg.text.strip()}\n\n")
