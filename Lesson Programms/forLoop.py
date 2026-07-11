print("\nFOR LOOP IN PYTHON====")

#range()
for i in range(3):
    print(i, end=" ")

#list
print("\n")
for fruit in ["Apple", "Banana"]:
    print(fruit, end=" ")

#print 1 to 5
for i in range(1, 6):
    print(i, end=" ")

#print characters of a string
print("\n")
for ch in "PYTHON":
    print(ch, end=" ")

#print a multiplication table
n = int(input("\n\nEnter a number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n * i)

print("\nFor loop used to iterate over sequences and ranges.\n")