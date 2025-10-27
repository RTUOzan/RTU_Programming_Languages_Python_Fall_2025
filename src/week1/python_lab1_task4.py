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


def count_characters(text):
    """Count non-space characters in a string."""
    return len(text.replace(" ", ""))  # TODO: implement


def count_words(text):
    """Count number of words in a string."""
    return len(text.split())  # TODO: implement


def extract_numbers(text):
    """Return list of integers found in text."""
    numbers = []
    for word in text.split():
        if word.isdigit():
            numbers.append(int(word))
    return numbers  # TODO: implement


def analyze_text(text):
    """Perform text-based arithmetic analysis."""
    char_count = count_characters(text)
    word_count = count_words(text)
    numbers = extract_numbers(text)
    total = sum(numbers)
    average = total / len(numbers) if numbers else 0
    return (
        char_count,
        word_count,
        numbers,
        total,
        average,
    )  # TODO: call helper functions and compute total, average, etc.


if __name__ == "__main__":
    user_input = input("Enter some text: ")  # TODO: read input
    chars, words, nums, total, avg = analyze_text(
        user_input
    )  # TODO: call analyze_text()
    print(f"Non-space characters: {chars}")
    print(f"Word count: {words}")
    print(f"Numbers found: {nums}")
    print(f"Sum of numbers: {total}")
    print(f"Average of numbers: {avg:.2f}")  # TODO: print results
