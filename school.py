class person:
      def __init__(self,name,dob,height,weight):
          self.name=name
          self.dob=dob
          self.height=height
          self.weight=weight
      def date_of_birth(self):
          dob=self.dob
          print(dob)
      def age(self):
          self.year=2022
          age=self.year-self.dob
          print(age)
      def height(self):
          print(self.height)
      def weight(self):
          print (self.weight)
      def bmi(self):
          bmi = self.weight/(self.height)
          print (bmi)


class student(person):
    def __init__(self, name, dob, height, weight, class_studying, favourite_subject):
        super().__init__(name, dob, height, weight)
        self.class_studying = class_studying
        self.favourite_subject = favourite_subject
    def class_studying(self):
        print(self.class_studying)
    def favourite_subject(self):
        print(self.favourite_subject)
   
class teacher(person):
    def __init__(self, name, dob, height, weight, class_teaching, salary):
        super().__init__(name, dob, height, weight)
        self.class_teaching = class_teaching
        self.salary = salary
    def class_teaching(self):
        print(self.class_teaching)
    def salary(self):
        print(self.salary)   
#instantiate
x = person("Fiona", 2004, 5, 150)
y = student("kamau", 2001, 5, 150, "1st", "Pysics")
z = teacher("Justin", 1998, 5, 150, "1st", "Biology")