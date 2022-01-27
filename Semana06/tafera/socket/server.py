# Importando bibliotecas
import socket
import threading
import time

# Forma usual de pegar o ip
SERVER_IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (SERVER_IP, PORT)

# Codificação da mensagem
FORMATO = "utf-8"

# Definindo o servidor
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

# Definindo arrays que serão necessários
conexoes = []
mensagens = []

# Funcao para possibilar envio de forma individual
def enviar_mensagem_individual(conexao):
    print(f"[ENVIANDO] Enviando mensagens para {conexao['addr']}")
    for i in range(conexao["last"], len(mensagens)):
        mensagem_de_envio = "msg=" + mensagens[i]
        conexao["conn"].send(mensagem_de_envio.encode())
        conexao["last"] = i + 1
        time.sleep(0.2)


# Funcao para possibilar envio geral
def enviar_mensagem_todos():
    global conexoes
    for conexao in conexoes:
        enviar_mensagem_individual(conexao)


# Funcao para possibitar conexao de varis clientes
def handle_clientes(conn, addr):
    print(f"[NOVA CONEXAO] Um novo usuario se conectou pelo endereço {addr}")
    global conexoes
    global mensagens
    nome = False

    while True:
        # Definindo tamanho máximo de tamanho de mensagem
        msg = conn.recv(1024).decode(FORMATO)
        if msg:
            if msg.startswith("nome="):
                mensagem_separada = msg.split("=")
                nome = mensagem_separada[1]
                mapa_da_conexao = {"conn": conn, "addr": addr, "nome": nome, "last": 0}
                conexoes.append(mapa_da_conexao)
                # Definindo mensagem para todos
                enviar_mensagem_individual(mapa_da_conexao)
            elif msg.startswith("msg="):
                # Garantindo que a mensagem chegue ordem correta
                mensagem_separada = msg.split("=")
                mensagem = nome + "=" + mensagem_separada[1]
                mensagens.append(mensagem)
                enviar_mensagem_todos()


# Inicaind cominicação
def start():
    print("[INICIANDO] Iniciando Socket")
    server.listen()
    while True:
        # Criando Thread para possibitar execução continua individual e geral
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_clientes, args=(conn, addr))
        thread.start()


# Executando inicialização
start()
