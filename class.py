class person:
    species = 'Homosapian'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self):
        print("Hi my name is " + self.name)

    def hello(self):
        print("Hello World")

class student(person):
    role = 'student'

class teacher(person):
    role = 'teacher'

    def hi(self):
        print("Hi my name is Mx." + self.name)


forlenza = teacher("forlenza", 184)
print(forlenza.role)

forlenza.hi()

kalyn = student("kalyn", 17)
print(kalyn.name)
print(kalyn.age)

ansu = student("ansu", 17)
print(ansu.name)
print(ansu.age)

kalyn.hi() # -> "hi my name is Kalyn"

ansu.hi() # -> "hi my name is Kalyn"