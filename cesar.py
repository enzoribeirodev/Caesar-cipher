from string import ascii_lowercase


def caesar_cipher(msg: str, turns: int, encode: bool = True) -> str:
    """
    Encodes or decodes a string using the Caesar cipher method.
    
    Args:
        msg (str): The message to be processed.
        turns (int): The number of positions to shift.
        encode (bool): If True, encodes the message. If False, decodes it.
    
    Returns:
        str: The processed message.
    """
    result = []
    
    shift = turns if encode else -turns
    
    for char in msg:
        if char in ascii_lowercase:
            current_index = ascii_lowercase.index(char)
            
            new_index = (current_index + shift) % 26
            
            result.append(ascii_lowercase[new_index])
        else:
            result.append(char)

    return "".join(result)


