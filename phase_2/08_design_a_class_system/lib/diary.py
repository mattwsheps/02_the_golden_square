class Diary:
    def __init__(self):
        """
        Side effects:
            Stores a list of DiaryEntry objects
        """
        self.entries = []

    def add(self, entry):
        """
        Parameters:
            entry: an instance of DiaryEntry
        Side effects:
            adds the entry to the list of entries
        """
        self.entries.append(entry)

    def all(self):
        """
        Returns:
            a list of all added entries
        """
        return self.entries