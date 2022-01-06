'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

import os
from datetime import datetime

os.chdir("/home/hericles")
print(dir(os))
print(os.getcwd())
os.makedirs("diretoriocriado/Sub-Dir-1")
os.removedirs("diretoriocriado/Sub-Dir-1")
os.system(str("touch READ.ME"))
os.rename('READ.ME', 'LEIA.ME')

print(os.stat('LEIA.ME').st_size)
mod_time = os.stat('LEIA.ME').st_mtime
print(datetime.fromtimestamp(mod_time)) 
print(os.listdir())

for dirpath, dirnames, filenames in os.walk('C:'):
    print('Current Path: ', dirpath)
    print('Directories: ', dirnames)
    print('Files: ', filenames)

print(os.path.basename('prog02.py'))
print(os.path.split('prog02.py'))
print(os.path.splitext('prog02.py'))