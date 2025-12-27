from gpt_tokenizer import GPT4Tokenizer

def main():
    print("=== Tokenizer Demo ===\n")
    
    tokenizer = GPT4Tokenizer()
    tokenizer.vocab_size = 300
    
    text = "hello world"
    print(f"Training on: '{text}'")
    tokenizer.train(text)
    print(f"Vocab size after training: {len(tokenizer.vocab)}")
    print(f"Number of merges: {len(tokenizer.merges)}\n")
    
    test_text = "hello"
    encoded = tokenizer.encode(test_text)
    decoded = tokenizer.decode(encoded)
    
    print(f"Original text: '{test_text}'")
    print(f"Encoded: {encoded}")
    print(f"Decoded: '{decoded}'")
    print(f"Round-trip successful: {test_text == decoded}")

if __name__ == "__main__":
    main()

    