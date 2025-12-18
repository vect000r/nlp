from abc import ABC, abstractmethod

class Tokenizer(ABC):
    """Abstract base class for all tokenizers."""
    
    @abstractmethod
    def encode(self, text: str) -> list[int]:
        """Convert text to token IDs."""
        pass
    
    @abstractmethod
    def decode(self, token_ids: list[int]) -> str:
        """Convert token IDs back to text."""
        pass
    
    @abstractmethod
    def get_vocab(self) -> dict:
        """Return the vocabulary mapping."""
        pass


class TrainableTokenizer(Tokenizer):
    """Abstract base for tokenizers that can be trained."""
    
    @abstractmethod
    def train(self, text: str, **kwargs) -> None:
        """Train the tokenizer on text. Kwargs for flexibility."""
        pass