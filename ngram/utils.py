import xml.etree.ElementTree as ET
import re
import random
from collections import Counter

FILE_1 = "POL0005_beczkowska_kedy-droga.xml"
FILE_2 = "POL0006_beczkowska_w-mieszczanskim-gniezdzie.xml"

def parse_text(path: str) -> list:
    try:
        tree = ET.parse(path)
        root = tree.getroot()
        text = "".join(root.itertext())
        text = text.lower()
        words = re.findall(r'\b\w+\b')
        return words
    
    except FileNotFoundError:
        print(f"File was not found on specified path: {path}")

def ngrams(words: list, n: int) -> list:
    if len(words) < n:
        return []
    return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]
