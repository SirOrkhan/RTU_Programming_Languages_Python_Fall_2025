"""
Task 3 – Function with Combined Logic
------------------------------------
Write a function `analyze_sentence(text)` that returns:
1. total character count (len)
2. word count (split)
3. whether it contains the word "Python" (case-insensitive)
Return results as a tuple and print summary in main.
"""


def analyze_sentence(text):
    """Return length, word count, and whether 'Python' appears in text."""
    # TODO: implement function logic
    total_chars = len(text)
    word_count = len(text.split())
    contains_python = "python" in text.lower()
    return total_chars, word_count, contains_python


if __name__ == "__main__":
    # TODO: read sentence from input, call function, and print results
    sentence = input("Enter a sentence: ")
    total_chars, word_count, contains_python = analyze_sentence(sentence)

    print(f"\nSentence analysis:")
    print(f"- Total characters: {total_chars}")
    print(f"- Word count: {word_count}")
    print(f"- Contains 'Python': {'Yes' if contains_python else 'No'}")
