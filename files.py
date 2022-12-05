my_file = open("kalyn.txt", "r+")


for line in my_file.readlines():
    print(line, end="")

#print( "hello")
#print("world")

my_file.writelines(['im writing from python'])