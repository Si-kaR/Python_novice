alist = [40,45,52,53,58,34,43,50,47,48,50,50,47,34,32,44,45,46,47,48,48,51,51,52,53,51,52,53,54,40,41,43,45,46,48,43,46,47,30,31,28,31,28,45,51,51]

def frequencyTableAlt(alist):
    print("ITEM","FREQUENCY")
    slist = alist[:]
    slist.sort()

    countlist = [ ]

    previous = slist[0]
    groupCount = 0
    for current in slist:
        if current == previous:
            groupCount = groupCount + 1
            previous = current
        else:
            print(previous, "   ", groupCount)
            previous = current
            groupCount = 1



frequencyTableAlt(alist)
