from transformers import AutoTokenizer

# Load a pre-trained tokenizer (you can use any available tokenizer, such as 'gpt2', 'bert-base-uncased', etc.)
tokenizer = AutoTokenizer.from_pretrained('gpt2')

def tokenize_and_count_tokens(text):
    # Tokenize the input text
    tokens = tokenizer.tokenize(text)
    
    # Encode the text to get token IDs (useful for the actual tokenization length)
    token_ids = tokenizer.encode(text, add_special_tokens=False)
    
    # Output the tokenized words and the token count
    print(f"\nTokens: {tokens}")
    print(f"Number of tokens: {len(token_ids)}")
    
    return tokens, len(token_ids)

while True:
    # Take input from the user
    user_input = input("\nEnter a word or sentence to tokenize (or type 'exit' to quit): ")

    # Break the loop if the user types 'exit' or 'quit'
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting the program.")
        break

    # Tokenize and display the result
    tokens, token_count = tokenize_and_count_tokens(user_input)
