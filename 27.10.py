class NameSurname:
   def  __init__(self, name, surname):
       self.name = name
       self.surname = surname


class Student:

    student_amout = 0
    def __init__(self,name, surname,age, height=188):
        self.ns = NameSurname(name,surname)
        self.age = age
        self.height = height
        Student.student_amout += 1

    def printStudent(self):
        print(f'Name: {self.ns.name}')
        print(f'Surname: {self.ns.surname}')
        print(f'Age: {self.age}')
        print(f'Height: {self.height}')

print(f'before creating Student object {Student.student_amout}')
first_student = Student("Ilya", "kosilo", 14)
first_student.printStudent()
print(f'after creating Student object  {first_student.student_amout}')

class Age:
    def Birthday(self):
        self.age += 1
    print(f' З днем народження! {self.ns.age}' )
