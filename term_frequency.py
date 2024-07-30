from collections import Counter
import re

def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation and non-alphanumeric characters
    text = re.sub(r'\W+', ' ', text)
    return text

def calculate_term_frequency(text):
    # Preprocess the text
    cleaned_text = preprocess_text(text)
    # Tokenize the text into words
    words = cleaned_text.split()
    # Count the occurrences of each word
    word_counts = Counter(words)
    # Calculate the total number of words
    total_words = len(words)
    # Calculate the term frequency for each word
    term_frequency = {word: count / total_words for word, count in word_counts.items()}
    return term_frequency

# Example usage
text = "This is a sample text. This text is just a sample."
tf = calculate_term_frequency(text)
print(tf)
