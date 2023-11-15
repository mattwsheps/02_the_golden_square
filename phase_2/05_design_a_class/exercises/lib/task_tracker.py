class TaskTracker:
    def __init__(self):
        """
        Side effects: stores a list of the incomplete tasks
        """
        self.task_list = []

    def add(self, task):
        """
        Parameters:
            task: a string representing a task
        Side effects:
            Adds the given task to a list
        """
        self.task_list.append(task)

    def list_tasks(self):
        """
        Returns:
            A list of the incomplete tasks.
        """
        return self.task_list

    def mark_complete(self, index):
        """
        Parameters:
            index: an integer representing the task to complete
        Side effects:
            removes the completed task from the list
        """
        if index > len(self.task_list)-1 or index < 0:
            raise Exception('The given index is outside of the task lists range.')
        self.task_list.pop(index)