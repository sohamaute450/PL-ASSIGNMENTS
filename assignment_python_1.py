n = int(input("Enter number of students: "))
# List 
students = []
for i in range(n):
    name = input(f"Enter name of student {i+1}: ")
    students.append(name)
#  Tuple
subjects = ("Maths", "Science", "English")
#  Dictionary
marks = {}
for name in students:
    print(f"\nEnter marks for {name}:")
    student_marks = []
    for subject in subjects:
        mark = int(input(f"{subject}: "))
        student_marks.append(mark)
    marks[name] = student_marks
#  Set 
all_marks = []
for m in marks.values():
    all_marks.extend(m)
unique_marks = set(all_marks)
print("Students List:", students)
print("Subjects Tuple:", subjects)
print("Marks Dictionary:", marks)
print("Unique Marks Set:", unique_marks)
