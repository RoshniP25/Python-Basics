print("===== SERVICE ELIGIBILITY CHECKER =====")

age = int(input("enter your age: "))
citizen = input("Are you an Indian citizen? (yes/no): ").lower()

if age >= 18 and citizen =="yes":
    print("You are eligible to apply.")