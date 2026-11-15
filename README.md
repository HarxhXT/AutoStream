# AutoStream

Android client + FastAPI backend starter for cloud-hosted prerecorded video livestreaming to Kick and YouTube.

## What is included
- Android app source (Kotlin + Jetpack Compose)
- Video picker UI
- Kick / YouTube destination selection UI
- FastAPI video upload endpoint
- FFmpeg worker foundation
- GitHub Actions workflow that builds a debug APK and publishes it as an artifact

## What is not yet production-ready
This is a buildable development foundation, not a finished public streaming service. YouTube OAuth/broadcast creation, secure user accounts, encrypted platform credentials, durable cloud storage/queue, deployed always-on workers, stream monitoring, and production security still need to be implemented and configured.

A successful APK build does not mean cloud streaming is deployed.

## Build APK using GitHub
1. Create a new GitHub repository named `AutoStream`.
2. Upload this ZIP's contents (the files inside the `AutoStream-GitHub` folder) to the repository root. Do not upload the ZIP as a single file.
3. Open the repository's **Actions** tab.
4. Select **Build Android APK** and run it, or push a commit to `main`.
5. Open the completed workflow run and download the `AutoStream-debug-apk` artifact.
6. Extract the artifact ZIP to get `app-debug.apk`.

## Build locally
Install JDK 17 and Android SDK, then:
```bash
cd android
gradle assembleDebug
```
APK output:
`android/app/build/outputs/apk/debug/app-debug.apk`

## Backend local development
Requires Docker:
```bash
docker compose up --build
```
API docs: `http://localhost:8000/docs`

## Streaming notes
- Kick: users can supply their own RTMPS ingest URL and stream key from their Kick creator dashboard. Store secrets encrypted on the server; never commit them.
- YouTube: use Google OAuth and YouTube Live Streaming API to create/manage broadcasts and stream ingestion. Do not ask users to paste Google passwords.
- Long-running video streaming requires an always-on worker and sufficient outbound bandwidth. Many free hosting tiers sleep, restrict CPU, or disallow long-running processes.

## Content and security
Only stream content you own or are authorized to broadcast. Do not publish API keys, stream keys, OAuth client secrets, or `.env` files to GitHub.
