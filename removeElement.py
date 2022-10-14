def removeElement():
    list1 = [1,2,3,4]
    print("\nList 1 = ",list1,"\nElement_to_remove = 2")
    list1.remove(2)
    print("New list = ",list1,"\n")

    list2 = [3,3,2,1]
    print("\nList 2 = ",list2,"\nElements_to_remove = 3")
    while list2.count(3) > 0:
        list2.remove(3)
        print("New list = ",list2)

    list3 = ["a", "b", "c", "b"]
    print("\nlist 3 = ",list3,"\nElements_to_remove = b")
    while list3.count('b') > 0:
        list3.remove('b')
        print("New list = ",list3)

    list4 = []
    if not list4:
        print("\nEmpty List")
    else:
        print("\nNot Empty")

    

removeElement()
