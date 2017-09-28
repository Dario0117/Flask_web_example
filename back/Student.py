class Student:
    id = 0
    def __init__(self, name, lastname, age, email):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email
        self.id = Student.id
        Student.id = self.id + 1