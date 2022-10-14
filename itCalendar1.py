'''This program will build a calendar
n = number of days in the month
d = the position of the day starting the month
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
        if (i+d) % 7 == 0:
            print(" ")
        i = i + 1



buildingCalendar(30,5)
