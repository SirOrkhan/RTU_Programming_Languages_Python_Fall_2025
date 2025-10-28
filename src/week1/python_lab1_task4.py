"""
Task 4 – Text-based Arithmetic Analyzer
--------------------------------------
Create a text-based analyzer that:
1. Counts non-space characters.
2. Counts words.
3. Extracts numbers and computes their sum and average.
Use helper functions:
- count_characters(text)
- count_words(text)
- extract_numbers(text)
- analyze_text(text)
Print formatted summary in main.
"""

import re


def count_characters(text):
    """Count non-space characters in a string."""
    # TODO: implement
    return len(text.replace(" ", ""))


def count_words(text):
    """Count number of words in a string."""
    # TODO: implement
    return len(text.split())


def extract_numbers(text):
    """Return list of integers found in text."""
    # TODO: implement
    numbers = re.findall(r"\d+", text)  # find all digit groups
    return [int(num) for num in numbers]


def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    # TODO: call helper functions and compute total, average, etc.
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)

    total = sum(numbers) if numbers else 0
    average = total / len(numbers) if numbers else 0

    return {
        "characters": char_count,
        "words": word_count,
        "numbers": numbers,
        "total": total,
        "average": average,
    }


if __name__ == "__main__":
    # TODO: read input, call analyze_text(), and print results
    text = input("Enter a text for analysis: ")
    result = analyze_text(text)

    print("\nText Analysis Summary:")
    print(f"- Non-space characters: {result['characters']}")
    print(f"- Word count: {result['words']}")
    print(f"- Numbers found: {result['numbers'] if result['numbers'] else 'None'}")
    print(f"- Sum of numbers: {result['total']}")
    print(f"- Average of numbers: {result['average']:.2f}")
