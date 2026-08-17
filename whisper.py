import os
import glob
import subprocess

def _load_cuda_dlls():
    if os.name != "nt":
        return

    import ctypes
    import importlib.util

    for package in ("nvidia.cublas", "nvidia.cudnn"):
        spec = importlib.util.find_spec(package)
        if spec is None or not spec.submodule_search_locations:
            continue

        dll_dir = os.path.join(spec.submodule_search_locations[0], "bin")
        if not os.path.isdir(dll_dir):
            continue

        os.add_dll_directory(dll_dir)
        for dll_path in glob.glob(os.path.join(dll_dir, "*.dll")):
            ctypes.WinDLL(dll_path)


_load_cuda_dlls()

from faster_whisper import WhisperModel

def timeconvert(time):
    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    milliseconds = round((time % 1) * 1000)

    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

def transcribe(course, lectureNumber):
    video_path = glob.glob(f"lectures/{course}/weeks/week-{lectureNumber}/*.mp4")[0]
    subprocess.run(["ffmpeg", "-i", video_path, f"lectures/{course}/weeks/week-{lectureNumber}/week-{lectureNumber}.wav"])
    audio_path = glob.glob(f"lectures/{course}/weeks/week-{lectureNumber}/*.wav")[0]

    try:
        model = WhisperModel("medium", device="cuda", compute_type="float16")
    except RuntimeError:
        print("No CUDA GPU found, falling back to CPU")
        model = WhisperModel("medium", device="cpu", compute_type="int8")

    segments = model.transcribe(audio_path)

    srt_path = f"lectures/{course}/weeks/week-{lectureNumber}/output/week-{lectureNumber}.srt"
    with open(srt_path, "w") as file:
        for count, segment in enumerate(segments, 1):
            startTime = timeconvert(segment.start)
            endTime = timeconvert(segment.end)
            file.write(f"{str(count)}\n{startTime} -->  {endTime}\n{segment.text}\n\n")






