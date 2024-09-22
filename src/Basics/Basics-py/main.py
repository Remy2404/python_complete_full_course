# 0.1  DataTypes : Variable can be of several data types. python support integers ,  float , String , boolean (True or false)
x = 10
f =10.54
s = "Hello"
print(x)
print(f)
print(s)

combination = s + " " + s
print(combination)
sum = f + f 
print(sum)

 # 0.2. python Strings (with Example) : 
#Define a String : 
x = "Hi" 
print(x)
# String index : 
print(x[0])
print(x[1])

# Sub String :
# By using a colon you can create a sub_String. if you start oe end numbers is written , python assumes you mean the first Char or last Char.
x = "Sub String"
s =x[1:2]
print(s)
s= x[:3]
print(s)
# complete exmaple : 
""" This exmaple does alot of String apeations like printing text, numbers, combining String 
slicing and accessing elements """

k= "Nancy"
print(k)
#combine numbers and text
s = "My Lucky numbers is %d , what is yours ? " % 7 
print(s)
s= "My lucky number is " + str(7) + " ,what is yours? "
print(s)

#print Char by index : 
print(k[0])
#print price of String : 
print(k[0:3])

#0.3 python String replace() Methods
""" python has builtin for String replacement . A Strign is a variable that contains
text data . if you don't know about String , you can read more about Strings in this article.
Can call the String .replace(old , new )  mehtod using the String object """
 #example : 
let = "hello wrold"
s_s= let.replace("wrold" , "Universe")
print(s_s)

#0.4.join() func : The join(sequence) method joins element and returns thr combined
# The join methods combines every element of the sequence.

# combine list of words ?
""" Combine them into a sentence with the join(sequence) 
mehtod. The method is called on a seperate String , which can be anything form a space to a dash
"""
# exmample :

#Define Strings :
firstname = "Phon"
lastname = "Ramy"

#define our sequence 
sequence = (firstname , lastname)
#join into  new String in seq:
name = " ".join(sequence)
print(name)

#0.5 find() in python : 
""" The find(query) method is built-in to Standard python 
Just call the method on the string obj to search  for a String , like 
so : obj.find("search").
The find method seraches for a query String and returns the char position it found. if the string 
is not found , it returns -1.

 """
#Example : 
s = "That I ever did see. Dusty as the handle on the door"
index = s.find("Dusty")
print(index)
#Split() methods
""" if you have a string , you can subdivde into several 
string. The string needs to have at the least one separting char , which may be a space 
 By default the split method will use space as separator , calling the method will retrun a list of all the substring"""
#Example : 

strr = "It's to easy bro !"
worlds = strr.split()
print(worlds)
# The len or length method will give the number of char and number of world:

print(len(worlds))
print(len(strr))