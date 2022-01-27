# Importando bibliotecas
import socket
import select

# Definindo postas e conexões
UDP_IP = "127.0.0.1"
IN_PORT = 5005

# Definindo timer
timeout = 3

# Configurando e estabelendo conexao o socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, IN_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    if data:
        print("File name:", data)

        # Organizando o nome para leitura
        file_name = data.strip()

    # Recebendo o arquivo com modo escrita
    f = open(file_name, "wb")

    while True:
        # Efetuando seleção do socket
        ready = select.select([sock], [], [], timeout)
        if ready[0]:
            # Efetuando leitura
            data, addr = sock.recvfrom(1024)
            f.write(data)
        else:
            # Encerrando o arquivo
            print("%s Finish!" % file_name)
            f.close()
            break
