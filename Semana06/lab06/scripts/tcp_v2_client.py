#!/usr/bin/python3

import socket
import sys
import argparse

host = 'localhost'
data_payload = 2048
backlog = 5
#port = 15000

def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address= (host, port)
    print('Servidor ativo em %s na porta %s' %server_address)
    sock.connect(server_address)

    try:
       message = 'Testando mensagem'
       print('Envaindo %s' %message)
       sock.sendall(message.encode('utf-8'))

       amount_received = 0
       amount_expected = len(message)

       while amount_received < amount_expected:
           data = sock.recv(16)
           amount_received += len(data)
           print('Recebido %s' %data)

    except socket.error as e:
        print('Erro no Socket: %s' %str(e))

    except Exception as e:
        print('Erro : %s' %str(e))

    finally:
        sock.close()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Socker de Exemplo')

    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port

    echo_client(port)