def reading_time_estimator(text):
    """Estimates the reading time for a text, assuming reader reads 200 words per min

    Parameters:
        text: a string consisting of wordy text

    Returns:
        a float representing the reading time in minutes
    """
    if text == "":
        raise Exception("Can't estimate reading time for an empty text.")
    word_list = text.split()
    word_no = len(word_list)
    return word_no / 200