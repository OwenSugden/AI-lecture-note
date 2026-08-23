# AI Lecture Notes

A personal automation pipeline that turns raw lecture recordings and slide decks into structured notes. It combines local audio transcription with slide content extraction, with the eventual goal of pushing organized notes into Notion.

## What it does

1. **Folder input** — Drag and drop the PDF lecture slides and the mp4 lecture recording into the **inbox** directory.
2. **Transcription** — Extracts audio from a lecture video (`ffmpeg`) and transcribes it locally using `faster-whisper`, producing `.txt` files.
3. **Slide parsing** — Converts lecture slide PDFs into Markdown for easy downstream processing.
   

## Requirements

- Python 3.13
- [ffmpeg](https://ffmpeg.org/download.html) installed and available on your system PATH
- An NVIDIA GPU with CUDA support (optional, but strongly recommended — CPU transcription is dramatically slower)

## Setup

This project uses a Python virtual environment (`venv`) to keep its dependencies isolated from your global Python install. All required packages are listed in `requirements.txt`.

**1. Create the virtual environment** (run once, from the project root):

```bash
python -m venv venv
```

**2. Activate it** (run every time you open a new terminal session to work on this project):

- macOS / Linux:
  ```bash
  source venv/bin/activate
  ```
- Windows (PowerShell):
  ```powershell
  venv\Scripts\Activate.ps1
  ```

Your terminal prompt should now show `(venv)` at the start of the line, confirming it's active.

**3. Install dependencies:**

```bash
pip install -r requirements.txt
```

GPU-acceleration packages (`nvidia-cublas-cu12`, `nvidia-cudnn-cu12`) are only installed automatically on Windows and Linux, since they require an NVIDIA GPU and don't apply on macOS. If you're on Windows/Linux with an NVIDIA GPU and still hit a `cublasXX.dll` / `cudnnXX.dll` load error at runtime, this is a known Windows DLL-path issue — see the code comments in `whisper.py` for the fix.

If you don't have an NVIDIA GPU, transcription will fall back to running on CPU (slower, but fully functional).

## Usage

Before running the command below, ensure the necessary files are in the **inbox** directory.
Set the target week and run the transcription script:

```bash
python main.py {course} {week number}
```

This will locate the `.mp4` in the matching `lectures/weeks/week-X/` folder, extract audio, transcribe it, and write out `week-X.txt` in the same folder.

## Status

This is an active, in-progress learning project — transcription is functional; slide parsing and Notion integration are in development.
