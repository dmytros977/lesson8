#a = input()
#def counthrees(self):
#            counttri = 0
#            for studen in studinfos:
#                if student.markFacultyofPhilology == 3
from math import gamma
from sys import api_version

#u = 0
#s = 0
#t = 0
#for m in a:
#    if m=='2':
#       u +=1
#    elif m in grades:
#       s += 1
#        t += int(m)
#print(u)
#print(t / s if s > 0 else 0)
#, 'Bilbo':int(input()), 'Steve':int(input()), 'Khendirk':int(input()), 'Aaron':int(input())
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades[0] = sum(grades[0]) / len(grades[0])
grades[1] = sum(grades[1]) / len(grades[1])
grades[2] = sum(grades[2]) / len(grades[2])
grades[3] = sum(grades[3]) / len(grades[3])
grades[4] = sum(grades[4]) / len(grades[4])
resoult = dict(zip(sorted(students), grades))
print(resoult)



#marks = {'Bill': int(input()), 'Jane': int(input()), 'John': int(input()), 'Mary': int(input())}

#average = 0

#for key in students.keys():

#   average += students[key]

#print(round(average / 4))
#a = {'Johnny':[5,3,3,5,4]}
#b = {'Bilbo':[2,2,2,3]}
#c = {'Steve':[4,5,5,2]}
#d = {'Khendrik':[4,4,3]}
#e = {'Aaron':[5,5,5,4,5]}

#a = input()
#marks = ['2', '3', '4', '5']  # Учитываемые оценки
#u = 0  # Количество неудов
#s = 0  # Количество оценок
#t = 0  # Сумма оценок

## Цикл исключает неверные символы
#for m in a:
#    if m == '2':
#        u += 1
#    elif m in marks:
#        s += 1
#        t += int(m)
#
#print(u)
#print(t / s if s > 0 else 0)  # Исключение деления на 0