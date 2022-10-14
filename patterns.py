def asteriskPattern():
    digit = eval(input("Enter positive figure here: "))

    

    if digit > 0:
        n = eval(input("\nHow many asterisks on one line: "))
        for i in range(1,51):
            print("*",end=" ")
            if (i+n)%n == 0:
                print(" ")
    else:
        print("You are only supposed to input positive integers.")
        return 0;        


asteriskPattern()
