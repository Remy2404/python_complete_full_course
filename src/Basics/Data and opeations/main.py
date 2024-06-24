import sys
#0.1 fuction in python :
""" The group sets of code you can use functions . fucntion are small parts od repreatable code. 
    A fuction accepts paramters without fuctions we only have a long list of instructions. fucntions can help you organize code.
     function can also be reused, often they are included in modules
"""
#Example :
"""Function can be seen as excutable code blocks
   A  function can be used once or more.
   Fucntion can be reusable , one can be used in multiple programs.
   The ptint function is an example of that.
   A simple exmaple of a fucntion is :

"""
def currentyear():
    print("2018")
    currentyear()
#Function with paramaeters
"""
In exmaple below we have parameter x and y. type this program and save it
as summation.py

"""
def f(x,y) : 
    return x*y
print(f(3,5))

# Return variables
"""
functions can return variables.
sometime a function make a calcuation or has same output, this
can be given to the program with a retrun variable.
in many cases that output is stored in variable:
"""
result = f(3,4)
print(result)

def sum_list_elements(mylist):
    return sum(mylist)
#Make a fuction that sums the list mylsit :
mylist = [1, 2, 3, 4, 5]
result = sum_list_elements(mylist)
print(f"The sum of the list {mylist} is {result}.")

# or 
def custom_sum_list_with_length(mylist):
    total = 0
    for num in mylist:
        total += num
    return total, len(mylist)

mylist = [1, 2, 3, 4, 5]
x = len(mylist)
result, length = custom_sum_list_with_length(mylist)
print(f"The sum of the list {mylist} is {result}.")
print(f"The length of the list is {x}.")

#List in python :
"""
List can be seen as a collwction : they can hold many variable .
list resemble pysical lists, they can contain a number of item.

A list can any number of element .they are similar to arrays
in other programming languages.
Lists can hold all kinds of variables:
integers (whole numbers ) , folats,
 char , texts and many more.

 """
# example :
#define list  for numeric:
rating = [2,4,53,5,7,9,3]
ratings = [ 'A','A','B','A','C','A' ]
print(ratings)
print(ratings[2])
#!/usr/bin/python

list = [ "New York", "Los Angles", "Boston", "Denver" ]

print(list) # prints all elements
print(list[0]) # print first element

list2 = [1,3,4,6,4,7,8,2,3]

print(sum(list2))
print(min(list2))
print(max(list2))
print(format(list2))

print(list2[0])
print(list2[-1])
lists=list2.pop(3)
print(lists)
print(f"{list2}")

#list opreations
""" 
List can be change with several methods. what are these methods ?
To add items to a list , you can use the appends() method. call the
method on the item to add . calling append(3) would add 3 to the list.
To remove an item form the end of the list , you can use the pop()
 """
#List can be modify by : append and pop :

x = [3,4,5,9,2,6,32,64,8,1]
x.append(6)
print(x)
x.sort()
print(x)
x.reverse()
print(x)

print(x.__sizeof__())
empty_list=[]
a =[34, 22]
b =[45, 56, 5, 60]
c =[23, 28, 38, 40]
d =[2, 3, 1, 4, 66, 54, 45, 89]
print(sys.getsizeof(empty_list))
print(sys.getsizeof(b))
print(sys.getsizeof(c))
print(sys.getsizeof(d))

#Range in python :
""" 
The range() function generates a list of numbers. This is very useful when
creating new lists or when using for loops: it can be used for both.
range() fuc can takes parameter , which must be integers, they can be both
positive and negetive.
By defualt , it create a list of numbers staing form 0.
range(stop)
-range(start, stop, step)
 """
for i in range(1,10):
    print(i)
# step size parameter:
for i in range(0,24,4):
    print(i)

#dictionaries in python:
""" python dictionaries are another collection.Real world
    dicionarice are a good analogy to understands them :
    they contain a lsit of items , each item  has a key and a value.
In the traditional dictionary , the key is the word and the value is the 
explanation or descrition of it. in python you can do something similar.

 """
#Example : 
# Introduction :
"""
In a more strict way of speaking (meathematical) , a dictionary is a one to one 
mapping. for every key in the dicitionary there is a value.
Thus value is assigned to the key.
Dicitionary contains : key and value
"""
#Defintion :
""" let type some code! we can create a dictionary with a one liner.
A dictionary is defined with these brackets {} """



words = {}
words["BMP"] = "Bitmap"
words["BTW"] = "By The Way"
words["BRB"] = "Be Right Back"

print(words["BMP"])
print (words["BRB"])

#Read file in python 
"""
Readding file is part of python standard libray. This means you 
do not have to include any module.
 
These are two ways to read files :
> line by line
> read bolck
In this article we will show you both methods

The solution you depends on the problem you are tying to solve.

"""
# Eaxmple:
#Line by lines you can use the readline() function.This wiil read a file line by line abd store it into a list:

myfile = "file.py"
with open(myfile) as fn :
    content = fn.readlines()
    print(content)

#!/usr/bin/env python
#Read block
filename = "file.py"

infile = open(filename, 'r')
data = infile.read()
infile.close()

print(data)

#Nested loops 

"""
A loop can contain one or more other loop: you can create a loop inside a loop.
This principle in known as nested loops.Nested loops go over two or more loop.

programming typically nest 2 or 3 levels deep. Anything higer than that is just confusing.

"""
# Example :
persons = [ "John", "Marissa", "Pete", "Dayton" ]
restaurants = [ "Japanese", "American", "Mexican", "French" ]
foods = ["micha", "bycha", "numbnhjok", "lordcha"]

for person in persons : 
    for restaurant in restaurants:
        for food in foods:
            print(person+" eat "+restaurant+" and "+food)

# How to slide list/ arrays in python :
"""
A silce can be taken form a string or list , as you can take a slice form a pizza.
if you have a variable , be it a list or a String .that you want a part of , you don't have 
to define it all over again.
you can get a copy of the variable , which is the whole or a subset of the original vaiable.
this concept is know a slicing
"""
#Eample 
#Take a the fist two sicle , you would use :
#!/usr/bin/python
slice = persons[0:2]
print(slice)

# Multiple return 

""" 
python function can  be retrun mutiple variable.These variable can stored in variable directly.A
Function is not requested to return
a variable , it can retrun zero, one , two , or more variables.

"""
def complexfunction(a,b):
    sum = (a+b)
    return sum
# call_function :
result = complexfunction(2,4)
print(result)

def getPerson():
    name = "Ramy"
    age =35
    country = "KH"
    return name, age , country
name , age , country = getPerson()
print(name)
print(age)
print(country)

#python Scope of variables :

"""
Variable have a certain  reach within a program .A golbal variable can be used anywhere in program,'
but a local variable in known only in certain area (function , loop)
 sometimes the word scope of project ", meaning not included the scope of a functin.

 """
#EXAMPLE :
""" Scope has to do with where a variable can be used.If you define a variable , it's not necessarily usable everywhere in the code. A variable defined in a function
is only known in a a function , unless you return it. """

def someting():
    localVar = 1
    print(localVar)

#Global and local variables:
""" 
In the program below m balance is a global vaiable. it can used anywhere in code. But the variable 
x can only be used inside add amount.

"""
balance = 0
def addAmount (X):
    global balance
    balance = balance + X
test = addAmount(5)
print(test)


#Date and time in python 
# if you want to get the system time using the module time. is not part of the module import time.
import time

timenow = time.localtime(time.time())
year,month,day,hour,minute = timenow[0:5]


print(str(day) + "/" + str(month) + "/" + str(year))
print(str(hour) + ":" + str(minute))


from datetime import datetime

now = datetime.now()  # Current date and time
year = now.strftime("%Y") 
month = now.strftime("%m") 
day = now.strftime("%d")  # Day (e.g., 24)
time = now.strftime("%H:%M:%S")  # Time 
date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

print(f"Year: {year}")
print(f"Month: {month}")
print(f"Day: {day}")
print(f"Time: {time}")
print(f"Date and time: {date_time}")


#Try and except in python :

""" 
The try except statement can handle exceptions. Exceptions may happen
when you run a program.

Exceptions are error that happen during excution of the program.
python won't tell you about error like syntax error (grammer faults),
instead it will abrupty stop.

"""
""" try: 
    <do someting>
except Exception:
    <handle the error> """
""" 
The idea of try-except block is this :
> Try : The code with the exceptions to catch. if an exception is raised, it jumps straight into
the except block.
> except: this is only excuted if an exception occured in the try block.
The except block is requirced with a try block , even if it contains only the pass statement.

It may be combained with the else and finally keywords.
>else: Code in the else block is only excuted if no exceptions were raised in the try block.
>finally: The code in the finally , block is always excuted, regeandless of if an exception was 
raised or not.
 """
# Example :

try:
    1/0
except ZeroDivisionError:
    print('Disvid by zero')

    print('should reach here')

try:
    x = input("Enter number: ")
    x = x + 1
    print(x)
except:
    print("Invalid input")

try:
    f = open("file.txt")
except:
    print('Could not open file')
finally:
    f.close()
    print('Program continue')
try:
    with open("file.txt") as f:
        # Perform file operations here
        pass
except FileNotFoundError:
    print('Could not open file')
print('Program continue')

