import re
import random
import json

class Eliza():
    def __init__(self, patterns_file: str):
        self.patterns_file = patterns_file
        self.patterns = []
        self.reflections = {}
        self.defaults = {}
    
    def load_patterns(self):
        with open(self.patterns_file, "r") as patterns_file:
            
            try:
                patterns = json.load(patterns_file)
            
                for pattern in patterns['patterns']:
                    self.patterns.append(pattern)
            
                self.reflections = patterns['reflections']
                self.defaults = patterns['defaults']
            
            except Exception as e:
                print("Invalid json")
                return 1

    
    def get_patterns(self):
        return f'Patterns loaded: {self.patterns}'

    
    def get_reflections(self):
        return f'Reflections loaded: {self.reflections}'

    
    def apply_reflections(self, text: str):
        words = text.split()

        reflected_words = []

        for word in words:

            if word in self.reflections:
                reflected_words.append(self.reflections[word])
            else:
                reflected_words.append(word)
        
        return ' '.join(reflected_words)


    def match_and_respond(self, input: str):
        clean_input = input.lower().strip()

        for pattern in self.patterns:
            match = re.search(pattern['pattern'], clean_input)

            if match:
                matched_groups = match.groups()
                response_template = random.choice(pattern['responses'])
            
                reflected_groups = []
                for group in matched_groups:
                    reflected = self.apply_reflections(group)
                    reflected_groups.append(reflected)
                
                response = response_template.format(*reflected_groups)

                return response

            else:
                return random.choice(self.defaults)
    
    
    
    def start(self):
        

        print(r"""
             ______     __         __     ______     ______    
            /\  ___\   /\ \       /\ \   /\___  \   /\  __ \   
            \ \  __\   \ \ \____  \ \ \  \/_/  /__  \ \  __ \  
             \ \_____\  \ \_____\  \ \_\   /\_____\  \ \_\ \_\ 
              \/_____/   \/_____/   \/_/   \/_____/   \/_/\/_/ 
              """)

        print("Welcome to the Eliza chatbot! Ask anything:")

