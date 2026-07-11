print("\n===== CONTROL FLOW IN PYTHON====")

#typed of control flow
print("1. Conditional Statements -> if, elif, else")
print("2. Looping Statement      -> for, while")
print("3. Jump Statement          -> break, continue, pass\n")

#Example values
temperature = 30
count = 3
weather = "sunny"

#conditipnal example
if weather == "sunny":
    print("Bright Day!")
elif weather == "rainy":
    print("Carry Umbrella.")
else:
    print("Stay Warm.")

#looping statement
print("\nNumbers 1 to 5:")
for i in range(1, 6):
    print( i, end=" ")

print("\nCountdown:")
while count > 0:
    print(count, end= " ")
    count -=1

# jump statment
print("\n\nJump Statements demo: ")
for i in range(1, 6):
    if i == 2:
        continue
    if i == 4:
        break
    print("Number:", i)

#pass statement
for j in range(3):
    pass

print("\nControl flow  helps Python make decision and repeat tasks!.\n")