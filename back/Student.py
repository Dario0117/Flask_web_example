class Student:

    def __init__(self, name, lastname, age, email):
        self.name = name
        self.lastname = lastname
        self.age = age
        self.email = email

    def __str__(self):
        return "%s %s %d %s" % (self.name, self.lastname, self.age, self.email)