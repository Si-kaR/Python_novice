
#. Tip, Tax, and Total
#Write a program that calculates the total amount of a meal purchased at a restaurant. The
#program should ask the user to enter the charge for the food, then calculate the amounts of 
#a 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

#1. input( receive info from user)
foodCharge = float(input("Enter charge for food: $"))
print("")

#2. process (calculate the info)
TIP_PERCENTAGE = .18
SALES_TAX = .07

tip = (foodCharge * TIP_PERCENTAGE)
salesTax = (foodCharge * SALES_TAX)
totalAmount = foodCharge + tip + salesTax

#3. output (display the info)
print(f"Amount charged on meal was: $", format(foodCharge, ",.2f"), sep='')
print(f"Amount deducted as Tip Percentage was: $", format(tip, ",.2f"), sep='')
print(f"Amount deducted as Sales Tax was: $", format(salesTax, ",.2f"), sep='')
print(f"Total Amount is $", format(totalAmount, ",.2f",), sep='')




