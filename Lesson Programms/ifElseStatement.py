print("\n==== IF-ELSE STATEMENT IN PYTHON =====")

#even or odd
n = int(input("Enter a number: "))
if n % 2 == 0:
    print("Even")
else :
    print("Odd")

#voting eligibility
age = int(input("\nEnter your age: "))
if age >= 18:
    print("Eligible")
else :
    print("Not eligible")

#temperature umber
a = int(input("\nEnter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("First id greater")
else :
    print("Second is greater or equal")

print("\nIF-ELSE executes only one block.\n")