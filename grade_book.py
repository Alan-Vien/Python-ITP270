#!/bin/python3

Subjects = ["Physics", "Calculus", "Poetry", "History"]

Grades = [98, 97, 85, 88]

Gradebook = [[Subjects[0], Grades[0]], 
             [Subjects[1], Grades[1]], 
             [Subjects[2], Grades[2]], 
             [Subjects[3], Grades[3]]]

print("Current Gradebook:", Gradebook)

Gradebook.append(["Computer Science", 100])

Gradebook.append(["Visual Arts", 93])

Gradebook[5][1] += 5

Poetry_Grade = Grades[2]
Gradebook.remove(["Poetry", Poetry_Grade])

Gradebook.append(["Poetry", "Pass"])

Last_Semester_Gradebook = [["Political Science", 90], ["Chemistry", 82], ["Philosophy", 95], ["Art History", 88]]
Full_Gradebook = Last_Semester_Gradebook + Gradebook

print("Full Gradebook including the Last Semester Grades:", Full_Gradebook)
