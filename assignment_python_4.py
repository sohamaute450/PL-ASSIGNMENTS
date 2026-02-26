class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_person_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Employee(Person):
    def __init__(self, name, age, employee_id, salary):
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.salary = salary
    def show_employee_details(self):
        print("Employee ID:", self.employee_id)
        print("Salary:", self.salary)
class Manager(Employee):
    def __init__(self, name, age, employee_id, salary, department):
        Employee.__init__(self, name, age, employee_id, salary)
        self.department = department
    def show_manager_details(self):
        print("Department:", self.department)
    def full_details(self):
        print(" Manager Full Details")
        self.show_person_details()
        self.show_employee_details()
        self.show_manager_details()
m1 = Manager("Vivek", 45, 10021, 65000, "data science")
print("-----------------")
m1.full_details()
print("-----------------")
print("Below are only employee details")
m1.show_employee_details()
print("-----------------")
print("Below are only manager details")
m1.show_manager_details() 
