import logging
logging.basicConfig(level=logging.DEBUG,
                    filename='logs.log',
                    filemode='a',
                    format="%(levelname)s:%(asctime)s")


class NameSurname:
   def  __init__(self, name, surname):
       if(type(name)!= str):
          raise TypeError(f"Name or Surname is not a string")
       if(type(surname) != str):
          raise TypeError (f"Surname is not a string ")
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

#print(f'before creating Student object {Student.student_amout}')

logging.info("start program")
try:
    first_student = Student("Ilya", "kosilo", 14)
    logging.info(f'Create new student {first_student.ns.name} {first_student.ns.surname}')
    second_student = Student("Pampywka", "RIshyska", 9)
    print(f'Start programm')
except Exception as error:



    logging.error("error")
#first_student.printStudent()
#print(f'after creating Student object  {first_student.student_amout}')

#print("Next code")
#firs_student.Birthday()

logging.info("finish program")

class Animal:
    def __init__(self,name,weight,quantity):
        self.name = name
        self.weight = weight
        self.quantity = quantity


        def printAnimal(self):
            print(f'Name: {self.ns.name}')
            print(f'Weight: {self.ns.weight}')
            print(f'Quantity: {self.ns.quantity}')
    print(f'Name: Cat, Weight: 8 kg,Quantity: 1 ')



