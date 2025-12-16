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
        _tokens = []
        i = 0

        while i < len(token_ids):
            if (i < len(token_ids) - 1) and (token_ids[i] == pair[0]) and (token_ids[i + 1] == pair[1]):
                _tokens.append(new_index)
                i += 2
            else:
                _tokens.append(token_ids[i])
                i += 1
        return _tokens
    
    def get_vocab(self):
        vocab = {idx: bytes([idx]) for idx in range(256)}
        for (p0, p1), idx in self.merges.items():
            vocab[idx] = vocab[p0] + vocab[p1]
        return vocab
    

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
        vocab = self.get_vocab()
        b_tokens = b"".join(vocab[idx] for idx in token_ids)
        text = b_tokens.decode('utf-8', errors="replace")
        return text