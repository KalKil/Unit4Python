todos = []

x = input ("what to add to list?  ")

todos.append(x)

print("your todo list is: ")
print (todos)

while True:
    print("Your todos are:")
    print(todos)

    x = input ("What todo would you like to add?")
    todos.append(x)
    
    my_file.writelines('x\n')

    my_file.close()

    my_file = open("kalyn.txt")

    for line in my_file.readlines():
        print(line, end="")

        my_file.writelines('')

