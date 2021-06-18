 class person:
   
     def __init__(self, name, age):
         self.name = name
         self.age = age

     def study(self):
         print(f"{self.name} is studing.")



 class student(person):
     def __init__(self, _id, name, age):
         super().__init__(name, age)
         self._id = _id


     def eating(self):
         print(f"{self.name} is eating")
       

 prashant = student("001", "prashant", 60)
 prashant.study()
 prashant.eating()


class Student_name:

    def __int__(self, college_name, college_address):
        self.college_name = college_name
        self.college_address = college_address

    def read(self):
        print(f"{self.name}is reading in Texas college")

class sagar(Student_name):

    def __init__(self, MarksObtained):
        super().__init__()
