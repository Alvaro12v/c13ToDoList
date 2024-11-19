class Task:
    def __init__(self,description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        status = "completado" if self.completed else "pendiente"
        return f"{self.description} - {status}"



class ToDoList:
    pass

def main():
    pass


if __name__ == "__main__":
    main()





