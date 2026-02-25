class TodoCLI:
    def __init__(self, service):
        self._service = service

    def run(self):
        print("=== To-Do List App ===")

        while True:
            command = input("\nCommand (add/list/delete/exit): ")

            if command == "add":
                task = input("Masukkan task: ")
                try:
                    message = self._service.add_task(task)
                    print(message)
                except ValueError as e:
                    print(f"Error: {e}")

            elif command == "list":
                tasks = self._service.get_all_tasks()
                if not tasks:
                    print("Belum ada task.")
                else:
                    for i, task in enumerate(tasks):
                        print(f"{i+1}. {task}")

            elif command == "delete":
                try:
                    index = int(input("Nomor task yang mau dihapus: ")) - 1
                    message = self._service.delete_task(index)
                    print(message)
                except ValueError as e:
                    print(f"Error: {e}")

            elif command == "exit":
                print("Goodbye 👋")
                break

            else:
                print("Command tidak dikenal!")
