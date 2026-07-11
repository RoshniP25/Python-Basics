#creating sets
nums = {10, 20, 30}
mixed = {10, "Python", 3.14}
empty = set()
dup = {1,2,2,3}

print(nums, mixed, empty, dup)

#adding and removing
fruits = {"apple", "mango", "banana"}
fruits.add("orange")
fruits.remove("banana")
fruits.discard("grapes")
print(fruits)

item = fruits.pop()
print("Popped: ", item)

#set operations
A = {1, 2, 3, 4}
B = {3, 4, 5}

print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(A.symmetric_difference(B))

#relationship methoods
print(A.issubset(B))
print(A.issuperset(B))
print(A.isdisjoint(B))

#update() and copoy()
A.update(B)
print(A)
A.update(B)
print(A)
