print("===== ODD NUMBERS GRID ====")

num = int(input("Enter a number: "))

for i in range(1, num + 1):
    for j in range(1, num + 1):
        if j % 2 == 0:
            continue
        print(j, end=" ")
    print()