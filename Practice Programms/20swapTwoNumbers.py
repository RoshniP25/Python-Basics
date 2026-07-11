print("=== SWAP TWO NUMBERS")

#taking input
a = (int(input("Enter First Number (a): ")))
b = (int(input("Enter Second Number (b): ")))

print("\nBefore swapping: a =", a, ", b=", b)

#swapping using a temporary variable
temp = a
a = b
b = temp

print("\nAfter swapping: a =", a, ", b=", b)
