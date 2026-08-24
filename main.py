import sys
import organise
import whisper
import md_export

course = sys.argv[1]
weekNumber = sys.argv[2]
lectureNumber = sys.argv[3]

organise.organiseFolders(course, weekNumber, lectureNumber)
organise.moveContents(course, weekNumber, lectureNumber)

whisper.transcribe(course, weekNumber, lectureNumber)

md_export.convertToMarkdown(course, weekNumber, lectureNumber)
md_export.filterTemplateImages(course, weekNumber, lectureNumber)


