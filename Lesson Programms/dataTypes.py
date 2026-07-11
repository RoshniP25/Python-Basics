import sys

#basic data types
integerVar = 10
floatVar = 3.14
complexVar = 2 + 5j
stringVar = "Hello Python"
boolVar = True
noneVar = None
listVar = [1, 2, 3]
tupleVar = (1, 2, 3)
setVar = {1, 2, 3}
dictVar = {"one": 1, "two": 2}

print("Integer:", type(integerVar))
print("Float:", type(floatVar))
print("Complex:", type(complexVar))
print("String:", type(stringVar))
print("Boolean:", type(boolVar))
print("None:", type(noneVar))
print("List:", type(listVar))
print("Tuple:", type(tupleVar))
print("Set:", type(setVar))
print("Dictionary:", type(dictVar))

#storage information
print("\n------Data Types Sizes------")
print("Boolean:", sys.getsizeof(boolVar), "bytes")
print("Integer:", sys.getsizeof(integerVar), "bytes")
print("Float:", sys.getsizeof(floatVar), "bytes")
print("Complex:", sys.getsizeof(complexVar), "bytes")
print("String:", sys.getsizeof(stringVar), "bytes")
print("None:", sys.getsizeof(None), "bytes")