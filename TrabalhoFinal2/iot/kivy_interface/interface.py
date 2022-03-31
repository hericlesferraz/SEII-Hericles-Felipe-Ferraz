from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.network.urlrequest import UrlRequest


class SampleApp(App):
    def build(self):
        layout = GridLayout(cols=2)
        self.btn1 = Button(background_normal="../../imgs/hall_off.png", background_down="../../imgs/hall_on.png")
        self.btn2 = Button(background_normal="../../imgs/kitchen_off.png", background_down="../../imgs/kitchen_on.png")
        self.btn3 = Button(background_normal="../../imgs/room_strange_off.jpeg", background_down="../../imgs/room_strange_on.jpeg")
        self.btn4 = Button(background_normal="../../imgs/bathroom_off.jpeg", background_down="../../imgs/bathroom_on.jpeg")
        
        layout.add_widget(self.btn1)
        layout.add_widget(self.btn2)
        layout.add_widget(self.btn3)
        layout.add_widget(self.btn4)

        return layout

    def modify_btn1():
        self.btn1.trigger_action(0)
        

if __name__ == "__main__":
    SampleApp().run()