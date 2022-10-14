def avg():
    map1 ={}
    map2 ={}
    list1=[("maria",10),("Bob",8),("Maria",17),("Bob",5),("Ewura Ama",20)]

    for i in list1:
        if i[0] in map1:
            map1[i[0]] = (map1[i[0]])+","+str(i[1])
        else:
            map1[i[0]]=str(i[1])

    for j in map1:
        string1 = map1[j]
        list1 = [int(n) for n in string1.split(",")]
        map2[j] = len(list1)
        map1[j] = sum(list1)
        print(j+"'s","average score is", (map1[j]/map2[j]))

avg()
