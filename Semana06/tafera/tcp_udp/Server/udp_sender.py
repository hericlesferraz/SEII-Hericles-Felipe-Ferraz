# Importando bibliotecas
import socket
import time
import sys

# Definindo postas e conexões
UDP_IP = "127.0.0.1"
UDP_PORT = 5005

# Definindo buffer
buf = 1024

# Pegando o primeiro argumento do usuario e passando para a variavel file_name
file_name = sys.argv[1]

# Configurando e estabelendo conexao o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.send(file_name, (UDP_IP, UDP_PORT))
print("Sending %s ..." % file_name)

# Enviando o arquivo com modo leitura
f = open(file_name, "r")
data = f.read(buf)
while data:

    # Estabelecendo conexões
    if sock.sendto(data, (UDP_IP, UDP_PORT)):
        data = f.read(buf)
        data.encode("utf-8")

        # Timer para salvar o arquivo
        time.sleep(0.02)  #

# Fechando conexões
sock.close()

# Fechando arquivo
f.close()
