'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses) 
print(len(courses))
print(courses[0])
print(courses[3]) 
print(courses[-1]) 
print(courses[0:2])
print(courses[:2]) 
print(courses[2:])  
courses.append('Art')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.insert(0, 'Art')
print(courses)
courses_2 = ['Art', 'Education']
courses.insert(0, courses_2)
print(courses)
print(courses[0])

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_2 = ['Art', 'Education']
courses.extend([0, courses_2])
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.remove('Math')
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.pop()
print(courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
popped = courses.pop()
print(popped) 

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.reverse()

print(courses) 

courses = ['History', 'Math', 'Physics', 'CompSci']
courses.sort()

print(courses) 

nums = [1, 5 , 2, 4, 3]
nums.sort()

print(nums)

nums = [1, 5 , 2, 4, 3]
nums.sort(reverse=True)

print(nums)

courses = ['History', 'Math', 'Physics', 'CompSci']
sorted_courses = sorted(courses)

print(sorted_courses) 

nums = [1, 5 , 2, 4, 3]

print('min : ',min(nums)) 
print('max : ',max(nums)) 
print('sum : ',sum(nums)) 

courses = ['History', 'Math', 'Physics', 'CompSci']

print(courses.index('CompSci')) #3
print('Art' in courses)
print('Math' in courses)

courses = ['History', 'Math', 'Physics', 'CompSci']
for course in courses:
   print(course) #Segue abaixo o resultado

courses = ['History', 'Math', 'Physics', 'CompSci']
for index, course in enumerate(courses):
   print(index, course) #Segue abaixo o resultado

courses = ['History', 'Math', 'Physics', 'CompSci']
for index, course in enumerate(courses, start=1):
   print(index, course) #Segue abaixo o resultado

courses = ['History', 'Math', 'Physics', 'CompSci']
courses_str = ''
courses_str = ', '.join(courses)
new_list = courses_str.split(' - ')
print(courses_str) #History, Math, Physics, CompSci
print(new_list) #['History', 'Math', 'Physics', 'CompSci']

list_1 = ['History', 'Math', 'Physics', 'CompSci']
list_2 = list_1
list_1[0] = 'Art'
print(list_1) #['Art', 'Math', 'Physics', 'CompSci']
print(list_2) #['Art', 'Math', 'Physics', 'CompSci']

tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1) #('History', 'Math', 'Physics', 'CompSci')
print(tuple_2) #('History', 'Math', 'Physics', 'CompSci')

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print(cs_courses) #{'History', 'Math', 'Physics', 'CompSci'} aleatório

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
print('Math' in cs_courses) #True

cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
ar_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses.intersection(ar_courses)) #{'Math', 'History'}
print(cs_courses.difference(ar_courses)) #{'CompSci', 'Physics'}
print(cs_courses.union(ar_courses)) #{'History', 'Design', 'Art', 'Physics', 'CompSci', 'Math'}

#listas vazias
empty_list = []
empty_list = list()

#tuples vazias
empty_tuple = ()
empty_tuple = tuple()

#sets vazias
empty_set = {} #isso n é certo
empty_set = set() #certo