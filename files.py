my_file = open("kalyn.txt", "a")

# print(my_file.readlines())

#print( "hello")
#print("world")

my_file.writelines('im writing from python\n')

my_file.close()

my_file = open("kalyn.txt")

for line in my_file.readlines():
    print(line, end="")
