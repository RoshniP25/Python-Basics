print("\n===== WHILE LOOP =====")
#counting 1 to 5
i = 1
while i <= 5:
    print(i, end="")
    i += 1

#countdown
print("\n")
x = 5
while x > 0:
    print(x, end=" ")
    x -= 1

#repeat with correct pass
print("\n")
pwd = ""
while pwd != "python": pwd = input("Enter password: ")
print("Access Granted")

#sum of N natural no.
print()
n = int(input("Enter a number:"))
sum_n, j = 0, 1
while j <= n:
    sum_n += j
    j += 1
print("Sum:", sum_n)
print("\nWhile loop repeats as long as the condition remains true.\n")