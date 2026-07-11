print("===== EMAIL CLEANING & CATEGORIZATION =====")

emails = [
    " john@gmail.com ", "RITA@Yahoo.com", "alex@gmail.com",
    " tom@outlook.com", "sara@GMAIL.com"
]

cleanedEmails = []       # will store trimmed, lowercase emails
gmailUsers = []          # will store only gmail users
others = []               # any other domain

for mail in emails:
    clean = mail.strip().lower()
    cleanedEmails.append(clean)

    if clean.endswith("@gmail.com"):
        gmailUsers.append(clean)
    else:
        others.append(clean)

print("\nAll cleaned Emails:", cleanedEmails)
print("Gmail users:", gmailUsers)
print("Other DOMAINS:", others)