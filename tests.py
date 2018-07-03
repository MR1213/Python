
x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    age = 10
    height = 1.5
    name = "Maksym"

list = [Person("Maksym", 10, 1.5), Person("Masha", 4, 1)]

for p in list:
    print("Name: " + p.name)
    print("Age: " + str(p.age))
    print("Height: " + str(p.height))
    print("---------------------------------")