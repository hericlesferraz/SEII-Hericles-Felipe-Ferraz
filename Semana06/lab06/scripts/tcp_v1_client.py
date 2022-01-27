#!/usr/bin/python3

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address= ('localhost', 15000)
print("Conectando a - {}:{}".format(*server_address))
    
try:
    sock.connect(server_address)
    msg = b'Mensagem enviada pelo cliente'
    tam = len(msg)

    for i in range(5):
        inp = input('Pressione enter para continuar :')
        
        print(i+1, msg)
        sock.sendall(msg)

        recebido = 0
        while recebido < tam:
            data = sock.recv(100)
            recebido += len(data)
            print('{!r}'.format(data))


finally:
    print('Finalizando a conexão: ')
    sock.close()