# Importando biblioteca do socket
import socket

# Definindo postas e conexões
TCP_IP = "127.0.0.1"
FILE_PORT = 5005
DATA_PORT = 5006

# Definindo timer
timeout = 3

# Definindo Buffer
buf = 1024

# Configurando e estabelendo conexao o socket
sock_f = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_f.bind((TCP_IP, FILE_PORT))
sock_f.listen(1)

# Configurando o recebedor, ou listener
sock_d = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_d.bind((TCP_IP, DATA_PORT))
sock_d.listen(1)


while True:
    conn, addr = sock_f.accept()

    # Estabelece o recebimento com o servidor
    data = conn.recv(buf)
    if data:
        print("File name:", data)

        # Prepara o nome do arquivo
        file_name = data.strip()

        # Abre o arquivo em modo de escrita
        f = open(file_name, "wb")

    conn, addr = sock_d.accept()
    while True:
        data = conn.recv(buf)

        if not data:
            break
        f.write(data)

    # Decodificando para receber como utf-8
    print(data.decode("utf-8"))
    print("%s Finish!" % file_name)

    # Fecha arquivo
    f.close()
    break
