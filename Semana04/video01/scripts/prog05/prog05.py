'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
print(student['name'])
print(student['courses']) 
print(student['age']) 
print(student.get('name'))
print(student.get('phone'))
print(student.get('phone', 'Not Found'))

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
student['phone'] = '555-5555'
student['name'] = 'Jane'
print(student)

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
student.update({'name': 'Jane', 'age': 26, 'phone': '555-5555'})
print(student)

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}
del student['age']
print(student)

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}

age = student.pop('age')
print(age) 
print(len(student))

student = {'name': 'John', 'age':25, 'courses':['Math', 'CompSci']}

print(student.keys()) 
print(student.values()) 
print(student.items()) 

for key,value in student.items():
    print(key,value)
