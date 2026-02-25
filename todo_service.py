class TodoService:
    def __init__(self, repository):
        self._repository = repository

    def add_task(self, task):
        # Validasi bisnis
        if not task or task.strip() == "":
            raise ValueError("Task tidak boleh kosong!")

        self._repository.add(task)
        return "Task berhasil ditambahkan."

    def get_all_tasks(self):
        return self._repository.get_all()

    def delete_task(self, index):
        result = self._repository.delete(index)
        if result is None:
            raise ValueError("Index tidak valid!")
        return "Task berhasil dihapus."
