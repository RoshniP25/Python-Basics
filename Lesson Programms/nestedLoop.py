print("\n===== NESTED LOOP =====")

#For-for nested loop
for i in range(1, 3):
    for j in range(1, 4):
        print(i, j, end=" ")
    print()

#nested loop for 2D list
matrix = [[1, 2], [3, 4]]
for row in matrix:
    for val in row:
        print(val, end=" ")
    print()

#generating combinations
colors = ["Red", "Blue"]
sizes = ["S", "M"]
for c in colors:
    for s in sizes:
        print(c, s)

print("\nInner loop runs fully for each outer loop iteration.\n")