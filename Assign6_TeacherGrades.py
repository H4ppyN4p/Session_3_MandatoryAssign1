print('its alive')

gradesDict = {
'Ganizani' : '80',
'Timon' : '80',
'Ladislas' : '90',
'Tanvi' : '90',
'Georgianna' : '90',
'Ernest' : '80',
'Sonja' : '80',
'Sedna' : '90',
'Mowgli' : '80',
'Musa' : '90',
'Cyra' : '80',
'Natanail' : '90'
}


studentsToUpdate = ['Timon', 'Tanvi', 'Sedna', 'Max']

def updateGrades(listOfStudents):
    for student in listOfStudents:
        if student in gradesDict:
            print('Choose ' + student + '-s new grade')
            newGrade = input()

            gradesDict[student] = newGrade

    for student in gradesDict:
        if int(gradesDict[student]) >= 85:
            print(student + ' their grade is: ' + gradesDict[student])  

updateGrades(studentsToUpdate)        