#!/usr/bin/python3
"""
UTF-8 Validation
"""
def validUTF8(data):
    """
    Determine if a given dataset represents a valid UTF-8 encoding.
    
    :param data: List of integers representing 1 byte of data each
    :return: True if data is a valid UTF-8 encoding, False otherwise
    """
    num_follows = 0

    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000
    
    for num in data:
        mask = 1 << 7
        
        """
        Determine number of following bytes
        """
        if num_follows == 0:
            while mask & num:
                num_follows += 1
                mask = mask >> 1
            
            """
            Handle 1-byte characters (0xxxxxxx)
            """
            if num_follows == 0:
                continue
            
            """
            Handle multi-byte characters
            """
            if num_follows == 1 or num_follows > 4:
                return False
        else:
            """
            Check if current byte is a continuation byte (10xxxxxx)
            """
            if not (num & mask1 and not (num & mask2)):
                return False
            
            num_follows -= 1
    
    return num_follows == 0
