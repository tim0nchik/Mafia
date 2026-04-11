from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class MafiaInputScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        app = App.get_running_app()
        text = Label(text = 'Выберите кол-во мафий:')
        button1 = Button(text = '1')
        button2 = Button(text = '2')
        button3 = Button(text = '3')
        hbl = BoxLayout(orientation = 'vertical')
        hbl.add_widget(text)
        hbl.add_widget(button1)
        hbl.add_widget(button2)
        hbl.add_widget(button3)
        self.add_widget(hbl)
        def but1():
            app.mafia_count = 1
            self.manager.current = 'scr4'
        button1.on_press = but1
        def but2():
            app.mafia_count = 2
            self.manager.current = 'scr4'
        button2.on_press = but2
        def but3():
            app.mafia_count = 3
            self.manager.current = 'scr4'
        button3.on_press = but3