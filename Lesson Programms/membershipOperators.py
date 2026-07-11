#Membership operators help check if the value exists inside sequence
#operators:  'in'  -> true if value exists
#             'not in' -> True if value does NOT exits

#String example
text = "python programming"
print("'p' in text:", 'p' in text)  #checks character
print("'java' not in text:", 'java' not in text) #substring not found

#list example
fruits = ["apple", "banana", "cherry"]
print("'banana' in fruits:", 'banana' in fruits) #element exists

#-tuple example
nums = (10, 20, 30)
print("20 in nums:", 20 in nums) #tuple memberships checks

#dictionary example
student = {"name": "John", "age": 23}
print("'name' in student:", 'name' in student ) #cheks keys only

#set example
colors = {"red", "green", "blue"}
print("'yellow' not in colors:", 'yellow' not in colors) #fast lookup
#user input example
word = input("Enter  word: ")
if 'a' in word:
    print("The letter 'a' is present.")
else:
    print("The letter 'a' is not present.")

print("\nUse 'in' or 'not in' to test membership in strings, lists, tuples, sets and dictionary.")