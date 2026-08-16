import pymupdf4llm
import glob

week_number = 3
pdfs = glob.glob(f"lectures/weeks/week-{week_number}/*.pdf")

for count, pdf in enumerate(pdfs, 1):
    md_text = pymupdf4llm.to_markdown(pdf)

    output_file = f"lectures/weeks/week-{week_number}/lecture-{week_number}.{count}.md"

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(md_text)