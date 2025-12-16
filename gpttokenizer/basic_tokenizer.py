class BasicTokenizer:
    def __init__(self):
        self.vocab_size = 1024
        self.merges ={}

    def get_stats(self, token_ids):
        counts = {}
        
        for pair in zip(token_ids, token_ids[1:]):
            counts[pair] = counts.get(pair, 0) + 1
        
        return counts


    def merge(self, token_ids, pair, new_index):
        pass

    def train(self):
        """
        Function which trains the tokenizer on a given text and vocab size.
        """
        pass

    def encode(self, text):
        """
        Encodes given text.
        """
        token_ids = list(text.encode('utf-8'))
        
        while len(token_ids) >= 2:
            stats = self.get_stats(token_ids)
            pair = min(stats, key = lambda x: self.merges.get(x, float('inf')))

            if pair not in self.merges:
                break
            index = self.merges[pair]
            token_ids = self.merge(token_ids, pair, index)
        return token_ids
    

    def decode(self):
        """
        Decodes given text.
        """
        pass