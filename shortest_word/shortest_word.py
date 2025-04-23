"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(s):

    split_string = s.split()
    current_lowest = len(split_string[0])

    for word in split_string:
        if len(word) < current_lowest:
            current_lowest = len(word)

    return current_lowest
