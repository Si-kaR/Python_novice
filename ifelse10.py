#6. Write an if-else statement that assigns 0 to the variable b
#if the variable a is less than 10. 
#Otherwise, it should assign 99 to the variable b.

a = int(input("Enter your a-value: "))
print("")

if a < 10:
    print(f"Your value {a} is less than 10")
    print(f"It satisfy the requirement so you are assigned")
    print(f"b = 0")
else:
    print(f"Your value {a} is greater than 10")
    print(f"It does not satisfy the requirement so you are assigned")
    print(f"b = 99")
