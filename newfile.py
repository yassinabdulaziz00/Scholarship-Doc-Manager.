# Text Analyzer Tool
# Developed by: Yassin Abdulaziz Ibrahim

def analyze_text():
    print("--- AI Text Analyzer ---")
    text = input("Enter the text you want to analyze: \n")
    
    if not text:
        print("Text is empty!")
        return

    # Basic Analysis
    words = text.split()
    word_count = len(words)
    char_count = len(text)
    avg_word_length = char_count / word_count if word_count > 0 else 0

    # Word Frequency Analysis
    word_freq = {}
    for word in words:
        word = word.lower().strip(".,!?;:")
        word_freq[word] = word_freq.get(word, 0) + 1

    # Sorting top words
    common_words = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]

    # Display Results
    print("\n" + "="*25)
    print(f"📊 Text Report:")
    print(f"Total Words: {word_count}")
    print(f"Total Characters: {char_count}")
    print(f"Avg Word Length: {avg_word_length:.2f}")
    print("-" * 25)
    print("🔝 Most Common Words:")
    for word, count in common_words:
        print(f"- {word}: {count} times")
    print("="*25)

if __name__ == "__main__":
    analyze_text()
