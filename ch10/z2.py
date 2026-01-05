filename = 'learning_python.txt'

with open(filename) as object_file:
    for line in object_file:
        print(line.replace('Python', 'C').strip())
