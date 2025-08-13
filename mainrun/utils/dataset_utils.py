
def pad_sequence(words, context_size, pad_mode="cyclic_padding", pad_token="<pad>", align="left"):
    """
    Pad the fixed length sequence to context_size with specified padding mode.
    Args:
        words (list): sequence of words to pad
        context_size (int): the desired length of the padded context
        pad_mode:
        - cyclic_padding (default): repeat the sentence tokens cyclically to reach context_size
        - edge_padding  : repeat boundary token (first for left, last for right)
        - token_padding   : use pad_token
        align: 'left' or 'right' where to place the original words relative to padding
    """
    len_words = len(words)
    pad_amount = context_size - len_words
    
    if pad_amount == 0:
        return words[:context_size]

    if pad_mode == "cyclic_padding":
        padded_seq = (words * ((context_size + len_words - 1) // len_words))[:context_size]
        return padded_seq

    elif pad_mode == "edge_padding":
        filler = [words[0]] * pad_amount if align == "left" else [words[-1]] * pad_amount
        return (filler + words) if align == "left" else (words + filler)

    elif pad_mode == "token_padding":
        filler = [pad_token] * pad_amount
        return (filler + words) if align == "left" else (words + filler)
    else:
        raise ValueError(f"Unknown pad_mode: {pad_mode}. Supported modes: cyclic_padding, edge_padding, and token_padding.")    

