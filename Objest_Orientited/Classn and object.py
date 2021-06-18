class marks:
    def __init__(self, English, Nepali, Physic, Chemistry, Mathmatics):
        self.Eng = English
        self.Nep = Nepali 
        self.Phy = Physic
        self.Chem = Chemistry
        self.Math = Mathmatics


Prashant = marks(50, 60, 80, 90, 100)
Bishal= marks(80,  86, 90, 70, 100)
Anish = marks(50, 60, 80, 90, 1000)
Meghraj= marks(50, 60, 80, 90, 100)
Bishal_kun= marks(50, 60, 80, 90, 100)

print(f'''Prashant{Prashant.__dict__}
Bishal{Bishal.__dict__} 
Anish{Anish.__dict__}
Meghraj{Meghraj.__dict__}
Bishal{Bishal_kun.__dict__}''')

class Book:
    def __init__(self, name, price):
        self.Bookname = name    
        self.Cost = price

    def (self):
        

p = Book("Python Programming", '1200')

print(f"List of Book Aviable are{p.__dict__}")

class student:
    College_name = "Texas college"
    # Initalizer function
    def __init__(self, _id, name, address):
        # Instance variable
        self._id = _id
        self.name  = name
        self.address = address

    def Prashant(self):
        print(f"The {self.name} is First boy")

st1 = student("001", "Prashant khanal", "Kapan")
st2 = student("002", "Bishal Rawal", "Chabhail")
st3 = student("003", "Anish sapkota", "Suryabinyak")

print(student.College_name)
print(st1.__dict__)
print(st2.__dict__)
print(st3.__dict__)


class student:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def p(self):
        print(f"{self.name} is studing")


st = student("Prashant", 'kapan')
st1 = student("bishal", "Rawal")

print(st1.__dict__)
print(st.__dict__)

st.p()


class Product:
    def __init__(self, name, price, brand=None):
        self.item = name
        # Name mangaling
        self.__price = price



p1 = Product("T-shrit", 800)
# print(f"Inital price {p1.price}")

p1.price = 400

print(p1.__dict__)
print(f"Changed price {p1.price}")



class college_student_detail:


    def __init__(self, name, address):
        self.__name = name 
        self.address = address

    @property
    def changed_name(self):
        return self.__name
    @changed_name.setter
    def changed_name(self, final_name):
        return self.__name

st1 = college_student_detail("Prashant", "kapan")

st2 = college_student_detail("Bishal", "chabhail")
print(st2.name)
st1.changed_address = "kapan"
# print(st1.__dict__)
# print(st2.__dict__)
print("later name :", st1.changed_name)
print("The name is prashant khanal")
