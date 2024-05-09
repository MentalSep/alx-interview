#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    count = 0

    for byte in data:
        mask = 1 << 7
        while mask & byte:
            count += 1
            mask >>= 1

        if count == 0:
            continue

        if count == 1 or count > 4:
            return False

        # Check for the expected format 10xxxxxx after the initial byte
        mask = (1 << 7) >> count
        if mask & byte == 0:
            return False

        count -= 1

    return count == 0
