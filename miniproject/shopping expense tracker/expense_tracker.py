def add_item():
    with open('shopping.txt','a') as f:
        item_name = input('enter item name : ')
        item_quantity = int(input('enter item quantity : '))
        item_price = int(input('enter item price per unit : '))

        data = f'{item_name},{item_quantity},{item_price}'
        f.write(data+'\n')

def view_items():
    with open('shopping.txt','r') as f:
        items = f.readlines()

        for line in items:
            parts = line.strip().split(',')
            if len(parts) == 3:
                name,quantity,price = parts

                print()
                print(f'item name : {name}')
                print(f'item quantity : {quantity}')
                print(f'item prices per unit : {price}')
                print()

def calculate_item():
    with open('shopping.txt','r') as f:
        data = f.readlines()

        total = 0
        for line in data:
            parts = line.strip().split(',')
            
            if len(parts) == 3:
                name,quantity,price = parts
                total +=float(price)
                print()
        print(f'total price : {total}')
        print()

while True:
    print('1. Add an item')
    print('2. View all items')
    print('3. Calculate total expenses')
    print('4. Exit the program')

    choice = input('enter the choice : ')

    if choice == '1':
        add_item()
    elif choice == '2':
        view_items()
    elif choice == '3':
        calculate_item()
    elif choice == '4':
        break