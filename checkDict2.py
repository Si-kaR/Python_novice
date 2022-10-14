'''def forAllDict():
    adict = {"a":4,"b":4,"c":4}
    v = list(adict.values())
    v[0]
    list(adict.values())[0]
print(forAllDict())
'''


adict = {}
bowl = adict.values()
emptyCup = []

for item in bowl:
    emptyCup.append(item)
fullCup = emptyCup
if len(fullCup) == 0:
    print("Empty")
else:    
#fullCup = [4, 4, 4]
    x = fullCup[0]
    empty = []
    for comparables in fullCup[1:]:
        if comparables !=x:
            empty.append(comparables)
    if len(empty) ==0:
        print("True")
    else:
        print("False")
    


    

#print(fullCup)


