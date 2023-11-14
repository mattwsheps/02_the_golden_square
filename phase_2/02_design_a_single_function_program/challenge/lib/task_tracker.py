def task_tracker(text):
    """
    A function that checks if '#TODO' is in a given text

    Parameters:
        text: a string of text

    Returns:
        A boolean where True means #TODO is in the text and False means it isn't
    """
    if text == "":
        raise Exception("Input text cannot be empty.")
    return '#TODO' in text