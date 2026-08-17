import pymupdf4llm
import glob

def convertToMarkdown(course, lectureNumber):
    pdfs = glob.glob(f"lectures/{course}/weeks/week-{lectureNumber}/*.pdf")

    for pdf in pdfs:
        md_text = pymupdf4llm.to_markdown(pdf)

        output_file = f"lectures/{course}/weeks/week-{lectureNumber}/output/{course}-lecture-{lectureNumber}.md"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md_text)