from flask import Flask, request, render_template 
from flask_socketio import SocketIO
from multiprocessing import Process
import threading
import eventlet
from eventlet import wsgi

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

def start_Flask():
    print("Starting server...")
    wsgi.server(eventlet.listen(('', 5000)), app)     

@app.route('/light_hall')
def light_hall():
    SampleApp().run().modify_btn1()
    return render_template('index.html', response='Luz da Sala')

@app.route('/light_room')
def light_room():
    print('hello')
    return render_template('index.html', response='Luz do Quarto')

@app.route('/light_kitchen')
def light_kitchen():
    print('hello')
    return render_template('index.html', response='Luz da Cozinha')

@app.route('/light_bathroom')
def light_bathroom():
    print('hello')
    return render_template('index.html', response='Luz do Banheiro')

@app.route('/light_library')
def light_library():
    print('hello')
    return render_template('index.html', response='Luz da Biblioteca')

@app.route('/') 
def main():
    response = None
    return render_template('index.html', response=response)

class SampleApp(App):
    def build(self):
        print('No  build')
        layout = GridLayout(cols=2)
        self.btn1 = Button(background_normal="imgs/hall_off.png", background_down="imgs/hall_on.png")
        self.btn2 = Button(background_normal="imgs/kitchen_off.png", background_down="imgs/kitchen_on.png")
        self.btn3 = Button(background_normal="imgs/room_strange_off.jpeg", background_down="imgs/room_strange_on.jpeg")
        self.btn4 = Button(background_normal="imgs/bathroom_off.jpeg", background_down="imgs/bathroom_on.jpeg")
        layout.add_widget(self.btn1)
        layout.add_widget(self.btn2)
        layout.add_widget(self.btn3)
        layout.add_widget(self.btn4)

        return layout

    def modify_btn1(self):
        self.btn1.trigger_action(1)
        self.btn2.trigger_action(0)

if __name__ == '__main__':
    global p1
    p1 = Process(target=start_Flask)    
    p1.start()                                
    SampleApp().run()
