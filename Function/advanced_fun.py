# def o():

#     def p():
#         print('my name is prasahnt')

#     p()

#     print('im youer father')
# o()    

# def p():

#     def oq():
#         print("pras")
#     return oq()
#     print('my name is khan')


# # q = p()
# # r = oq()

# # def pras(name):
# #     print(f"Good morning {name}")

# # def pra(khanal):
# #     khanal('prashant')

# # pra(pras)        

# # def khanal():
# #     return 'prashbat'

# # a = khanal

# # print(a())




# def prasahnt_func(func):
#     def khanal():
#         print("Printed before function call")
#         func()
#         print("Printed before function call")
#     return khanal

# def example():
#     print("I am example function")


# a = prasahnt_func(example)
# a()

# printed before fuction call
# i am example function
# printed before

# def a():
#     return 'laptop'

# b = a()
# print(b) 


# def greet(p):
#     print(f"Welcome {p}")


# def greet_with_name(abc): #abc = greet
#     abc("Ram") # greet("Ram")


# greet_with_name(greet)        


# def decorate_func(func):
#     def wrapper():
#         print("Printed before function call")
#         func()
#         print("Printed after function call")

# def decorate_func(func): # example
#     def wrapper():
#         print("Printed before function call")
#         func() # Example lai call gareko jastei ho
#         print("Printed after function call")
#     return wrapper

# @decorate_func
# def example():
#     print("i am example function")


# example()


# def decorator_func(abc):
#     def wrapper():
#         print("My name is prashant")
#         abc()
#         print("I leave in kathmandu")

#     return wrapper 

# @decorate_func
# def khanal():
#     print("my cast name is khanal")

# khanal()     

# def decorate_func(name):
#     def wrapper():
        

#         name()
#         print("i'm from khatmandu nepal")

#     return wrapper    



# @decorate_func
# def func():
#     print("My name is prashant")
# @decorate_func
# def pras():
#     print("I'm super man")


# func()
# pras()


# def address(pras):
#     def wrapper():
#         pras()
#         print("I studied in texas college")

#     return wrapper    

# @address
# def p():
#     print("my name is prashant")
# @address
# def b():
#     print("My name id bishal")

# p()
# b()

# def division_Error_by_zero(pra):
#     def wrapper(a, b):
#         if b == 0:
#             return "Cannot Divide by zero"
#         else:
#             return a / b
#         pra()

#     return wrapper        

# @division_Error_by_zero
# def division(a, b):
#     return a / b



# def smart_division(div):
#     	def wrapper(*args, **kwargs): # *args, **kwargs
# 		if args[1] == 0:
# 			return "Can not divide by zero"
# 		else:
# 			return div(*args)
# 	return wrapper


# @smart_division
# def division(dividend, divisor):
# 	return dividend / divisor


# print(division(10, 5))
# print(division(100, 0))




# print(division(20, 5))

# print(division(500, 10))


