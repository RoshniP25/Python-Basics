def greet():
    print("Hello from a function")

def add (a, b):
    return a + b

def info(name, course="Python"):
    print(name, course)

def total(*nums):
    return sum(nums)

def details (**data):
    print(data)

x = 10
def show():
    x = 5
    print(x)

y = 20
def change():
    global y
    y = 50

greet()
print(add(3, 4))

info("John")
info(name="Asha", course="Java")
print(total(10, 20, 30))
details(city = "Mumbai", age = 23)

show()
print(x)

change()
print(y)