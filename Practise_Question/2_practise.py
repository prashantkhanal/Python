# if name is less than 3 character long
#    name must be at least 3 characgter long
# otherwise if it's more than 50 character long
# otherwise
# name looks good    

# a = input()

# if len(a) <= 3:
#     print("The character must be at least 3 character long ")
# elif len(a)> 50:
#     print("The charcter must be less than 50 character ")

# else:
#     print("Name looks good ")    

# # take a user input of his/her weight and convert into his/her choice kg/pound
# mass = int(input("Enter your weight: "))
# unit = input("L or Kg: ")

# if unit.upper() == 'L':
#     pras = mass * 0.45  
#     print(f"Your weight is {pras} pound")
# else:
#     unit.upper()== 'Kg'
#     prashant = mass / 0.45  
#     print(f"Your weight is {prashant} kg")    

# CAR GAME 



# while True:
#     a = input()
    
#     if a == 'help':
#         print('Start - to start the car')
#         print('Stop = to stop the car')
#         print('quit = to exit')

#     elif a.lower() == 'start':
#         print("Car is starting...........")

#     elif  a.lower() =='stop':

#         print("car stooped")

#     elif a.lower() == 'stop':
#         print('Car has stooped')

#     elif a == 'quit':
#         break              

 
    


# command = ''

# while command != 'quit':
#     command =  input('>' )
#     if command == 'start':
       
#         print('car is starting')
#     elif command == 'stop':
#         print('Car stooped') 
#     elif command == 'help':
#         print("""Start - to start the car
#                  Stop = to stop the car')
#                  quit = to exit""")

#     else:
#         print("soory")                 


# while True:
#     a = input()
#     if a == 'prashant':
#         print("this id your name")
#     elif a == 'khanal':
#         print("This is your cast")

#     else:
#         a == 'quit'
#         break

# print('Thank you')         
       

# numbers = [5, 2, 5, 2, 2]
# for i in numbers:
#     print('x' * i)
    
# numbers = [2, 3, 7, 9, 1]

# for i in numbers:
#     print('y' * i)


# a = ['khanal', 'rawal', 'sapkota']

# while True:
#     b = input('Enter your name to find your cast: ')

#     if b== 'prashant':
#         print(a[0] )

#     elif b == 'bishal':
#         print(a [1])

#     elif b == 'anish':
#         print(a[2])

#     elif b == 'quit':
#         break     

#     else:
#         print("Soory we don't have your name in our database")



# a = ['prashant', 'khanal', 'bishal', 'rawal']

# print(a[1: 4])


# a = [1, 3, 4]

# a, y, z = a
# print(a)
# print(y)
# print(z)


unit = input("Kg or Pound: ")
mass = int(input("Enter the mass: "))

while True:
    
   
    

    if unit == 'kg':
        converter = mass * 2
        print(f"Your weight is {converter} kg")

    elif unit == 'pound':
        conve = mass / 2
        print(f"your weight is {conve} pound")

    elif unit == 'quit':
        break 

print("Thank you")           
