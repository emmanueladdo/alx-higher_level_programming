#!/usr/bin/python3
"""The Module text_indentation
Adds two new lines after a set of characters.
"""


def text_indentation(text):
    """Prints text with added two newlines
    after each of these characters {'.', '?', ':'}.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    demil = ".:?"

    for delim in demil:
        text = (delim + "\n\n").join(
            [line.strip(" ") for line in text.split(delim)])

    print(f"{text}", end="")
