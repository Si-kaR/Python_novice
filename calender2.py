def main():
    #     d = number of days....make it start from 0 = sunday to 6 = saturday...this sums up to 7days
    d = eval(input("Input the starting day (0=sun, 1=mon, ...): "))
    #    n = number of months....should be from 28 for February to 31 for the highest number of days in the month
    n = eval(input("Input the number of days in the month (28-31): "))

    
    '''
    from our initial version, our code printed the number of days in a vertical manner
    now we want it to print in a horizontoal manner
    we use the in-built command below
    end = ""

    What that command will do is that, when i is printed, then the LOOP will pause there, and introcude a space, before running again to print the next value
    This will result in us having the (number of days being printed in the horizontal manner
    '''
    
    i = 1
    while i <= n:
        print(i, end = " ")
        i = i + 1

main()# This is to call our function
'''Now bare in mind, we're building a Calendar....Calenders don't look sooo linear.
   Our next task will be to break our linear (number of days, such that it'll arrange to look like what calenders look like)
'''
