# -*- coding: utf-8 -*-

import json
import unicodedata


def generate_unicode_json():
    unicode_ranges = [
        (0x0600, 0x06FF, "Arabic"),
        (0x0750, 0x077F, "Arabic Supplement"),
        (0x0870, 0x089F, "Arabic Extended-B"),
        (0x08A0, 0x08FF, "Arabic Extended-A"),
        (0xFB50, 0xFDFF, "Arabic Presentation Forms-A"),
        (0xFE70, 0xFEFF, "Arabic Presentation Forms-B"),
        (0x10E60, 0x10E7F, "Rumi Numeral Symbols"),
        (0x10EC0, 0x10EFF, "Arabic Extended-C"),
        (0x1EC70, 0x1ECBF, "Indic Siyaq Numbers"),
        (0x1ED00, 0x1ED4F, "Ottoman Siyaq Numbers"),
        (0x1EE00, 0x1EEFF, "Arabic Mathematical Alphabetic Symbols"),
    ]

    data = []

    for start, end, range_name in unicode_ranges:
        for code_point in range(start, end + 1):
            char = chr(code_point)
            char_name = unicodedata.name(char, "Unknown")
            category = unicodedata.category(char)
            data.append(
                {
                    "Code Point": f"U+{code_point:04X}",
                    "Character": char,
                    "Character Name": char_name,
                    "Category": category,
                    "RANGE": f"U+{start:04X}-U+{end:04X}",
                    "RANGE_NAME": range_name,
                }
            )

    with open("unicode_data.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)


def generate_markdown():
    with open("unicode_data.json", "r", encoding="utf-8") as json_file:
        data = json.load(json_file)

    markdown_output = (
        "| Code Point | Character | Character Name | Category | RANGE | RANGE_NAME |\n"
    )
    markdown_output += (
        "|------------|-----------|----------------|----------|-------|------------|\n"
    )

    for entry in data:
        markdown_output += f"| {entry['Code Point']} | {entry['Character']} | {entry['Character Name']} | {entry['Category']} | {entry['RANGE']} | {entry['RANGE_NAME']} |\n"

    with open("unicode_data.md", "w", encoding="utf-8") as markdown_file:
        markdown_file.write(markdown_output)


if __name__ == "__main__":
    generate_unicode_json()
    generate_markdown()
