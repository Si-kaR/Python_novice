#8. Write a loop that prints out all numbers between 6 and 30 that are not divisible by 2, 3, or 5. 
#First approach
'''
def selection():

    for i in range(30):
        if i>6 and i<30:
            if i%2!=0:
                if i%3!=0:
                    if i%5!=0:
                        print(i)
selection()

#Second Approach
def selection():
    for i in range(30):
        if i>6 and i<30:
            if i%2!=0 and i%3!=0:
                if i%5!=0:
                    print(i)
selection()
      

def selection():
    for i in range(30):
        if i>6 and i<30:
            if (i%2!=0 and i%3!=0) and i%5!=0:
                print(i)
selection()



def selection():
    for i in range(30):
        if ((i>6 and i<30)and(i%2!=0 and i%3!=0)) and i%5!=0:
            print(i)
selection()
'''

def selection():
    for i in range(30):
        if (i>6 and i<30) and ((i%2!=0 and i%3!=0) and i%5!=0):
            print(i)
selection()
