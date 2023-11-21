from math import ceil

class Diary:
    def __init__(self):
        self.entries = []
        self.word_count = 0
        self.mins_reading = 0

    def add(self, entry):
        # Parameters:
        #   entry: an instance of DiaryEntry
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the entry to the entries list
        self.entries.append(entry)

    def all(self):
        # Returns:
        #   A list of instances of DiaryEntry
        return self.entries

    def count_words(self):
        # Returns:
        #   An integer representing the number of words in all diary entries
        # HINT:
        #   This method should make use of the `count_words` method on DiaryEntry.
        for entry in self.entries:
            self.word_count += entry.count_words()
        return self.word_count

    def reading_time(self, wpm):
        # Parameters:
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        # Returns:
        #   An integer representing an estimate of the reading time in minutes
        #   if the user were to read all entries in the diary.
        if len(self.entries) == 0:
            raise Exception('No entries added yet.')
        self.word_count = self.count_words()
        return ceil(self.word_count / wpm)
            

    def find_best_entry_for_reading_time(self, wpm, minutes):
        # Parameters:
        #   wpm:     an integer representing the number of words the user can
        #            read per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   An instance of DiaryEntry representing the entry that is closest to,
        #   but not over, the length that the user could read in the minutes
        #   they have available given their reading speed.
        if len(self.entries) == 0:
            raise Exception('No entries added yet.')
        no_of_readable_words = wpm * minutes
        closest_word_count = 0
        closest_entry = None
        for entry in self.entries:
            current_entry_word_count = entry.count_words()
            if current_entry_word_count <= no_of_readable_words:
                if current_entry_word_count > closest_word_count:
                    closest_word_count = current_entry_word_count
                    closest_entry = entry
        return closest_entry
