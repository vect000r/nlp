import regex as re
from basic_tokenizer import BasicTokenizer, VocabSizeException

# TODO: OVERRIDE INHERTIED METHODS 


class GPT4Tokenizer(BasicTokenizer):
    def __init__(self):
        super().__init__()
        self.pattern = r"""'(?i:[sdmt]|ll|ve|re)|[^\r\n\p{L}\p{N}]?+\p{L}+|\p{N}{1,3}| ?[^\s\p{L}\p{N}]++[\r\n]*|\s*[\r\n]|\s+(?!\S)|\s+"""
        self.vocab = {}

    def get_stats(self, token_ids, stats):
        """
        Identifies consecutive pairs from token ids.
        """

        for pair in zip(token_ids, token_ids[1:]):
            stats[pair] = stats.get(pair, 0) + 1
        return stats
    

    def merge(self, token_ids, pair, new_index):
        """
        Merges pairs.
        """
        
        merged = []
        i = 0
        num_tokens = len(token_ids)

        while i < num_tokens:
            if (i < num_tokens - 1) and (token_ids[i] == pair[0]) and (token_ids[i + 1] == pair[1]):
                merged.append(new_index)
                i += 2
            else:
                merged.append(token_ids[i])
                i += 1
        
        return merged


    def train(self, text, verbose=False):
        """
        Function which trains the tokenizer on a given text.
        """

        try:
            if self.vocab_size < 256:
                raise VocabSizeException
            
            num_merges = self.vocab_size - 256
            text_chunks = re.findall(self.pattern, text)
            token_ids = [list(chunk.encode('utf-8') for chunk in text_chunks)]
            self.vocab = {idx: bytes([idx]) for idx in range(256)}

            for i in range(num_merges):
                stats = {}
                for chunk_token in token_ids:
                    self.get_stats(chunk_token, stats)
                top_pair = max(stats, key=stats.get)
                index = 256 + i
                if verbose:
                    print(f"Merged pair: {top_pair} -> {index}")
                
                token_ids = [self.merge(chunk_token, top_pair, index) for chunk_token in token_ids]
                
                self.vocab[index] = self.vocab[top_pair[0]] + self.vocab[top_pair[1]]
                self.merges[top_pair] = index

        except VocabSizeException as err:
            print("Vocab size is under 256")
            return {}

    def encode(self, text):
        pass

    def decode(self, token_ids):
        pass