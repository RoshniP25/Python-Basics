#creating dictionaries
student = {"name": "Aditya", "age": 23, "course": "CS"}
person = dict(name="Sneha", age = 21)
empty = {}
school = {"s1": {"name": "Asha", "marks": 82}}

print(student, person, empty, school)

#accessing values
print(student["name"])
print(student.get("course"))
print(student.get("phone", "Not provided"))

print(list(student.keys()))
print(list(student.values()))
print(list(student.items()))

#adding and updating
student["phone"] = "98765"
student["age"] = 24
student.update({"city": "Pune"})
student.setdefault("dept", "Engineering")
print(student)

#removing elements
student.pop("phone", None)
student.popitem()
if "city" in student:
    del student["city"]
print(student)

#iterating
emp = {"id": 101, "name": "Rina", "role": "Engineer"}
for k in emp: print(k)
for v in emp.values(): print(v)
for k , v in emp.items(): print(k, v)

#nested dictionaries
company = {"d1": {"manager": "Amit"}}

print(company["d1"]["manager"])

text = input("Enter text: ").split()
freq = {}
for w in text:
    freq[w] = freq.get(w, 0) + 1
    print(freq)
