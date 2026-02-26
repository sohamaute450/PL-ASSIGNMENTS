class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(self.name, self.age)
class Student(Person):
    def __init__(self, name, age, marks):
        Person.__init__(self, name, age)
        self.marks = marks
    def stud(self):
        print("I am Student")
student1 = Student("abc", 18, 93)
student1.display()
student1.stud()
print(student1.marks)
