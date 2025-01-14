class Task:
    def __init__(self,description):
        self.description = description
        self.completed = False

    def complete(self):
        self.completed = True #Agregamos comentario para hacer otra prueba

    def __str__(self):
        estado = "completado" if self.completed else "pendiente"
        return f"{self.description} - {estado}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task (self,description):
        task = Task(description)
        self.tasks.append(task)

def main():
    pass


if __name__ == "__main__":
    main()





