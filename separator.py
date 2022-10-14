def separate():
    agender = [1,"mankind",7.7,456,10,"b", True, False]

    string = []
    integer = []
    boolean = []  
    

    for element in agender:
        if type(element) is str:
            string.append(element)
        elif type(element) is int:
            integer.append(element)
        elif type(element) is bool:
            boolean.append(element)

    print(string)
    print(integer)
    print(boolean)
    
separate()



