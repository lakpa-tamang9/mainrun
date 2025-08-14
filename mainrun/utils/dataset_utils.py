import re

kwargs = {
    "pad_mode": "cyclic_padding",  # default padding mode
    "pad_token": "<pad>",           # default padding token
    "align": "left"                 # default alignment for padding
}
def pad_sequence(words, context_size, **kwargs):
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

    if kwargs["pad_mode"] == "cyclic_padding":
        padded_seq = (words * ((context_size + len_words - 1) // len_words))[:context_size]
        return padded_seq

    elif kwargs["pad_mode"] == "edge_padding":
        filler = [words[0]] * pad_amount if kwargs["align"] == "left" else [words[-1]] * pad_amount
        return (filler + words) if kwargs["align"] == "left" else (words + filler)

    elif kwargs["pad_mode"] == "token_padding":
        filler = [kwargs["pad_token"]] * pad_amount
        return (filler + words) if kwargs["align"] == "left" else (words + filler)
    else:
        raise ValueError(f"Unknown pad_mode")    



def sliding_window(titles, context_size,
):
    """
    Returns list of text contexts of length = context_size.
    Args:
        titles (list): list of titles to process
        context_size (int): size of the sliding window
    """
    contexts = []
    for title in titles:
        words = re.sub(r"\s+", " ", title.strip()).split()
        len_words = len(words)
        if len_words == 0:
            continue

        if len_words < context_size:
            ctx_words = pad_sequence(words, context_size, **kwargs)
            contexts.append(" ".join(ctx_words))
        else:
            for i in range(len_words - context_size + 1):
                contexts.append(" ".join(words[i:i + context_size]))
    return contexts

