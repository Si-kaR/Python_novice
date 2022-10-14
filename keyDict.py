
'''
def checkDiction1():
    
    adict = {"a":4, "b": 6}
    key = "a"
    
    if key in adict:
        return True
    else:
        return False

    

print(checkDiction1())



def checkDiction3():
    
    adict = {}
    key = "d"
    
    if key in adict:
        return True
    else:
        return False

print(checkDiction3())


'''
def checkDiction2(adict, key):
    
    if key in adict:
        return True
    else:
        return False

checkDiction2({"a":4, "b": 6},"a")
print(checkDiction2({"a":4, "b": 6},"a"))
checkDiction2({"a":4, "b": 6},"c")
print(checkDiction2({"a":4, "b": 6},"c"))
checkDiction2({}, "d")
print(checkDiction2({},"d"))






































