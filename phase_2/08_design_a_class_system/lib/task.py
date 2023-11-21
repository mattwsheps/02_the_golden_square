class Task:
    def __init__(self, task):
        """
        Parameters:
            task: a string representing a task
        """
        self.task = task
        self.complete = False
    
    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        if self.complete:
            raise Exception('This task is already complete.')
        self.complete = True