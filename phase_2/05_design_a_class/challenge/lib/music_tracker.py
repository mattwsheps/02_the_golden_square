class MusicTracker():
    def __init__(self):
        """
        Side effects:
            Stores the added tracks in a list
        """
        self.track_list = []

    def add(self, track):
        """
        Parameters:
            track: a string representing the name of a track that has been listened to

        Side effects:
            Adds the given track to a list
        """
        if track == "":
            raise Exception('Input string cannot be empty.')
        if type(track) != str:
            raise Exception('Input must be a string.')
        self.track_list.append(track)

    def show_tracks(self):
        """
        Returns:
            the list of tracks that have been listened to
        """
        return self.track_list