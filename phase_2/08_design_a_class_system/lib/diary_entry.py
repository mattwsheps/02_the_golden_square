class DiaryEntry:
    def __init__(self, title, contents):
        """
        Parameters:
            title: a string representing the title of the diary entry
            contents: a string representing the contents of the diary entry
            contents_list: a list where each element is a word in the      contents string
        """
        self.title = title
        self.contents = contents
        self.contents_list = self.contents.split()

    def count_words(self):
        """
        Returns:
            an integer representing the number of words in the contents
        """
        return len(self.contents_list)
