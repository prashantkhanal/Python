
# write a program in python such that ask a user to input name 
# and pw if it matches  from a database of users and passsword print access granted else print acess denied


# d = {'id':'prashant', 'p': 'bishal', 'pw': 'programmer', 'o': 'hacker'}
# choice = 'yes'

# while choice.lower() == 'yes':
#     pp = input("Enter your name: ") 
#     po = input("Enter your pw: ")

#     if pp == d.get('prashant') and po == d.get('programmer'):
#         print("Access granted.")

#     else:
#         print("Access denied")

#     choice = input("Do you want to cotinue and try to login (yes/no)?")       

# no of guesses 9 
# print no of guesses left
# game over
# No of guess he took to finish

# av = 5
# n = 19 
# i = 1


#     p = int(input("Enter the number /n"))

# if n < 18:
#     print("sorry!! you have enter minumum number")
#     print("You have left only 8 guess")
# elif n>20 :
#     print("Sorry you have guess the maximum number")

# elif n== 19:
#     print("You have won this game")

# else:
#     print("Game over!!!")                 



# # no of guesses 9
# # print no of guesses left
# # No of guesses he took to finish
# # game over


# # wap(write a progam) in python that takes two lists and prints the common numbers as 
# # output{ for eg input = [1,2,3,,5,7,9}{1,2,4,6,8} output should be [1,2}



 
   
# l1 = []
# l2 = []
# l1=int(input("enter first list"))
# l2=("enter second list")
# def common( l1,  l2):
  
#     output=[]

#     for i in l1:

#         if i in l2:

#             output.append(i)



#     return output
# print(output)    
# print(common(l1,l2)

# a = []
# b = []
# c = []
# print('Enter the first list')

# for i in range(3):
#     p = int(input("Enter the number: "))
#     a.append(p)
   
    
# print('The second number ')    
# for i in range(3):
#     q = int(input('Enter the number: '))  
#     b.append(q)
# if a not in b:
#     c.append(a)

# elif b not in a:
#     c.append(b)






# # print(a)
# # print(b)
# print(c)



# def greet(name):
#     print(f'welcome {name}')

# def greet_with_name(fun):
#     fun('prashnat')


# greet_with_name(greet)    

# import random   
# def gameWin(comp, you):
#     if comp == you:
#         return "Tie"
#     elif comp == 's':
#         if  you == 'w':
#             return "computer win"
#         elif you == 'g':
#             return "you win"

#     elif comp == 'w':
#         if you == 'g':
#             return False
#         elif you == 's':
#             return True
#     elif comp == 'g':
#         if you == 's':
#             return False
#         elif you == 'g':
#             return  True

# comp = input("Enter s , w: ")
# you = input("Enter s , w: ")

# prashant = (comp, you)

# khanal = gameWin(comp, you)
# print(khanal)



# print("Com Turn: snake(s) Water (w) or Gun (g)? ")
# randNo = random.randint(1, 3)
# if randNo == 1:
#     comp = 's'
# elif randNo == 2:
#     comp = 'w'
# elif randNo == 3:
#     comp = 'g'

# you = input("your Turn: snake(s) Water (w) or Gun (g)? ")

# a = gameWin(comp, you) # Function call

# print(f"Computer choose {comp}")
# print(f"You choose {you}")
 
# if a == None:
#     print("The game is Tie!")

# elif a:
#     print("You win!")

# else:
#     print("You loose")        


# import random

# def name_cast_matching_game(user, second_player):
#     if user == 'prashant':
#         if second_player == 'khanal':
#             return "You win"
#         else:
#             return 'You loose'

#     if user == 'bishal':
#         if second_player == 'rawal':
#             return "You win"
#         else:
#             return 'You loose'
#     if user == 'anish':
#         if second_player == 'sapkota':
#             return "You win"
#         else:
#             return 'You loose'
#     if user == 'prince':
#         if second_player == 'singh':
#             return "You win"
#         else:
#             return 'You loose'                        



# user = input("Enter your name: prashant, bishal, anish, prince:  ")
    
# second_player = input("Emter your cast: singh, sapkota, khanal, rawal: ")    
    



# a = name_cast_matching_game(user, second_player)
# print(a)

