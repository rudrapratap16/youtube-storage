# youtube-storage

Store any file as a YouTube video, and get it back later — using YouTube as free, (nearly) unlimited cold storage.

Files are split into small chunks, each chunk is base64-encoded and turned into a QR code, and the QR codes are stitched together frame-by-frame into a video. The video is uploaded to YouTube. To retrieve the file, the video is downloaded again, each frame's QR code is decoded, and the original bytes are reassembled.

## How it works

**Encode & upload**
1. The source file is read in small chunks (1 KB at a time).
2. Each chunk is base64-encoded and rendered as a QR code image (1080×1080).
3. A "start buffer" marker frame is repeated for 60 frames, followed by all the QR-code frames, followed by a "end buffer" marker frame for 60 more frames.
4. The frames are written to an `.avi` video at 30 fps.
5. The video is uploaded to YouTube via the YouTube Data API v3.

**Download & decode**
1. The YouTube video is downloaded with `yt-dlp`.
2. The video is read frame-by-frame; each frame's QR code is decoded with `pyzbar`.
3. Start/end buffer marker frames are skipped.
4. The remaining base64 chunks are decoded and concatenated back into the original file.

## Repository structure

```
youtube-storage/
├── upload to youtube/
│   ├── preprocess_data_1.py   # Reads a file, generates QR-code frames, builds temporary/video.avi
│   ├── upload_2.py            # Uploads temporary/video.avi to YouTube via the YouTube Data API
│   ├── buffers/
│   │   ├── start/              # "start buffer" marker frame(s)
│   │   └── end/                 # "end buffer" marker frame(s)
│   ├── credentials/             # Place your YouTube OAuth credentials JSON here
│   └── temporary/               # Working directory for the generated video
├── download and decode/
│   ├── download.py             # Downloads a YouTube video (via yt-dlp) into temporary/
│   ├── decode_video.py         # Decodes the QR frames back into the original file
│   └── temporary/               # Working directory for the downloaded video
├── outputs/                     # Reconstructed files land here
├── purge.py                     # Deletes everything in both temporary/ folders
└── requirements.txt
```

## Requirements

- Python 3.9+
- A Google Cloud project with the **YouTube Data API v3** enabled, plus an OAuth client so you can upload videos to your own channel (`upload_2.py` expects an authorized-user credentials JSON with the `youtube.upload` scope).
- The `zbar` shared library installed on your system, since `pyzbar` depends on it, e.g.:
  - Debian/Ubuntu: `sudo apt-get install libzbar0`
  - macOS: `brew install zbar`

Install the Python dependencies:

```bash
python -m venv venv
source venv/bin/activate        # venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Key libraries used: `opencv-python`, `qrcode`, `pyzbar`, `pillow`, `numpy`, `pandas`, `yt-dlp`, `google-api-python-client`, `google-auth-oauthlib`.

## Usage

> **Note:** the scripts currently use hard-coded paths/links rather than command-line arguments, so you'll need to edit a couple of lines in each script before running it.

### 1. Encode a file into a video

In `upload to youtube/preprocess_data_1.py`, set:
```python
path_to_csv_file = "path/to/your/file"
```
Then run it from inside the `upload to youtube/` folder:
```bash
cd "upload to youtube"
python preprocess_data_1.py
```
This produces `temporary/video.avi`.

### 2. Upload the video to YouTube

Place your OAuth credentials JSON at `upload to youtube/credentials/youtube_cred.json`, then run:
```bash
python upload_2.py
```
This uploads `temporary/video.avi` as a **public** video and prints the resulting video ID. Adjust the title/description/tags/category at the bottom of the script as needed.

### 3. Download the video back

In `download and decode/download.py`, set:
```python
link = "https://www.youtube.com/watch?v=YOUR_VIDEO_ID"
```
Then run it from inside the `download and decode/` folder:
```bash
cd "download and decode"
python download.py
```
This saves the video into `temporary/`.

### 4. Decode the video back into a file

In `download and decode/decode_video.py`, set:
```python
vid_path = "path/to/downloaded/video"
output_file = "../outputs/your_filename.ext"
```
Then run:
```bash
python decode_video.py
```
The reconstructed file is written to the path you set (typically inside `outputs/`).

### 5. Clean up temporary files

From the repo root:
```bash
python purge.py
```
This empties both `upload to youtube/temporary/` and `download and decode/temporary/`.

## Limitations

- Chunk size is fixed at 1 KB per QR code frame, so large files produce long videos and can take a while to encode/decode.
- Paths, video links, and credential locations are hard-coded in the scripts rather than passed as arguments — edit them directly before each run.
- Uploaded videos are set to `public` by default; change `privacyStatus` in `upload_2.py` if you'd rather keep them unlisted or private.
- YouTube's video compression could, in principle, distort QR codes; if decoding fails partway through, try re-uploading at a higher bitrate/resolution or adjusting the QR error-correction level.

## License

No license file is currently included in this repository — add one if you intend for others to reuse this code.
