import os
import glob
import shutil

def organiseFolders(course, weekNumber, lectureNumber):
  os.makedirs(f"lectures/{course}/weeks/week-{weekNumber}/lecture-{lectureNumber}/output", exist_ok=True)

def moveContents(course, weekNumber, lectureNumber):
  filePaths = glob.glob("inbox/*")
  destination = f"lectures/{course}/weeks/week-{weekNumber}/lecture-{lectureNumber}"

  mp4Files = [path for path in filePaths if path.lower().endswith(".mp4")]
  pdfFiles = [path for path in filePaths if path.lower().endswith(".pdf")]

  if len(mp4Files) != 1:
    raise ValueError(f"Inbox should have exactly 1 mp4 file, found {len(mp4Files)}")

  if len(pdfFiles) < 1:
    raise ValueError("Inbox should have at least 1 pdf file")

  for path in filePaths:
    shutil.move(path, destination)