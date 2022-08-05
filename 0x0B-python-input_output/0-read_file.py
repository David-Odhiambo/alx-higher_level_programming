#!/usr/bin/python3
"""
Module for read_file mode.
"""


def read_file(filename=""):
    """
    Reads test file and prints to STDOUT
    """

    with open('filename', "r", encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
