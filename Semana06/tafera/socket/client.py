# Importando bibliotecas
import socket
import threading
import time

# Definindo portas
PORT = 5050

# Definindo tipo de codificação
FORMATO = "utf-8"

# Definidno o ip
SERVER = "192.168.0.109"
ADDR = (SERVER, PORT)

# Efetuando conexões
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def handle_mensagens():
    while True:
        msg = client.recv(1024).decode()
        mensagem_splitada = msg.split("=")
        print(mensagem_splitada[1] + ": " + mensagem_splitada[2])


# Funca que efetua o envio na codificação configurada
def enviar(mensagem):
    client.send(mensagem.encode(FORMATO))


# Funcao que envia a mensagem dada no input
def enviar_mensagem():
    mensagem = input()
    enviar("msg=" + mensagem)


def enviar_nome():
    nome = input("Digite seu nome: ")
    enviar("nome=" + nome)


# Funcao para efetuar o inicio do envio da mesnag
def iniciar_envio():
    enviar_nome()
    enviar_mensagem()


# Definindo thereas que serão utilizadas
def iniciar():
    thread1 = threading.Thread(target=handle_mensagens)
    thread2 = threading.Thread(target=iniciar_envio)
    thread1.start()
    thread2.start()


iniciar()
