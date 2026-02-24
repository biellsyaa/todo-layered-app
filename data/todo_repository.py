class TodoRepository:
    def __init__(self):
        self._tasks = []

    def add(self, task):
        self._tasks.append(task)

    def get_all(self):
        return self._tasks

    def delete(self, index):
        if 0 <= index < len(self._tasks):
            return self._tasks.pop(index)
        return None