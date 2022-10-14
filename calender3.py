def main():
    #     d = number of days....make it start from 0 = sunday to 6 = saturday...this sums up to 7days
    #     d      is     (the index where the count 1 should start from ) in the month
    #     So if I say d = 5, it means the loop will count 0,1,2,3,4..............the 4 is the postion where the number 1 representing Monday or anyday
    #     starting the calender in real life will printed
    d = eval(input("Input the starting day (0=sun, 1=mon, ...): "))
    #    n = number of months....should be from 28 for February to 31 for the highest number of days(the index where the count 1 should start from ) in the month
    n = eval(input("Input the number of days in the month (28-31): "))
    
    '''
    In our intial code, we realise that, our (number of days) were being printed
    very horizontally (linear).
    It is a calendar, so we should try to make the number of days represent the weeks
    How will we get this?
    Seven days should be printed on the first line. This will mean one week
    next line should also have seven days
    and the next
    until finally the number of days can no longer be seven.



    To do this, use the the modular function
    (i+d) modulo 7 == 0
    or
    (i+d) % 7 == 0
    Now, what the above code will do is that, it'll take our total (number of days)
    which was printed, and when it is printed, it'll check if the outputs are equal to 7
    if they are, it'll go to the next line.
    How exactly does this work though?
    '''
    

    
    i = 1
    while i <= n:
        print(i, end = " ")
        if (i+d) % 7 == 0: 
            print(" ")
        i = i + 1

        '''
        # if (i+d) % 7 == 0:
        What the code above does is that,taking d, when i is being printed, it will account for the number of jumps (d = 3)the program had to do while choosing the initial position (index) to
        on which to display 1 which represents the start / first day on that calender
        so if d = 4,
        the first line should count 0,1,2,3 before displaying 1 (1 represents the first day on that calendar)
        so we will have some thing like what is below
        _ _ _ _ 1 2 3
        4 5 6 7 8 9 10
        11 12 13 14 15 16 17
        .........................all the way till were done with the vaalue given for the (number of days)...which should be between 28 and 31 because in real life,
        these are the range of days for the months
        '''

main()#calling function

# Our next task will be to arrange our digits (days) nicely

