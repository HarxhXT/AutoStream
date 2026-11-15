"""Worker placeholder.

Production version should consume authenticated jobs from a durable queue,
load media from private object storage, retrieve encrypted destination credentials,
and launch an isolated FFmpeg process. Never accept shell fragments or arbitrary
ingest URLs directly from an unauthenticated client.
"""
import time

if __name__ == "__main__":
    print("AutoStream worker scaffold is running; no queue is configured.")
    while True:
        time.sleep(60)
