print("\n==== IF STATEMENT IN PYTHON====")

#Example 1 : Basic IF
age= int(input("Enter your age:"))
if age >= 18:
    print("Eligible to vote.")

#Example 2: Temperature check
temp = float(input("\nEnter temperature: "))
if temp > 30:
    print("It's hot today.")

#example 3 Boolean condition
is_student = True
if is_student:
    print("\nStudent discount available.")

#Example 4: Independent IF's
marks = int(input("\nEnter marks: "))
if marks >= 90: print("Grade A+")
if marks >= 75: print("Grade A")
if marks >= 60: print("Grade B")
if marks >= 40: print("Grade C")
if marks > 40: print("Fail")

#Example 5: even/odd
num = int(input("Enter a number"))
if num % 2 == 0: print("Even number")
if num % 2 != 0: print("Odd number")

print("\nIF executes only when condition is true,\n")