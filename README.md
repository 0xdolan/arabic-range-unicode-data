# Unicode Character Data Generator

This Python script allows you to generate Unicode character data within specified code point ranges and save it in both JSON and Markdown formats. It's particularly useful for creating reference tables of Unicode characters for various scripts and ranges.

## Features

- Generates Unicode character data for specified code point ranges.
- Retrieves character names and categories using the `unicodedata` module.
- Outputs data in JSON and Markdown formats for easy reference and documentation.

## Usage

1. Run the `generate_unicode_json` function to generate Unicode data in JSON format.
2. Run the `generate_markdown` function to convert the JSON data into a Markdown table.
3. The generated data files are named `unicode_data.json` (JSON format) and `unicode_data.md` (Markdown format).

Example:

```bash
python unicode_data_generator.py
```
