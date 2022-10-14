'''This program prints a calender but for a society that has 8 days in a week'''
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


calendarNumbers()
