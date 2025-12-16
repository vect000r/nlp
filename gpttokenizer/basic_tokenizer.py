class BasicTokenizer:
    def __init__(self, text, ids, vocab_size):
        self.text = text
        self.ids = ids
        self.vocab_size = vocab_size

    def train(self):
        """
        Function which trains the tokenizer on a given text and vocab size.
        """
        pass

    def encode(self):
        """
        Encodes given text.
        """
        pass

    def decode(self):
        """
        Decodes given text.
        """
        pass