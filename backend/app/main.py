import os
from pathlib import Path
from uuid import uuid4

from fastapi import FastAPI, File, HTTPException, UploadFile

UPLOAD_DIR = Path(os.getenv("UPLOAD_DIR", "./uploads"))
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)
MAX_BYTES = 2 * 1024 * 1024 * 1024

app = FastAPI(title="AutoStream API", version="0.1.0")


@app.get("/health")
def health():
    return {"status": "ok", "service": "autostream-api"}


@app.post("/v1/videos")
async def upload_video(file: UploadFile = File(...)):
    allowed = {".mp4", ".mkv", ".mov", ".webm"}
    suffix = Path(file.filename or "").suffix.lower()
    if suffix not in allowed:
        raise HTTPException(400, "Unsupported video extension")

    video_id = str(uuid4())
    target = UPLOAD_DIR / f"{video_id}{suffix}"
    size = 0
    try:
        with target.open("wb") as out:
            while chunk := await file.read(1024 * 1024):
                size += len(chunk)
                if size > MAX_BYTES:
                    raise HTTPException(413, "Video exceeds 2 GB development limit")
                out.write(chunk)
    except Exception:
        target.unlink(missing_ok=True)
        raise
    finally:
        await file.close()

    return {
        "video_id": video_id,
        "filename": file.filename,
        "bytes": size,
        "status": "uploaded",
        "message": "Upload saved to development storage. Streaming jobs are not enabled yet."
    }
