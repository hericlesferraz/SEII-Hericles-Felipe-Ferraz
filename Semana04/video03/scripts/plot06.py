#plot06

'''

Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022

'''

import matplotlib.pyplot as plt
import numpy as np

# o metodo arange cria um array de um intervalo de inicio inteiro 'begin', ate um intervalo final inteiro 'end' 
# com o incremento inteiro 'inc': np.arange(begin, end, inc)
x1 = np.arange(0, 1000, 1)

# o comando plt.plot plota em um grafico 2d a relacao de um conjunto de pontos, de forma analoda ao scatter utilizado
# anteriormente
plt.plot(x1, x1**2)
plt.show()

x2 = np.arange(-1000, 1000, 1)

# o comando plt.plot plota em um grafico 2d a relacao de um conjunto de pontos, de forma analoda ao scatter utilizado
# anteriormente
plt.plot(x2, x2**2)
plt.show()