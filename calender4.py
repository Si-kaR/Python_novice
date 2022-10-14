def main():
    d = eval(input("Input the starting day (0=sun, 1=mon, ...): "))
    n = eval(input("Input the number of days in the month (28-31): "))

    
    i = 1
    while i <= n:
        if i < 10:#
            print("",i, end = " ")#
        else:#
            print(i, end = " ")# This was initially the original command
        if (i+d) % 7 == 0:
            print(" ")
        i = i + 1

        
        '''
        The lines of code with the    #    are the new iterations
        what is being said here is that, "When the value i scanned is less than 10, add a space to its front before printing it itself"
        Otherwise just print it as it is...with the previous (original conditions)
        This action will shift all values of i less than 10 a bit to the left.......this will make our previous version of the calendar a nicer one in this calendar'''

main()#Calling function


'''
Now, if I should make d = 4,
we will see that the spaces will be at the left side of our calender
Meaning, our program will start by counting 0,1,2,3 and on the 3rd position, it'll display 1 which represents the first day of that week.


In real life we don't see our calendars to be in that manner, so what we'll do is shift it such that
the program will start counting fromm the left to the right rather
See the next code 5
'''
