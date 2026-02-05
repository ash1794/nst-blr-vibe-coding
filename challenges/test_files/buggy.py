"""
A collection of buggy functions.
Your agent's job: find and fix all the bugs!
"""


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)  # 💥 Bug: crashes on empty list
    return average


def find_max(numbers):
    """Find the maximum value in a list."""
    max_val = 0  # 💥 Bug: fails for negative numbers
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val


def reverse_string(text):
    """Reverse a string."""
    reversed_text = ""
    for i in range(len(text), 0, -1):  # 💥 Bug: off-by-one error
        reversed_text += text[i]
    return reversed_text


def count_words(sentence):
    """Count the number of words in a sentence."""
    words = sentence.split(" ")
    return len(words)  # 💥 Bug: multiple spaces give wrong count


if __name__ == "__main__":
    # These tests should ALL pass after fixing
    print("Test 1:", calculate_average([10, 20, 30]))  # Should print 20.0
    print("Test 2:", calculate_average([]))             # Should print 0 (not crash)
    print("Test 3:", find_max([-5, -2, -8]))            # Should print -2 (not 0)
    print("Test 4:", reverse_string("hello"))           # Should print "olleh"
    print("Test 5:", count_words("hello  world"))       # Should print 2 (not 3)
