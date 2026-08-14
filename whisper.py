import os
os.add_dll_directory(r"C:\Users\User\AppData\Local\Programs\Python\Python313\Lib\site-packages\nvidia\cublas\bin")
import ctypes
ctypes.WinDLL("cublas64_12.dll")                    

from faster_whisper import WhisperModel
import glob
import subprocess

week_number = 3

video_path = glob.glob(f"lectures/weeks/week-{week_number}/*.mp4")[0]
subprocess.run(["ffmpeg", "-i", video_path, f"lectures/weeks/week-{week_number}/week-{week_number}.wav"])
audio_path = glob.glob(f"lectures/weeks/week-{week_number}/*.wav")[0]

model = WhisperModel("medium", device="cuda", compute_type="float16")

segments, info = model.transcribe(audio_path)

def timeconvert(time):
    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    milliseconds = round((time % 1) * 1000)

    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

file = open(f"lectures/weeks/week-{week_number}/week-{week_number}.srt", "w") 

for count, segment in enumerate(segments, 1):
    startTime = timeconvert(segment.start)
    endTime = timeconvert(segment.end)
    file.write(f"{str(count)}\n{startTime} -->  {endTime}\n{segment.text}\n\n")

file.close()

