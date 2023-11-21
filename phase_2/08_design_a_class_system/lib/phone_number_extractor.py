class PhoneNumberExtractor:
    def __init__(self):
        self.list = []
        pass

    def extract_all(self, diary):
        """
        Parameters:
            diary: An instance of Diary
        Returns:
            A list of strings representing phone numbers that can be found in the diary entries
        """
        for entry in diary.entries:
            for word in entry.contents_list:
                if word[:2] == '07':
                    if word[:11] not in self.list:
                        self.list.append(word[:11])
        return self.list
