print("-----Implicit TypeConversion-----")
numInt = 10
numfloat = 3.5

#int is automatically converted into f;loat during arithmativ operation
result = numInt + numfloat

print("Value of result:", result)
print("Type of result:", type(result))

print("-----Explicit TypeConversion-----")

floatNum = 9.99
intNum = int(floatNum)
print("Float:", floatNum, "| After int():", intNum)

age = 21
ageStr = str(age)
print("Integer:", age, "| After str(age):", ageStr, "| Type:", type(ageStr))

strNumber = "45.67"
floatNumber = float(strNumber)
print("String:", strNumber, "| After float():", floatNumber, "| Type:", type(floatNumber))