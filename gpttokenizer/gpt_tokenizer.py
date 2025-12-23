import regex as re
from basic_tokenizer import BasicTokenizer

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
        pass


    def train(self, text, verbose=False):
        pass


    def encode(self, text):
        pass

    def decode(self, token_ids):
        pass