import re
from pdfminer.high_level import extract_pages, extract_text

def extract_sentence_ending(text):
    pattern = re.compile(r"[a-zA-Z]+,{1}")
    matches = pattern.findall(text)
    print(matches)

text = extract_text("sample.pdf")

for page_layout in extract_pages("sample.pdf"):
    for element in page_layout:
        print(element)

extract_sentence_ending(text)