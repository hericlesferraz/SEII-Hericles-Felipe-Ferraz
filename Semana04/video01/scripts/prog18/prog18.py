'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

x = 'global x'

def test():
    global x
    x = 'local x'
    print(x)

test()
print(x)

import builtins
def mins():
    pass

m = mins([5, 1, 4, 2, 3])
print(m)

def test(z):
    x = 'local x'
    print(z)

test('local z')
x = 'global x'

def outer():
    x = 'outer x'

    def inner():
        x = 'inner x'
        print(x)
        
    inner()
    print(x)

outer()
