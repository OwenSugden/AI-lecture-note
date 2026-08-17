import sys
import organise
import whisper
import markdown

course = sys.argv[1]
lectureNumber = sys.argv[2]

organise.organiseFolders(course, lectureNumber)
organise.moveContents(course, lectureNumber)

whisper.transcribe(course, lectureNumber)

markdown.convertToMarkdown(course, lectureNumber)


