#11. Write a program that asks the user for a number in the range of 1 through 7.
#The program should display the corresponding day of the week,
#where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday,
#5 = Friday, 6 = Saturday, and 7 = Sunday.
#The program should display an error message if the user enters
#a number that is outside the range of 1 through 7.

user = int(input("Enter your value here: "))
print("")

if 1 <= user <= 7:
    print(f"1 = Monday")
    print(f"2 = Tuesday")
    print(f"3 = Wednesday")
    print(f"4 = Thursday")
    print(f"5 = Friday")
    print(f"6 = Satday")
    print(f"7 = Sunday")
