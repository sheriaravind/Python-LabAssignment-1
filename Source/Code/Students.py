def Find_Students(Python, BigData):
    Common_List = []
    Un_Common_List = []
    for Student in Python:
        if Student in BigData:
            Common_List.append(Student)
            BigData.remove(Student)
        else:
            Un_Common_List.append(Student)

    print("Common list of students in both the subjects are: ",Common_List)
    print("Un Common list of students in both the subjects are: ", Un_Common_List + BigData)

if __name__ == '__main__':
    Python = ['John','Tom','Robert','Joey']
    BigData = ['Tom', 'Robert','Samuel']
    Find_Students(Python, BigData)