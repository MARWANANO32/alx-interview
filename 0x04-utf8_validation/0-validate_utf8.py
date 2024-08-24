"""UTF-8 Validation"""


def get_leading_set_bits(num):
    """returns the number of leading set bits (1)"""
    set_bits = 0
    helper = 1 << 7
    while helper & num:
        set_bits += 1
        helper = helper >> 1
    return set_bits


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""
    if not data:
        return False
    for i in data:
        if i < 0 or i > 255:
            return False
    i = 0
    while i < len(data):
        leading_set_bits = get_leading_set_bits(data[i])
        if leading_set_bits == 0:
            i += 1
            continue
        if leading_set_bits == 1 or leading_set_bits > 4:
            return False
        for j in range(1, leading_set_bits):
            if i + j >= len(data):
                return False
            if get_leading_set_bits(data[i + j]) != 1:
                return False
        i += leading_set_bits
    return True
