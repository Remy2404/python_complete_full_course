 #0.1 if Statement
""" In python the if statement is used for condition execution or branching.
An if statement is one of control Structures.
The if Statement may be combined with certain opreator such as equaltiy(==) 
 , greater than (>=) , Smallr (<=) and not equal (!=)
 Condition may be combined using the keywords or and and """

# if <condition>:
#<statement>
x = 4
if x < 10:
    print("x below ten")
    if x >10 :
       print("x is greater than ten")
if x > 1 and x <= 4 : 
                print('x is range ')

# if-Else : 
gender = input("Gender? : ")
if gender == "male" or gender == "female" : 
        print("You are male")
else:
        print("you cat is female ")

age = int(input("Age of your cat ? : "))
if age < 5 :
 print("Your cat is young")
else: print("Your cat is adult.")

num  = 4 
if num < 5 : 
        print ("x is smaller than five ")
        print(" thsi means it's not equal to 5 ")
        print("X is an integer")

#0.2 else_if: 
x = 3 
if x ==2 :
        print("two")
elif x==3:
        print("three")
elif x== 4 :
        print("four")
else:
        print("somthing else")

number = int(input("Enter the number between 1 and 10: "))
if number not in range(1, 11):
    print("Invalid number")
else:
    print("You entered a number between 1 and 10")


# 0.3 loop in python : 
"""  A for loop is written inside the code .
     A for loop can have 1 or more instructions
     A for loop can will repeat a code block.
     Repeation in continued until the stop condition is met
     of the stop condition is not met it will lopp infintely.
     
     These instrucions (loop) is repeated until a condition is met."""

# Example :
city = ['Tokyo' ,'New York' , 'phnom penh' , 'hong kong']
print('city loop: ')
for x in city :
       print("city : " + x)
       print("\n") #newline

drinks = ['coke', 'Pepsi', 'Sprite', 'water']

for x in drinks :
        print("drink : " + x)

num = [1,2,3,5,8,7,9,4]
print("x^2 loop : ")
print('\n')
for x in num :
        y =x*x
        print(str(x) + '*' + str(x) + '=' + str(y))
# 0.4 while loop (indefinite iteration)
""" "A while loop repeats code until the condintion is met . unlike for loops , the number of interations in it may be unknow ]
. A while loop always consists of a condiontion  and a block of code 
A while loop end if and only if the condition is true , in contrast to a for loop that always has a finite 
countable number numer of steps" """
#Example :
x = 1
while x < 10 :
       print(x)
       x= x+1
else : print("invalid number")
print('\n')