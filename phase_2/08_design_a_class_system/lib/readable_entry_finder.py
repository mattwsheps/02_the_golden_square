class ReadableEntryFinder:
    def __init__(self, wpm, minutes):
        """
        Parameters:
            wpm: an int representing reading speed in words per min
            minutes: an int representing the minutes available to the reader
        """
        self.wpm = wpm
        self.minutes = minutes

    def find_entry(self, diary):
        """
        Parameters:
            diary: an instance of a diary
        Returns:
            an entry to read based on reading speed and time available
        """
        if len(diary.entries) == 0:
            raise Exception('No entries added yet.')
        no_of_readable_words = self.wpm * self.minutes
        closest_word_count = 0
        closest_entry = None
        for entry in diary.entries:
            current_entry_word_count = entry.count_words()
            if current_entry_word_count <= no_of_readable_words:
                if current_entry_word_count > closest_word_count:
                    closest_word_count = current_entry_word_count
                    closest_entry = entry
        return closest_entry