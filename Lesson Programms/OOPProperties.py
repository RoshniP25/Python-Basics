print("\n===== OOP FOUR PILLARS DEMO====")

#encapsulation + abstraction
class Employee:
    company_name = "Tech Solutions" #class variables

    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary #private variable (encapsulation)

    def get_salary(self):
        return self.__salary

    def work(self):          #method overridden
        print(self.name, "is working at", Employee.company_name)

#inheritance + polymorphism
class Manager(Employee):
    def work(self):
        print(self.name, "is working the team at", Employee.company_name)

#creating objects
emp = Employee("Ravi", 40000)
mgr = Manager("Sneha", 80000)

print("\n ==== Work Behaviour ====")
emp.work()
mgr.work()

print("\n--- Salary Access ---")
print("Employee Salary:", emp.get_salary())
print("Manager Salary:", mgr.get_salary())

print("\n---  Changing class variable ---")
Employee.company_name = "Global Tech"

emp.work()
mgr.work()