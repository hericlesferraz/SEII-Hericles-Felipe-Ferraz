'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''
import os

try:
    name_archive = 'file.txt'
    f = open(name_archive)
    print('Arquivo existente, excluindo arquivo: ')

    os.remove(name_archive)

except FileNotFoundError as e:
    print(e, 'Arquivo nao existe')
    os.system('touch ' + str(name_archive))

except Exception as e:
    print('Error')

else:
    print(f.read())
    f.close()

finally:
    print("Fim do processamento")