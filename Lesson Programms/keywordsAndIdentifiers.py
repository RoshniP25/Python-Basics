import keyword

#========KEYWORDS=========
print("======Keywords in Python======")
print("Some keywords are:", keyword.kwlist[:10])
print("Total number of keywords:", len(keyword.kwlist), "\n")

#============IDENTIFIERS==========
print("======Identifiers in Python======")

name = "Alice"
age1 = 21
_student = "John"
print("valid identifiers:", name, age1, _student)

city = "Mumbai"
City = "Delhi"
print("\ncity:", city)
print("City:" , City)

print("\nCheck if a word is Identifier or keyword:")
words = ["name", "2abc", "class", "value_1"]
for w in words:
    print(w, "-> isidentifier?", w.isidentifier(), "| is keyword?", keyword.iskeyword(w))
