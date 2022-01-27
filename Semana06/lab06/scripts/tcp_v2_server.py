#!/usr/bin/python3

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5
#port = 15000

def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address= (host, port)
    print('Servidor ativo em %s na porta %s' %server_address)
    sock.bind(server_address)

    sock.listen(backlog)
    while True:
        print("Esperando por nova conexao!!")
        client, address = sock.accept()
        data = client.recv(data_payload)
        if data:
            print('Data: %s' %data)

            client.send(data)
            print('data: ',data, 'address: ', address)
        
    client.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socker de Exemplo')

    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port

    echo_server(port)