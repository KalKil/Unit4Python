class person:
    species = 'Homosapian'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def hi(self):
        print("Hi my name is " + self.name)

    def hello(self):
        print("Hello World")

kalyn = person("kalyn", 17)
print(kalyn.name)
print(kalyn.age)

ansu = person("ansu", 17)
print(ansu.name)
print(ansu.age)

kalyn.hi() # -> "hi my name is Kalyn"

ansu.hi() # -> "hi my name is Kalyn"