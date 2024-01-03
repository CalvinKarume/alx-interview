#!/usr/bin/python3
"""
UTF-8 Validation
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    """
    # Initialize the count of expected continuation bytes
    remaining_bytes = 0

    for byte in data:
        # Check if it's the start of a new character
        if remaining_bytes == 0:
            if byte >> 5 in {0b110, 0b1110}:
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                remaining_bytes = 3
            elif byte >> 7 == 0b1:
                return False
        else:
            # Check if it's a valid continuation byte
            if byte >> 6 != 0b10:
                return False
            remaining_bytes -= 1


    return remaining_bytes == 0
