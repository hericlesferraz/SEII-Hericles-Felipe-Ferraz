import socketio
import time

socket = socketio.Client(reconnection=True)

global count
count = 0

@socket.event
def connect():
    print('Conectado com o servidor')
     
@socket.event
def light(data):
    print(data)
    print(f"Response: ")

@socket.event
def connect_error():
    print("Falha na conexão")

@socket.event
def disconnect():
    print('Desconectado pelo servidor')

if __name__ == '__main__':
    while True:
        try:
            socket.connect('http://localhost:5000')
            socket.wait()  
        except:
            time.sleep(1) 
            print('Falha na Conexão')
