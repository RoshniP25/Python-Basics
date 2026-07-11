print("\n===== LOOP ELSE =====")

#for loop search example
nums = [2, 4, 6, 8]
for n in nums:
    if n == 5:
        print("Found 5")
        break
else:
    print("5 not found in list")

#while loop example
print()
x = 3
while x >0:
    print(x, end=" ")
    x -= 1
else:
    print("\nCountdown Finished")

users=["Roshni","Divya", "Akshaya"]
target = "Roshni"
for user in users :
   if user == target:
       print("User found")
       break
else:
     print("User not found")

print("\nElse runs only when loop completes without break.\n")