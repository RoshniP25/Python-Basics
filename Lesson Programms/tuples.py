#creating tuples
nums = (1, 20, 30)
mixed = (10, "Python", 3.14)
single = (5,)
nested = (1,2, (3,4))

#accessing elements
fruits = ("apple", "banana", "mango")
print(fruits [0], fruits[-1])
print(fruits[1:3], fruits[::-1])

#immutability example
t = (1,2,3)
new_t = t + (4,5)
print(new_t)

#tuple methods
vals = (10, 20, 10, 30)
print(vals.count(10))
print(vals.index(30))
