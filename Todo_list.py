from tabulate import tabulate
'''
Todo Application: 
Options: 
1. Add a Todo 
2. Display all the todos 
3. mark a todo as completed 

structure of todo: 
Id -> we can use to uniquely identify a todo 
Title -> title 
description 
status -> completed/pending 
'''
def add_todo(todo: dict[str]):
    todos.append(todo)
    print("Todo added succesfully..")
    
def completed(todo: dict[str]):
    todo["status"] = "completed"
    print("Marked as completed...")
    
def search(tid: int) -> dict[str]: 
    if len(todos) == 0:
        return None 
    else: 
        for todo in todos: 
            if todo['id'] == tid:
                return todo 
        return None 

def get_table():
    headers = ["ID","Title","Description","Status"]
    rows = [] 
    for todo in todos: 
        row = list(todo.values())
        rows.append(row)
    table = tabulate(rows,headers=headers,tablefmt="grid")
    return table 
    
def display():
    table = get_table()
    print(table)

options = """Options: 
1. Add a Todo 
2. Display all the todos
3. Mark a todo as completed
4. Exit 
"""
todos = [] 
tid = 0 
while True: 
    print("Todo Application")
    print(options)
    choice = int(input("Enter your choice: "))
    match choice: 
        case 1: 
           print("Adding Todo: ")
           tid += 1 
           title = input("Title: ")
           description = input("Description: ")
           status = "pending"
           # single todo 
           todo = {"id":tid,"title": title,"description": description,"status":status}
           add_todo(todo)
        case 2:
            print("Displaying Todos: ")
            display()
        case 3: 
            print("Marking Todo as completed: ")
            target_id = int(input("Enter todo ID: "))
            todo = search(target_id)
            if todo == None: 
                print(f"Todo with ID {target_id} is not found.")
            else: 
                completed(todo)
        case 4:
            print("Exiting...")
            break 
        case _: 
            print("Invalid option.Try again.")
    print("="*20)  

