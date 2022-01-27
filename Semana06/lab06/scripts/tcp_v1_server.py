#!/usr/bin/python3

import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address= ('localhost', 15000)
sock.bind(server_address)

sock.listen(1)

while True:
    print("Esperando por nova conexao!!")
    connection, client_address = sock.accept()
    
    try:
        while True:
            data = connection.recv(100)
            print('recebido :{!r}'.format(data))

            if data:
                print('reenviando estrutura para o cliente: ', client_address)
                connection.sendall(data)

            else:
                print('Não foi recebido nenhum dado: ', client_address)
                break
    finally:
        connection.close()