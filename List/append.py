# take 5 user input as integer
# append them in alist, print alist

# alist = []
# for prashant in range(5):
#     p = int(input("Enter any number: "))
#     alist.append(p)
# print(f"This is a list that you want {alist}")  

# Take user input 5 times 
# make two list evenlist and oddlist
# if number is even append in evenlist
# if number is odd append in oddlist 

# oddlist = []
# entvenlist = []

# for i in range(10):
#     p = i(input("Enter any number: "))
#     if p % 2 != 0:
#         oddlist.append(p)
#     elif p % 2 == 0:
#         evenlist.append(p)

# print(f"This is your oddlist {oddlist},  This is your evenlist {evenlist}")

# mainlist, evenlist, oddlist and duplicatelist
# take 15 user input as integer
# every input should in mainlist
# even should be in evenlist
# odd should be in oddlist
# duplicate entry shuold be in duplicatelist


mainlist = []
evenlist = []
oddlist = []

for i in range(15):
    n = int(input("Emter any number: "))
    mainlist.append(n)
    if n % 2 == 0:
        evenlist.append(n)
    elif n % 2 != 0:
        oddlist.append(n)
           

print(f"This is mainlist {mainlist}, This is oddlist {oddlist}, This is evenlist {evenlist}")


