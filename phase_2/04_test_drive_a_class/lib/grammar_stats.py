class GrammarStats:
    def __init__(self):
        self.check_list = []

    def check(self, text):
        # Parameters:
        #   text: string
        # Returns:
        #   bool: true if the text begins with a capital letter and ends with a
        #         sentence-ending punctuation mark, false otherwise
        check_bool = text[0].isupper() and text[-1] in '.?!'
        self.check_list.append(check_bool)
        return check_bool

    def percentage_good(self):
        # Returns:
        #   int: the percentage of texts checked so far that passed the check
        #        defined in the `check` method. The number 55 represents 55%.
        good_no = self.check_list.count(True)
        return (good_no / len(self.check_list)) * 100