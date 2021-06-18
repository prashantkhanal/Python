# def pras():
#     print("I'm the hero of this universe")

# pras() # => This is the excuate of function 
# khanal = pras() # => reference leyera call garnu ho
# khanal

# def my_basic_information(name, address, contact): # parameter
#     print(f"Your name: {name}")
#     print(f"Your address: {address}")
#     print(f"Your contact number: {contact}")

    # required positional argument
    # my_basic_information('Prashant khanal', 'kathmandu', 9840337736) # argument
    # keyword argument
    # my_basic_information(contact= 9840337736, name='prashant', address= 'kathmadu')

    # Take 5 times user input
    # print the grestest number, lowest number
 
# def n(num, num1):
#   return num +num1

# p = int(input("Enter any number: "))
# m = int(input("Enter another number: "))

# ans = n(p, m)

# print(f"The sum of {p}and {m} is {ans}")  


# # find out the difference of tow number
# # addition of two number
# # multiplication of ftwo nummber
# # division of two number

# def add_two_number(num , num1):
#     return num + num1

# def substraction_two_number(num , num1):
#     return num  - num1

# def quotient_two_number(num , num1):
#     return num // num1

# p = int(input('Enter any number: '))
# m = int(input('Enter another number: '))

# pras = add_two_number(p , m)
# pras = quotient_two_number(p , m) 
# pras = substraction_two_number(p , m)


# print(f"The sum of {p} and {m} is {pras} ")  
# print(f"The substraction {p} and {m} is {pras} ")    
  
# print(f"The quotient of {p} and {m} is {pras} ")    


# def prashant(*args):
#     print(args)

# prashant(1,2, 3, 4, 'prashant', 'python', 'java', 'c++', 'swift')


# def khanal(**kwargs):
#     return kwargs
   
# khanal( name= 'khan', cast= 'prashant', address= 'kapan') 

# def op(*args, **kwargs):
#     print(f"Args{args}")
#     print(f"kwargs{kwargs}")


# op(1, 2, 3, 4, 5, 'python', 'django', name= 'bishal', cast = 'rawal', address = 'chabhail')

# num = 10 #=> global scope

# def pa():
#     num = 5 #=> local scope
#     print(num)

# pa()    
# print(num)


# p = int(input("Enter any num:"))
# q = int(input("Enter any num:"))

# number = p + q

# def pras():
#     p = int(input("Emter any num: "))
#     q = int(input("Emter any num: "))
#     number = p + q
#     print(number)

# pras()
# print(f"The sum of {p} and {q} is {number} ")

# n = 20

# def pras():
#     # global n
#     # n +=1
#     print(n)

# pras()


# n = 1

# def op():
#     n = 20
#     for i in range(1):
#         o = int(input("Enter any num: "))

#     if o == n:
#         print('You win')

#     else:
#         print("You loose")

# op()        
# print(n)             

# def percent(marks):
#     p = ((marks[0] + marks[1] + marks[2] + marks[3] + marks[4])*100)/400
#     return p
# prashant = [45, 78, 86, 77, 44]
# percentage = percent(prashant)

# print(percentage)


# def percent(num, num1):

#     return num + num1

# prashant = percent(12, 2)
# print(prashant)
# def message(fullname, cast):
#     print("Good morning, " +  fullname  +  cast )

# message('prashant',  'khanal')

def pras():

    def khan():
        print("My name is prashat")
    khan()
    print("my name is khanal")



pras()

