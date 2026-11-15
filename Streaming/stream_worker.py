"""Illustrative FFmpeg publisher.

Call only from a trusted worker after authorization and secure credential lookup.
Do not expose ingest_url as an unauthenticated public API parameter.
"""
import subprocess
from pathlib import Path


def stream_file(video_path: Path, ingest_url: str):
    if not video_path.is_file():
        raise FileNotFoundError(video_path)
    cmd = [
        "ffmpeg", "-re", "-i", str(video_path),
        "-c:v", "libx264", "-preset", "veryfast",
        "-b:v", "4500k", "-maxrate", "4500k", "-bufsize", "9000k",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "128k",
        "-f", "flv", ingest_url,
    ]
    return subprocess.Popen(cmd, shell=False)
