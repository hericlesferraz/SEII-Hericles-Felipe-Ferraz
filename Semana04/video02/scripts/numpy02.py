'''

Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022

'''

import numpy as np
import matplotlib.pyplot as plt

# Efetuando a criacao de cada um dos arrays

a1 = np.array([3,5,7,3])
a2 = np.zeros(10)
a3 = np.ones(10)
a4 = np.random.random(10)
a5 = np.random.randn(10)
a6 = np.linspace(0, 10, 100)
a7 = np.arange(0, 10, 0.02)

# Efetuando operacoes basicas

print("2.a1 = ", 2*a1)
print("1/a1 = ", 1/a1)
print("a1 > 4 = ", a1 > 4)
print("1/a1 + a1 + 2 = ", 1/a1 + a1 + 2)

x = np.linspace(0, 1, 100)

print("x = ", x)
print("x^2 = ", x**2)

plt.plot(x, x**2)
plt.savefig('../figs/numpy02_fig_01.png', dpi=100)
plt.show()

plt.hist(a4)
plt.savefig('../figs/numpy02_fig_02.png', dpi=100)
plt.show()

def f(x):
	return x**2 * np.sin(x) / np.exp(-x)

x = np.linspace(0, 10, 100)
y = f(x)

plt.plot(x, y)
plt.savefig('../figs/numpy02_fig_03.png', dpi=100)
plt.show()

