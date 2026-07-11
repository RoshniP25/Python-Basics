print("==== STUDENT CLASS DEMO =====")

class Student:
    def __init__(self,name ,marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

s1 = Student("Asha", 85)
s2= Student("Rohit", 92)

s1.display()
s2.display()