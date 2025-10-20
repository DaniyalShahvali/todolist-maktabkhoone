import pandas as pd

class Task:
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
    def __str__(self):
        return f"Name: {self.name}\nDescription: {self.description}\nPriority: {self.priority}"

    

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks.append(task)
            return f"We added your task sir."
        else:
            return f"we have this task in list."
        
    def del_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            return f"we deleted the task. ({task.name})"
        return f"Something happend that we do not know, try again!"
    
    def show_tasks(self):
        if not self.tasks:
            print("No task yet")
        for task in self.tasks:
            print(f"Task{self.tasks.index(task) + 1}:")
            print(task)

    def create_csv(self):
        names = []
        descriptions = []
        priorities = []
        for task in self.tasks:
            names.append(task.name)
            descriptions.append(task.description)
            priorities.append(task.priority)
        data_dict = {'Name' : names,
                     'Description' : descriptions,
                     'Priority' : priorities}
        df = pd.DataFrame(data_dict)
        df.to_csv('ToDoList.csv')
        print("Excel file has been created.")
    
    def upload_csv(self):
        try:
            file_name = input("Enter the file name: ")
            df = pd.read_csv(file_name)
            for line in df.values:
                uploaded_task = Task(name= line[1], description= line[2], priority= line[3])
                self.tasks.append(uploaded_task)
            print('We uploaded your tasks sir.')
        except FileNotFoundError:
            print(f"We couldn't find this file '{file_name}'")

        
# task1 = Task("Zaban", "We have an exam", "High")
# task2 = Task("Math", "We have question", "medium")

# todolist = ToDoList()

# print(todolist.add_task(task1))
# print(todolist.add_task(task2))

# todolist.show_tasks()

# print(todolist.del_task(task2))
# todolist.show_tasks()


def hello():
    print("Wlcome to TODoList.")

def user_input():
    return int(input("-------------------------\n1) Add a task\n2) Delete a task\n3) Show a tasks\n4) Export excel\n5) Upload a CSV file\n6) Eixt\n-------------------------\n"))
main = True
while main == True:
    todolist = ToDoList()
    hello()
    for i in range(100):
        a = user_input()
        if a == 1:
            name = input("Give a name for your task: ")
            description = input("Give a description: ")
            priority = input("What is the priority (High, Medium, Low): ")
            while priority.lower not in ['high', 'medium', 'low']:
                priority = input("What is the priority (High, Medium, Low): ")
            task1 = Task(name= name, description= description, priority= priority.lower)
            print(todolist.add_task(task1))
        if a == 2:
            idx_task = int(input("Which task do you want to delete?\n"))
            task = todolist.tasks[(idx_task-1)]
            print(task)
            print(todolist.del_task(task))
        if a == 3:
            todolist.show_tasks()
        if a == 4:
            todolist.create_csv()
        if a == 5:
            todolist.upload_csv()
        if a == 6:
            print('GoodBye Sir.')
            main = False
            break
        
