#TASK 1-5 CODE COMBINED
def main():
    d = eval(input("Input the starting day (0=sun, 1=mon, ...): "))
    n = eval(input("Input the number of days in the month (28-31): "))
    for j in range(d):#
        print(" ", end = "  ")#

    i = 1
    while i <= n:
        if i < 10:
            print("",i, end = " ")
        else:
            print(i, end = " ")
        if (i+d) % 7 == 0:
            print(" ")
        i = i + 1
main()# calling function for TASK 1-5 combined



#Practice exercise for building Calendar
'''Activity 1
This program will build a calender using test parameters
'''
def buildingCalendar(n,d):
    for j in range(d):
        print(" ", end = "  ")

    i = 1
    while i <= n:
        if i < 10:
            print("",i, end = " ")
        else:
            print(i, end = " ")
        if (i+d) % 8 == 0:
            print(" ")
        i = i + 1
#Calling function for program to print three calendars with input parameters
print("")
print("\nThis is a test to build a calendar with determined parameters")
buildingCalendar(30,5)
print("\n")
buildingCalendar(31,2)
print("\n")
buildingCalendar(29,4)


''''Activity 2
This program will build a calendar having 8 days
'''
def buildingCalendar(n,d):
    for j in range(d):
        print(" ", end = "  ")

    i = 1
    while i <= n:
        if i < 10:
            print("",i, end = " ")
        else:
            print(i, end = " ")
        if (i+d) % 8 == 0:
            print(" ")
        i = i + 1
#Calling function for Calender program that has 8 DAYS A WEEK
print("")
print("\nThis is a program that builds a calendar\nfor a society that has 8 days in a week")
buildingCalendar(30,5)
print("\n")
buildingCalendar(31,2)
print("\n")
buildingCalendar(29,4)
print("\n")





'''Activity 3
This program will build any given number of calenders
Each time, the user will have to give the value n for number of days in the month
and d for position where first day should start
'''
def buildingCalendar():
    d = eval(input("\nInput the starting day (0=sun, 1=mon, ...): "))
    n = eval(input("Input the number of days in the month (28-31): "))    
       
    for j in range(d):
        print(" ", end = "  ")

    i = 1
    while i <= n:
        if i < 10:
            print("",i, end = " ")
        else:
            print(i, end = " ")
        if (i+d) % 7 == 0:
            print(" ")
        i = i + 1

def calendarNumbers():    
    calendars = eval(input("\nEnter preffered number of calendars: "))
    for numbers in range(calendars):
        buildingCalendar()
        print("\n")
#Calling function to print any number of preffered calendars
#User inputs the values of n and d everytime
print("This is a program to build any number of calenders, preferrably 5 calenders")
calendarNumbers()
print("")



'''Activity 4 - LEAP YEAR
This program will accept a value and check whether it is a leap year or not'''
def check4Leap():
    n = eval(input("Enter your year here: "))

    if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
        print("LEAP YEAR")
    else:
        print("NOT LEAP YEAR")
#Calling function to check for LEAP YEAR
print("This program will check if your year is a Leap year or not")
check4Leap()
print("")



''''
Activity 5
This program will print 50 asterisks when user inputs
a positive integer.
It will arrange on one line, a number of the asterisks n, given by the user
'''
def asteriskPattern():
    digit = eval(input("Enter positive figure here: "))    

    if digit > 0:
        n = eval(input("\nHow many asterisks on one line: "))
        for i in range(1,51):
            print("*",end=" ")
            if (i+n)%n == 0:
                print(" ")
    else:
        print("\nI told you not to type a negative digit\nNow you will not see any pattern\nGo and be sad")
        return 0;
#Calling Function to print Asterisks pattern
print("This program will print a pattern for you by arranging asterisks")
print("Do not input a negative figure")
asteriskPattern()
print("")






#TASK 6
'''
This program will remove occurrences of elements in
the respective lists and display the New List with
the removed elements 
'''
def removeElement():
    list1 = [1,2,3,4]
    print("\nList 1 = ",list1,"\nElement_to_remove = 2")
    list1.remove(2)
    print("New list = ",list1,"\n")

    list2 = [3,3,2,1]
    print("\nList 2 = ",list2,"\nElements_to_remove = 3")
    while list2.count(3) > 0:
        list2.remove(3)
        print("New list = ",list2)

    list3 = ["a", "b", "c", "b"]
    print("\nlist 3 = ",list3,"\nElements_to_remove = b")
    while list3.count('b') > 0:
        list3.remove('b')
        print("New list = ",list3)

    list4 = []
    if not list4:
        print("\nEmpty List")
    else:
        print("\nNot Empty")
#Calling function that remove elements from list

print("\nThis program is displaying a list, and removing selected elements")
removeElement()
