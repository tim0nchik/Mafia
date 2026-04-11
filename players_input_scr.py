from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.app import App

class PlayersInputScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        app = App.get_running_app()
        text = Label(text = "Выберите кол-во игроков:")
        button1 = Button(text = '6')
        button2 = Button(text = '7')
        button3 = Button(text = '8')
        hbl = BoxLayout(orientation = 'vertical')
        hbl.add_widget(text)
        hbl.add_widget(button1)
        hbl.add_widget(button2)
        hbl.add_widget(button3)
        self.add_widget(hbl)
        def but1():
            app.players_count = 6
            self.manager.current = 'scr2'
        button1.on_press = but1
        def but2():
            app.players_count = 7
            self.manager.current = 'scr2'
        button2.on_press = but2
        def but3():
            app.players_count = 8
            self.manager.current = 'scr2'
        button3.on_press = but3

