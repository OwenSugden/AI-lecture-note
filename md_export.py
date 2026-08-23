import pymupdf4llm
import glob
import os
import re
from collections import defaultdict

import imagehash
from PIL import Image

def convertToMarkdown(course, lectureNumber):
    pdfs = glob.glob(f"lectures/{course}/weeks/week-{lectureNumber}/*.pdf")

    for pdf in pdfs:
        image_path = f"lectures/{course}/weeks/week-{lectureNumber}/output/images"
        md_text = pymupdf4llm.to_markdown(pdf, write_images=True, image_path=image_path)

        output_file = f"lectures/{course}/weeks/week-{lectureNumber}/output/{course}-lecture-{lectureNumber}.md"

        with open(output_file, "w", encoding="utf-8") as f:
            f.write(md_text)

def filterTemplateImages(course, lectureNumber, max_occurrences=2, min_area=100 * 100):
    output_dir = f"lectures/{course}/weeks/week-{lectureNumber}/output"
    image_dir = f"{output_dir}/images"
    md_path = f"{output_dir}/{course}-lecture-{lectureNumber}.md"

    image_files = glob.glob(f"{image_dir}/*")

    info = {}
    hash_counts = defaultdict(int)
    for path in image_files:
        with Image.open(path) as img:
            width, height = img.size
            phash = imagehash.phash(img)
        info[path] = (phash, width, height)
        hash_counts[phash] += 1

    to_delete = [
        path
        for path, (phash, width, height) in info.items()
        if width * height < min_area or hash_counts[phash] > max_occurrences
    ]

    for path in to_delete:
        os.remove(path)

    if to_delete:
        deleted_names = {os.path.basename(path) for path in to_delete}
        image_ref_pattern = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")

        with open(md_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        kept_lines = [
            line
            for line in lines
            if not (
                (match := image_ref_pattern.search(line))
                and os.path.basename(match.group(1)) in deleted_names
            )
        ]

        with open(md_path, "w", encoding="utf-8") as f:
            f.writelines(kept_lines)

    return to_delete