import pytest
from gpt_tokenizer import GPT4Tokenizer

class TestGPT4Tokenizer:
    
    @pytest.fixture
    def tokenizer(self):
        tok = GPT4Tokenizer()
        tok.vocab_size = 256
        tok.merges = {}
        return tok
    
    def test_initialization(self, tokenizer):
        assert tokenizer.vocab == {}
        assert tokenizer.merges == {}
        assert tokenizer.pattern is not None
    
    def test_get_stats(self, tokenizer):
        token_ids = [1, 2, 2, 3, 1, 2]
        stats = {}
        result = tokenizer.get_stats(token_ids, stats)
        assert result[(1, 2)] == 2
        assert result[(2, 2)] == 1
        assert result[(2, 3)] == 1
        assert result[(3, 1)] == 1
    
    def test_merge_consecutive_pairs(self, tokenizer):
        token_ids = [1, 2, 3, 1, 2, 4]
        merged = tokenizer.merge(token_ids, (1, 2), 99)
        assert merged == [99, 3, 99, 4]
    
    def test_merge_no_pairs(self, tokenizer):
        token_ids = [1, 2, 3, 4]
        merged = tokenizer.merge(token_ids, (5, 6), 99)
        assert merged == token_ids
    
    def test_merge_overlapping_pairs(self, tokenizer):
        token_ids = [1, 1, 1]
        merged = tokenizer.merge(token_ids, (1, 1), 99)
        assert merged == [99, 1]
    
    def test_train_basic(self, tokenizer):
        tokenizer.vocab_size = 260
        text = "hello world"
        tokenizer.train(text)
        assert len(tokenizer.vocab) > 256
        assert len(tokenizer.merges) > 0
    
    def test_train_vocab_size_exception(self, tokenizer):
        tokenizer.vocab_size = 100
        result = tokenizer.train("test text")
        assert result == {}
    
    def test_encode_chunks_basic(self, tokenizer):
        tokenizer.vocab_size = 260
        tokenizer.train("hello")
        chunk_bytes = "hi".encode("utf-8")
        result = tokenizer.encode_chunks(chunk_bytes)
        assert isinstance(result, list)
        assert all(isinstance(x, int) for x in result)
    
    def test_encode_basic(self, tokenizer):
        tokenizer.vocab_size = 260
        tokenizer.train("hello world")
        token_ids = tokenizer.encode("hello")
        assert isinstance(token_ids, list)
        assert len(token_ids) > 0
    
    def test_decode_valid_tokens(self, tokenizer):
        tokenizer.vocab = {72: b'H', 101: b'e', 108: b'l', 111: b'o'}
        result = tokenizer.decode([72, 101, 108, 108, 111])
        assert result == "Hello"
    
    def test_decode_invalid_token(self, tokenizer):
        tokenizer.vocab = {72: b'H'}
        with pytest.raises(ValueError):
            tokenizer.decode([72, 999])
    
    def test_encode_decode_roundtrip(self, tokenizer):
        tokenizer.vocab_size = 300
        text = "test"
        tokenizer.train(text)
        encoded = tokenizer.encode(text)
        decoded = tokenizer.decode(encoded)
        assert decoded == text