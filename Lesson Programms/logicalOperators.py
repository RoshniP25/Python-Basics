print("\n=====LOGICAL OPERATORS IN PYTHON =====")

#example values
a, b, c = 10, 20, 5
print("Using a=", a, ", b =", b, ", c =", c ,"\n")

#logical and
print("a > b and b > c ->", (a > b) and (b > c))

#logical OR
print("a > b or b > c ->", (a > b) or (b > c))

#logical NOT
print("not(a > b) ->", not(a > b))

#combined expression
print("(a > b) or (a < c and b > c) ->", (a > b) or (a < c and b > c))

#boolean value
x , y = True, False
print("\nBoolean Examples:")
print("x and y ->", x and y)
print("x or y ->", x or y)
print("not x ->", not x)

#user input
num = int(input("\nEnter a number: "))

if num > 0 and num < 10:
    print("Number is betweeen 1 and 9.")
elif num <= 0 or num >= 10:
    print("Number is not in the range 1-9.")