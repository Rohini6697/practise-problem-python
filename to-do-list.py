list = []

while True:
    print('TASK MENU : ')
    print()
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print()

    value = input('enter your choice : ')  
    if value == '1':
        print('Tasks : ',list)
    elif value == '2':
        task = input('Enter the task to add : ').lower()
        list.append(task)
        print('Task Added')
    elif value == '3':
        task = input('Enter the task wanted to delete : ').lower()
        list.remove(task)
        print('Task deleted')
    elif value == '4':
        task = input('Enter the task need to mark as done : ').lower()
        list.remove(task)
        print('Task Completed')