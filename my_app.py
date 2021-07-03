#If you can't execute the code then CMD SHIFT P, default choose the detected



name = input('what is your name? ') #This is a variable name
print('hello ' + name) 

#Variable is where you can store anything you want, strings(letters) and numbers

#Creating a variable, you need to give it a name. Think of a variable as a box
name = 'Jamila'
age = 18 
pi = 3.14
cars = ['bmw','mercedes','range rover'] #the datatypes are now a list.


#String is just a sequence of characters
# Interger is just a whole number
#decimals are a float which are DATATYPES
#Everthing in a variable has different datatypes
#List -- allows you to store multiple values

print(name)
print(age)
print(cars)

#STRINGS
name = 'jamila'
surname = 'smith'
full_name = name + ' ' + surname
print(full_name)

#len tells you the length of characters

print(len(name))## the len function tells you how many characters are within the variable name

#introducing the capatalise function to make jamila capital letter

full_name = name.capitalize()+ '' + surname
print(full_name) 
print(full_name.endswith('fucku'))
# the ends with means if the full_name contains the strong fucku

##NUMBERS
addition = 10 + 5
subtraction = 10-15
multiplication = 80*2*4
divided = 10000/80
mod = 10 % 3 ## how many times does 3 goes into 10. MOD is simply the remainder

print(addition)
print(subtraction)
print(multiplication)
print(divided)
print(mod)

#Working with booleans
#use booleans when you want to know if values are true or false
print(10<10)## will give us false
print(0 == 0)
print('jamalia'.endswith('a'))

is_adult = True
age = 18
is_teenager = False

##IF STATEMENTS

#if statement gives you control of flow of program
if is_adult:
    print("is adult") ##if is_adult is true then it will print what is inside

if age >= 18: ## if age is 18, true 
    print('adult')## it will print this line
else:
    print('not an adult') #else, this line will be exectued

#LISTS store more than 1 value
#cars = 'bmw' #string, only store a sequence of characters
cars = ['bmw','tesla','mercedes']
#print(len(cars))## say that we have 3 items 
#print(cars[0])## this gives you the first item in the list/position zero
#print(cars[1])
#LOOPS
## the below will loop for every single item in the list
for car in cars:
    print(car)
## you can even capitalise it
for yourmum in cars:
    if yourmum =='bmw':
        print(yourmum.upper())
    else:
        print(yourmum.capitalize()); ## capital letters for list

#WHILE LOOPS
## allows us to loop while the boolean variable is true, once false it will stop

#number = 0

#while number > 5:
#    print(number)
    
#asshole = 1

#while asshole<=2:
#    print("fuck you nico")

## incrementing

number = 0

while number <=10:
    print(number)
    number = number + 1
else:
    print('while loop ended and value of number is '+ str(number))
#we want to take the number and convert it into a string

#FUNCTIONS
#only gets executed when calling it
#age = 18 we can put numbers inside the function we made
#age2 = 17

#if age < 18:
   # print('oops not an adult')
#else:
 #   print('I am an adult')

#if age2 < 18:
 #   print('oops not an adult')
#else:
 #   print('I am an adult')

#making a function for the above
# the function check_age tells you if you are an adult or note, you simply create the function and change the number inside check_age(X)
def check_age(age):
    if age < 18:
        print('oops not an adult')
    else:
        print('I am an adult')   

check_age(35)
check_age(1)

#BUILT IN FUNCTIONS
#startwith('') just tells you what letter you want to check it starts with
#() parameter
#inside brackets inside the agrument
print('hello'.endswith('o'))# argument is true 

#CLASSES
#blue brints allows us to model
#properties:brand, colour, price
#behaviours: what the phone does;pictures,calls
#use classes as a blue print to create multiple objects

#class Person: # name should always be capital 
 #   def_init_(self, name, age): #this is a function and need to pass arguments
  #      self.name = name # first property name
   #     self.age = age # second property is age
#john = Person('John',22)#John is an object
#mariam = Person('Mariam',18)

#print(john.name + ' ' + str(john.age))# we are going to get an error, need to convert 
#print(mariam.name+ ' '+ str(mariam.age))# a interger into a string
#you need to have two underscores and a space between def & init

class Person:
    def __init__(self,name,age):#properties
        self.name = name
        self.age = age

    def walk(self):#behaviours
        print(self.name + 'is walking...')

    def speak(self):#behaviour
        print('hello my nigga, my name is '+ self.name + ' and I am ' + str(self.age) + 'years old')

john = Person('John', 22)
john.speak()
john.walk()
steven = Person('Steven', 23)
#steven.speak()
#steven.walk()

print(john.name + ' ' + str(john.age))
print(steven.name + ' '+ str(steven.age))

#Behaviours, what classes can do
#behaviour is just a function
# the below is a class
class Person:
    def __init__(self,name,age):
        self.name = name# properties
        self.age = age
    def walk(self):#behaviour
        print(self.name + ' is fucking that bitch')
    def speak(self):
        print('Hi my name is ' + ' '+ self.name + ' I am'+ ' '+ str(self.age)+ 'years old')

steven = Person('steven', 23)
steven.walk()# steven is walking
steven.speak()# steven is speaking, so will return the print
