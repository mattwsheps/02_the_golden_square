def make_snippet(string):
    if type(string) != str:
        raise Exception("Please input a string")

    split_string = string.split()
    
    first_five = [word for i, word in enumerate(split_string) if i < 5]
    
    if len(split_string) > 5:
        return " ".join(first_five) + "..."
    
    return " ".join(first_five)

