'''Problem 2'''
#This program will ask for the number class a user has. The program will loop the number of class
#with each loop it wil ask for the name of the class and grade obtained for that class
#it will then display this result and display a calculated GPA for the grades
''' Forumlar = sum of all grades / TOTAL NUMBER of grades'''
def reportGPA(Class, Grade):
    print("\nThis program will calculate GPA of a student based on the number of \ntimes he or she attended class and the grade \nobtained in each of them.")
    times = 3
    print("\nNumber of classes taken is: ", times)

    classList = []
    gradeList = []
    
    for running in range(times):

        classList.append(Class)
        gradeList.append(Grade)

    print("\nreport card".upper())

    for allGrades in range(len(classList)):
        print(classList[allGrades],"  -  ",gradeList[allGrades])

    final = (sum(gradeList))/(len(gradeList))
    print("Overall GPA - ", final)
    return final;
    
reportGPA("English", 45)  
reportGPA("French", 89)
reportGPA("Spanish", 12)
