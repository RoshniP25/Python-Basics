print("\n==== ASSIGNMENT OPERATORS IN PYTHON ====")

#simple adignment
a = 10
print("Initial a=", a)

#arithmetic assignment operators
a += 5
a -= 3
a *= 2
a /= 4
a %= 3
print("After various arithmetic assignments, a=", a)

#floor division and exponent
a = 10
a //= 3
a **= 2
print("After floor division and exponent assignments, a=", a)

#bitwise assignment
a = 5
a &= 3
a |= 2
a ^= 1
a <<= 1
a >>= 2
print("Final value after bitwise assignments, a=", a)

#user input example
x = int(input("\nEnter a nmber: "))
x += 10
x *= 2
x //= 5
print("Final x after assignment operations =", x)
