# make a faulty calculator which makes while adding 2 + 2 = 400, multypling 50*5 = 50, while dividing 500/5 = 500
#  and subtracting 500-100 = 1000

opreator = input("Enter your opreator to calculate: ")
num = int(input('Enter any number: '))
num1 = int(input("Enter another number: "))


if opreator == '+':
    if num == 2 and num1 == 2:
        print("The sum is 400")

    else:
        print(f"The sum is {num + num1}")  

if opreator == '-':
    if num == 500 and num1 == 100:
        print("The sum is 1000")

    else:
        print(f"The sum is {num - num1}")  




if opreator == '*':
    if num == 500 and num1 == 5:
        print("The sum is 50")

    else:
        print(f"The multipication is {num * num1}")

if opreator == '/':
    if num == 500 and num1 == 5:
        print('The division is 500')

    else:
        print(f"The division is {num/num1}")    



        