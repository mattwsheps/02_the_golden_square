def grammar_improver(text):
    """
    A function that validates if a text starts with a capital letter and ends with a suitable-ending punctuation mark

    Parameters: 
        text: a string of the text to be verified

    Returns:
        A boolean which is True if the text is grammatically valid and False if not.
    """
    return text[0].isupper() and text[-1] in '.?!'
