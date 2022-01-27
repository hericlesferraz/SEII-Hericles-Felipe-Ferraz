# Importando biblioteca do socket
import socket
import sys

# Definindo postas e conexões
TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006

# Definindo Buffer
buf = 1024

# Pegando o primeiro argumento do usuario e passando para a variavel file_name
file_name = sys.argv[1]

try:
    # Configurando e estabelendo conexao o socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((TCP_IP, FILE_PORT))

    # Configurando o publisher, ou iniciando o server
    # Encodificando para enviar como utf-8
    sock.send(file_name.encode("utf-8"))
    sock.close()

    print("Sending %s ..." % file_name)

    # Enviando o arquivo com modo leitura
    f = open(file_name, "rb")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Estabelecendo conexões
    sock.connect((TCP_IP, DATA_PORT))
    data = f.read()
    sock.send(data)

finally:
    # Finaliza e fecha o arquivo
    sock.close()
    f.close()
