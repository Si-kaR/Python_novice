Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
print('Hello world')
Hello world
print(variableName)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    print(variableName)
NameError: name 'variableName' is not defined
print('Value of variable', variableName)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print('Value of variable', variableName)
NameError: name 'variableName' is not defined
#you don't have to specify variables
print('Value of variable,' varibaleName, 'with a coninued sentence.')
SyntaxError: invalid syntax. Perhaps you forgot a comma?
print("It's a nice day outside")
It's a nice day outside
########
#####
####
###
#Variabbles

room = 503 #will be stored as an int
rentalRate = 87.99 #will be stored as a float
hotelName = 'Logic Lodge'

print('I am staying in room number', room)
I am staying in room number 503
print('My room number is ', room)#will print the number whcih has been saved as a variable
My room number is  503
print('The rate at', hotelName, 'is', rentalRate)
The rate at Logic Lodge is 87.99
hours = input('How many hours did you work?')
How many hours did you work?
employee_name = ra_input('Enter your name: ')
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    employee_name = ra_input('Enter your name: ')
NameError: name 'ra_input' is not defined

