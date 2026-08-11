from faster_whisper import WhisperModel
from datetime import timedelta

audio_path = "/"

model = WhisperModel("medium", device="cuda", compute_type="float16")

segments, info = model.transcribe(audio_path)

def timeconvert(time):
    hours = int(time // 3600)
    minutes = int((time % 3600) // 60)
    seconds = int(time % 60)
    milliseconds = round((time % 1) * 1000)

    return f"{hours:02}:{minutes:02}:{seconds:02},{milliseconds:03}"

file = open("myfile.srt", "w") 

for count, segment in enumerate(segments, 1):
    startTime = timeconvert(segment.start)
    endTime = timeconvert(segment.end)
    
    file.write(f"{str(count)}\n{startTime} -->  {endTime}\n{segment.text}\n\n")

file.close()

