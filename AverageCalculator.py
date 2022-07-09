from time import sleep

NumberGrade = ['First', 'Seconde','Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth', 'Eleventh', 'Twelfth', 'Thirteenth', 'Fourteenth', 'Fifteenth', 'Sixteenth', 'Seventeenth', 'Eighteenth', 'Nineteenth', 'Twentieth'] # Max number of Grade

print('Hello')
print('In this Average Calculator we are assuming every grade (up to 20 in a subject) are all coefficient 1 which mean they only count for 1')

NumberOfGradeInput = int(input('Number of grade: '))
if NumberOfGradeInput > 20:
    print('Error, Max Input 20')
if NumberOfGradeInput < 2:
    print('Error, Min Input 2')
else:
    x = 0
    GradeList = []
    while True:
        if x == NumberOfGradeInput:
            TotalGrade = sum(GradeList)
            TotalAverage = TotalGrade / len(GradeList)
            print('You have an average of :', TotalAverage)
            break
        Grade = int(input(NumberGrade[x]+': '))
        if Grade > 20:
            print('Error, Max Input 20')
            quit()
        else:
            GradeList.append(Grade)
            x = x + 1
            sleep(0.25)
