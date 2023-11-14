def count_words(string):
    if type(string) != str:
        raise Exception('The input you provide must be a string.')
    string_list = string.split()
    return len(string_list)