def check4Leap():
    n = eval(input("Enter your year here: "))

    if n % 4 == 0 and not(n % 100 == 0) and(n % 400 == 0):
        print("LEAP YEAR")
    
    else:
        print("NOT LEAP YEAR")



check4Leap()
