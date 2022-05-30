class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def details(self):
        print(f"My name is {self.name} and age is {self.age}")
p1 = Person("Caleb",17)
p1.details()
class Employee(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary=salary
    def details(self):
        print(f"My name is {self.name} and my age is {self.age} and my salary is {50000}")
p2 =Employee("Caleb",17,50000)
p2.details()