def computeAmount():
    P=eval(input('Enter your principal'))
    r=eval(input('Enter your rate'))
    n=eval(input('Enter the number of times there was compounding'))
    t=eval(input('Enter the number of years'))
    Amount= P * (1 + r/n)**(n/t)
    print(Amount)
