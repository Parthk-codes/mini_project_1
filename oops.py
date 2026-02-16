# class - blueprint or template
class student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

# object - instances of class
student1 = student('madhav', 11)
print(student1.name, student1.grade)

student2 = student('parth', 12)
print(student2.name, student2.grade)