print("===== FILTER GMAIL ACCOUNTS =====")

#Gmail lists
emails = [
    "john@gmail.com", "rita@yahoo.com", "alex@gmail.com",
    "tom@outlook.com", "sara@gmail.com"
]

print("gmail users: ")
#print only emails ending with gmail domain
for email in emails:
    if email.endswith("@gmail.com"):
        print(email)