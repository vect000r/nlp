import re
import random
import json

class Eliza():
    def __init__(self, patterns_file: str):
        self.patterns_file = patterns_file
        self.patterns = []


    def load_patterns(self):
        with open(self.patterns_file, "r") as patterns_file:
            for pattern in patterns_file.json():
                pass

