
#Python Function Examples:

""" 
A function in python is a piece of code that runs when it is referenced.
It is used to utilize the code in more than one place program. It is also called a methodor procedure.

python satement function :
def : 
"""
# Syntax :
""" def functionname(parameters):
    "function_docsting"
    function_suite
    return[expressiom]
"""
#python lambda function :
""" 
A lambda function is a small anonymous function or a function having no name.

It is used to create small functions.
A lambda function can take any number of arguments, but can only have one expression.
 The expression is evaluated and returned.
 The Lambda function can be used wherever function objects are required.
 keyword lambda is used to define a lambda function. (just like def) to define a function.
 Define in python will have 3 essentinal parts :
1. The lambda keyword.
2. The parameters (or bound variables).
3. The expression (or body) of the function.

A lambda function can have any number of parameters , but the function body can contain only one expression.
Moreover, a lambda is wrritten in a single line of code and not in a block of statements.
And here is a lambda in python tutorial will we learn :
1.lambda in filter()
2.lambda in map()
3.lambda in reduce()
4.lambda in sorted()
5.lambda in zip()
6.lambda in dict()
7.why(and why not ) use lambda function ?
8.lambda in list comprehension
9.lambda in generator comprehension
10.lambda in set comprehension
11.lambda in dictionary comprehension
12.lambda in string formatting
13.lambda in list slicing
14.lambda vs.Regular function
-> Syntax :
lambda arguments : expression
lambda p1 , p2 : p1 + p2 

Example :
add = lambda x , y : x + y 
print(add(10,20))

"""
add = lambda x, y : x + y
print(add(10,20))
#what a lambda returns :
string = 'some kind of a useless lambda function'
print(lambda string : print(string))
""" 
# explain code above :


"""
#What a lambda returns #2
x="some kind of a useless lambda"
(lambda x : print(x))(x)
