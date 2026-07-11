print("\n===== BASIC OOP STRUCTURE =====")

class Student:

    school_name = "Bright Future School"  #class variable

    #constructor
    def __init__(self, name, age):
        self.name = name     #instance variable
        self.age = age

    #instance method
    def display(self):
        print("School:", Student.school_name)
        print("Name:", self.name)
        print("Age:", self.age)

    #another instance method
    def is_adult(self):
        return self.age >= 18

    #class method
    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    #static method
    @staticmethod
    def course_info():
        print("Course: Advanced Python Programming")

#creating objects
s1 = Student("Alice", 20)
s2 = Student("Bob", 16)

s1.display()
print("Is Adult:", s1.is_adult())

print()
s2.display()
print("Is Adult:", s2.is_adult())

print("\n===== USING CLASS METHOD =====")
Student.change_school("Global Public School")

s1.display()
print()
s2.display()

print("\n===== USING STATIC METHOD")
Student.course_info()