'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

def hello_func():
    print('Hello Function')

print('func 0 ',hello_func) 

hello_func()

def hello_func1():
    return 'Hello Function'

print(hello_func1().upper())

def hello_func2(greeting, name='You'):
    return '{}, {}'.format(greeting,name)

print('func2: ', hello_func2('Hi', name = 'Corey'))

def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

courses = ['Math', 'Art']
info = {'name': 'John', 'age': 22}

student_info(courses, info)
student_info(*courses, **info)

month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    if not 1 <= month <= 12:
        return 'Invalid Month'

    if month == 2 and is_leap(year):
        return 29

    return month_days[month]

print(days_in_month(2021, 2))