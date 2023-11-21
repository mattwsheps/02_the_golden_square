class TaskList:
    def __init__(self):
        """
        Side effects:
            Stores a list of strings representing tasks
        """
        self.list = []

    def add(self, task):
        """
        Parameters:
            task: a string representing a task to complete
        Side effects:
            Adds the task to the list of tasks
        """
        self.list.append(task)

    def incomplete(self):
        """
        Returns:
            A list of task instances representing the tasks that are not complete
        """
        return [task for task in self.list if not task.complete]

    def complete(self):
        """
        Returns:
            A list of task instances representing the tasks that are complete
        """
        return [task for task in self.list if task.complete]

    def give_up(self):
        """
        Returns:
            Nothing
        Side-effects:
            Marks all tasks as complete
        """
        for task in self.list:
            if not task.complete:
                task.mark_complete()