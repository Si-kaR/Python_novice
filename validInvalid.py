#8. Write an if-else statement that determines whether
#the points variable is outside the range 
#of 9 to 51. If the variable’s value is outside
#this range it should display “Invalid points.” 
#Otherwise, it should display “Valid points.

a = int(input("Enter your variable input: "))

if 9 <= a <= 51:
    print(f"Valid points")
else:
    print(f"Invaid points")
