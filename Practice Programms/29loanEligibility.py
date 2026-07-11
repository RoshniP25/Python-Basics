print("====== LOAN ELIGIBILITY CHECK======")

salary = float(input("Enter your monthly salary: "))
cibil = int(input("Enter your cibil score: "))

if salary >= 30000 and cibil >= 700:
    print("Loan Approved.")
else:
    print("Not approved.")
    