#-------Basic print----
from main import height

print("Hello, World!")
print("Numbers:", 10,20,30)   #multiple values
print()    #blank line

#-----print() with sep and end---------
print("A", "B", "C", sep="-")   #custom separator
print("Line without newline->", end=" ")
print("continues same line")

#basic input
name = input("\nEnter your name: ")
print("Hi,", name + "!")


#------type casting----
age = int(input("Enter your age: "))
height= float(input("Enter your height in meters: "))
print("Age:", age, "| height:", height)

#-----multiple inputs---
a,b= input("Enter two integers separated by space: ").split()
a,b = int(a), int(b)
print("Sum=", a +b)


#-handling empty input-
color = input("Favourite color (press Enter to skip): ").strip()
if color == "":
    color = "Not provided"
print ("Color:", color)

#-----formatted output
item, price, qty = "Book", 120.5, 2
print(f"using f-string ->{item}, {price}, {qty}, Total = {price * qty: .2f}")

#--------escape sequence
print("Newline ->\\n\nTab ->\\t\tExample\t Tab")