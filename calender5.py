def main():
    d = eval(input("Input the starting day (0=sun, 1=mon, ...): "))
    n = eval(input("Input the number of days in the month (28-31): "))
    for j in range(d):#
        print(" ", end = "  ")#

    i = 1
    while i <= n:
        if i < 10:
            print("",i, end = " ")
        else:
            print(i, end = " ")
        if (i+d) % 7 == 0:
            print(" ")
        i = i + 1

        '''

        # indicates our iterations
        We know from our previous iteration, that, every number column has two things
        1. either it has two digits
        or
        2. it has a SPACE and DIGIT (in the first line of code)


        The problem however is that the first line is not like what we see in real life, so we introduced the     # lines of code
        for j in range(d):#
        print(" ", end = " ")#


        Meaning, whhen the user states that he or she wants the days position to start from the 4th position, .......add 1SPACE jump and 2 DIGIT jump
        spaces to the columns for the (first and second things I said earlier)
        before eventually printing the first number 1 which represents the very first day

        So in our first line, we will have {(5 jumps) x 3} i.e (1SPACE and 2DIGIT)......before the position for 1 which will have 1SPACE and 1DIGIT being 1

        '''
        
        

main()# calling function
