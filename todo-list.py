list = []

# todo = input("Enter a task : ").lower
print(list)
# list.append(todo)

add = input('Do you want to add task ? (Y/N) : ').upper()
if add == 'Y':
    task = input('Enter the task : ').lower()
    list.append(task)
    print(list)
delete = input('Do you want to delete task ? (Y/N) : ').upper()
if delete == 'Y':
    task = input('Enter task want to delete : ').lower()
    if task in list:
        list.remove(task)
        print(list)
mark_done = input('Do you want to mark done task ? (Y/N) : ').upper()
if mark_done == 'Y':
    task = input('Enter task want to delete : ').lower()
    if task in list:
        list.remove(task)
        print('Task Completed')