'''

Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022

'''

import numpy as np
import matplotlib.pyplot as plt

# Array Indexing/Slicing

a1 = np.array([2,4,6,8,10])

print("a1[2] =", a1[2])
print("a1[2:] =", a1[2:])
print("a1[:-2] =", a1[:-2])
print("a1[1:-2] =", a1[1:-2])
print("a1[a1>3] =", a1[a1>3])

names = np.array(['Jim', 'Luke', 'Josh', 'Pete'])

first_letter_j = np.vectorize(lambda s: s[0])(names)=='J'
f = lambda s: s[0]

print("f('animal') =", f('animal'))

print("names[first_letter_j] =",names[first_letter_j])

print("a1[a1%4 == 0] = ",a1[a1%4 == 0])
