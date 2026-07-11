#creating strings
s1 = "Python"
msg = """Learning
Strings in Python"""

print(s1)
print(msg)

#indexing and slicing
print(s1[0], s1[-1])    #first and last character
print(s1[1:4], s1[::-1])     #slice and reverse

#useful methods
t = "  Hello Python  "
print(t.strip(), t.lower(), t.replace("Pyhton", "Java"))

#Formatting
name, age = "John", 23
print(f"{name} is {age} years old")     #f- string
print("Name: {}, age: {}.format(name, age)")     #Format()