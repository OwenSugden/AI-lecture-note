# AI Lecture Notes

A personal automation pipeline that turns raw lecture recordings and slide decks into structured notes. It combines local audio transcription with slide content extraction, with the eventual goal of pushing organized notes into Notion.

## What it does

1. **Transcription** — Extracts audio from a lecture video (`ffmpeg`) and transcribes it locally using `faster-whisper`, producing timestamped `.srt` subtitle files.
2. **Slide parsing** — Converts lecture slide PDFs into Markdown for easy downstream processing.
3. **(Planned)** — Merge transcript + slide content and push structured notes to Notion via the Notion API, with a simple local drag-and-drop front end.

## Project structure

```
lectures/
  weeks/
    week-1/
      *.mp4      (raw lecture recording — ignored by git)
      *.wav      (extracted audio — ignored by git)
      *.pdf      (lecture slides — ignored by git)
      *.srt      (generated transcript — ignored by git)
```

Each week's raw files and generated outputs are excluded from version control (see `.gitignore`) — only the processing scripts are tracked.

## Requirements

- Python 3.13
- [ffmpeg](https://ffmpeg.org/download.html) installed and available on your system PATH
- An NVIDIA GPU with CUDA support (optional, but strongly recommended — CPU transcription is dramatically slower)

## Libraries to install

```bash
pip install faster-whisper tqdm pikepdf pymupdf4llm
```

If you're running on GPU and hit a `cublasXX.dll` / `cudnnXX.dll` load error on Windows, also install:

```bash
pip install nvidia-cublas-cu12 nvidia-cudnn-cu12
```

## Usage

Set the target week and run the transcription script:

```bash
python whisper.py
```

This will locate the `.mp4` in the matching `lectures/weeks/week-X/` folder, extract audio, transcribe it, and write out `week-X.srt` in the same folder.

## Status

This is an active, in-progress learning project — transcription is functional; slide parsing and Notion integration are in development.
