print("===== FILE HANDLING DEMO =====")

with open("notes.txt", "w") as file:
    file.write("This is a sample note.\nLearning Python is fun")

with open("notes.txt", "r")as file:
    content = file.read()

print("File Content:\n", content)