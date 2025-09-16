
try:
    files = input('enter a file name : ')
    with open(files,'r') as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print('file not existing')
