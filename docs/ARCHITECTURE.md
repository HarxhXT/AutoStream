# Architecture

1. Android authenticates and requests a resumable upload session.
2. Video is uploaded to private object storage.
3. User selects Kick or YouTube destination.
4. Backend validates destination ownership and retrieves encrypted credentials.
5. Backend creates a durable stream job.
6. Worker fetches media and runs FFmpeg in real-time mode (`-re`).
7. Worker publishes to RTMPS and reports status/health.
8. User can stop the job; worker terminates FFmpeg and cleans temporary media.

## Required before public launch
- Authentication and per-user authorization
- Private object storage and resumable multipart uploads
- Database and durable queue
- Encrypted secrets storage, key rotation, and redacted logs
- Worker isolation, quotas, rate limits, timeouts
- HTTPS, audit logs, retention/deletion controls
- Retry policy and duplicate-job protection
- YouTube OAuth consent and refresh-token handling
- Tests for invalid keys, disconnects, unsupported codecs, and worker crashes

## Free-tier limitation
A free API host may sleep or impose execution limits. Long video encoding and sustained outbound bandwidth typically require an always-on worker. Use short private test streams first.
