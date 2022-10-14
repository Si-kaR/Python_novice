'''Problem 1'''
#This function will print values ranging from 0 to 100,inclusive and tatek these as values in Celsius.
#It will then find the Fahrenheit conversion of each of the values.
#Finally, it will print this data in a tabular form
def converT():
    print("\nThis program will convert celsius Temperatures ranging from 0 to 100 \ninto Fahrenheit in a tabular form\n")
    print("{0:10}{1}".format("Celsius", "Fahrenheit"))
    
    for celsius in range(101):       
            F = (0.5*celsius) + 32
            print("{0:<10}{1:<10}".format(celsius, F))   
converT()

#This program accepts integer inputs and arrange them in a list.
#It will stop accepting input when the user enter a value zero (0)
#it will then arrange the values as a list while arranging the values from lowest to highest
def sortings():
    print("\nThis next program will print and compile a list for values given by the user.\nIt will stop when a zero(0) is given")
    print("\nEnter the first value below. Enter 0 to see your list")
    
    store = []
    while True:
        ask = int(input())
        if ask == 0:
            break
        else:
            store.append(ask)
            
    store.sort()
    print(store)
sortings()

'''Problem 2'''
#This program will ask for the number class a user has. The program will loop the number of class
#with each loop it wil ask for the name of the class and grade obtained for that class
#it will then display this result and display a calculated GPA for the grades
def reportGpa():
    print("\nThis program will calculate GPA pf a student based on the number of \ntimes he or she attended class and the grade \nobtained in each of them.")
    times = int(input("\nHow many classes did you take: "))

    classList = []
    gradeList = []
    
    for running in range(times):
        Class = str(input("\nName of class? "))
        Grade = int(input("What was the grade for this class? "))

        classList.append(Class)
        gradeList.append(Grade)

    print("\nreport card".upper())

    for allGrades in range(len(classList)):
        print(classList[allGrades],"  -  ",gradeList[allGrades])

    final = (sum(gradeList))/(len(gradeList))
    print("Overall GPA - ", final)
reportGpa()    

'''Problem 3'''
#This prpogram calculates the income of the user, as well as taxes related.
#it also calculates for the for the extra time spent working
print("This program calculates payroll")
workHours = int(input("\nEnter number of hours spent working: "))
incomePerHour = int(input("Enter the pay per hour: "))

if workHours > 40:
    overTime = workHours - 40
    overTimeWage = overTime * (1.5*incomePerHour)
    income = 40 * incomePerHour
    grossSalary = income + overTimeWage
    overTimeTax = 0.015 * overTimeWage
    incomeTax = 0.015*overTimeWage
    incomeTax = 0.1*income
    netIncome = (income - incomeTax) + (overTimeWage - overTimeTax)
    print("Your Gross Salary is", format(grossSalary,'.2f'))
    print("Your incomeTax is", format(incomeTax,'.2f'))
    print("Your OvertimeTax is", format(overTimeTax,'.2f'))
    print("Your net Incomme is", format(netIncome,'.2f'))
else:
    grossSalary = workHours * incomePerHour
    incomeTax = 0.1 * grossSalary
    netIncome = grossSalary - incomeTax
    print("Your Gross Salary is ", format(grossSalary,'.2f'))
    print("Your Income Tax is ", format(incomeTax,'.2f'))
    print("Your net income is ", format(netIncome,'.2f'))
