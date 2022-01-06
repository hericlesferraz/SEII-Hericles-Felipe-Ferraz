'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

language = 'Python'
if language=='Python':
    print('Language is Python')
else:
    print('No match')

language = 'Java'
if language=='Python':
    print('Language is Python')

elif language == 'Java':
    print('Language is Java')

elif language == 'JavaScript':
    print('Language is JavaScript')

else:
    print('No match')

user = 'Admin'
logged_in = True
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds' )

user = 'Admin'
logged_in = False
if not logged_in:
    print('Please Log In')
else:
    print('Welcome')

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a)) 
print(id(b)) 
print(a is b) 

a = [1, 2, 3]
b = [1, 2, 3]
print(id(a)) 
print(id(b)) 
print(a == b) 

condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')