'''
Aluno: Hericles Felipe Ferraz
Matricula: 11811EMT022
'''

f = open('teste.txt', 'r')

print(f.name)
print(f.mode)

f.close()

with open('teste.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    
    f_contents = f.readlines()
    print(f_contents)

    f_contents = f.readline()
    print(f_contents)
    f_contents = f.readline()
    print(f_contents)
    
    f_contents = f.readline()
    print(f_contents, end='')
    f_contents = f.readline()
    print(f_contents, end='') 

    for line in f:
        print(line, end='')

    f_contents = f.read(100) 
    print(f_contents, end='')
    f_contents = f.read(100)
    print(f_contents, end='')
    f_contents = f.read(100)
    print(f_contents, end='')

    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)

    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f.seek(0)
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    

   
with open('test2.txt','w') as f:
    pass
    f.write('Test')
    f.seek(0)
    f.write('R')


with open('teste.txt', 'r') as rf:
    with open('teste_copy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


with open('imagem.jpg', 'rb') as rf:
   with open('imagem_copy.jpg', 'wb') as wf:
       for line in rf:
           wf.write(line)

with open('imagem.jpg', 'rb') as rf:
    with open('imagem_copy.jpg', 'wb') as wf:
        imagem_size = 4096
        rf_imagem = rf.read(imagem_size)
        while len(rf_imagem) > 0:
            wf.write(rf_imagem)
            rf_imagem = rf.read(imagem_size)

print(' Finish')