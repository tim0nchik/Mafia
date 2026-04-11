from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class ProstituteInputScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        app = App.get_running_app()
        text = Label(text = 'Выберите кол-во путан')
        button1 = Button(text = '1')
        button2 = Button(text = '0')
        hbl = BoxLayout(orientation = 'vertical')
        hbl.add_widget(text)
        hbl.add_widget(button1)
        hbl.add_widget(button2)
        self.add_widget(hbl)
        def but1():
            app.prostitute_count = 1
            self.manager.current = 'scr6'
        button1.on_press = but1
        def but2():
            app.prostitute_count = 0
            self.managet.current = 'scr6'
        button2.on_press = but2
