'''This program will build a calendar
n = number of days in the month
d = the position of the day starting the month
It will accepts input arguments n and d
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











        

buildingCalendar(30,5)
print("\n")
buildingCalendar(31,2)
print("\n")
buildingCalendar(29,4)

