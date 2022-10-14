
'''Problem 3'''
#This prpogram calculates the income of the user, as well as taxes related.
#it also calculates for the for the extra time spent working
def payroll(workHours, hourly_payRate):
    print("\nThis program calculates payroll")  

    if workHours > 40:
        overTime = workHours - 40
        overTimeWage = overTime * (1.5*hourly_payRate)
        income = 40 * hourly_payRate
        grossSalary = income + overTimeWage
        overTimeTax = 0.015 * overTimeWage
        incomeTax = 0.015*overTimeWage
        incomeTax = 0.1*income
        netIncome = (income - incomeTax) + (overTimeWage - overTimeTax)
        print("\nYour Gross Salary is $", format(grossSalary,'.2f'))
        print("Your incomeTax is $", format(incomeTax,'.2f'))
        print("Your OvertimeTax is $", format(overTimeTax,'.2f'))
        print("Your net Incomme is $", format(netIncome,'.2f'))
    else:
        grossSalary = workHours * hourly_payRate
        incomeTax = 0.1 * grossSalary
        netIncome = grossSalary - incomeTax
        print("\nYour Gross Salary is $", format(grossSalary,'.2f'))
        print("Your Income Tax is $", format(incomeTax,'.2f'))
        print("Your net income is $", format(netIncome,'.2f'))




payroll(80,20)
payroll(60,20)
payroll(40,20)
