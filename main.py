import sys
import organise
import whisper
import md_export

course = sys.argv[1]
lectureNumber = sys.argv[2]

organise.organiseFolders(course, lectureNumber)
organise.moveContents(course, lectureNumber)

whisper.transcribe(course, lectureNumber)

md_export.convertToMarkdown(course, lectureNumber)
md_export.filterTemplateImages(course, lectureNumber)


