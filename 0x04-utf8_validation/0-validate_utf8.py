#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    num_bytes = 0

    for num in data:
        bin_repr = format(num, '#010b')[-8:]

        if num_bytes == 0:
            num_bytes = len(bin_repr.split('0')[0])

            if num_bytes == 0:
                continue

            num_bytes = 8 - num_bytes

            if num_bytes == 1 or num_bytes > 4:
                return False

        else:
            # Check for the expected format 10xxxxxx after the initial byte
            if not (bin_repr[0] == '1' and bin_repr[1] == '0'):
                return False

            num_bytes -= 1

    return num_bytes == 0
