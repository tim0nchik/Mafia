from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from players_input_scr import PlayersInputScr
from peaceful_input_scr import PeacefulInputScr

class MyApp(App):
    players_count = 0
    mafia_count = 0
    peaceful_count = 0
    prostitute_count = 0
    comisar_count = 0
    doctor_count = 0
    def build(self):
        scrm = ScreenManager()
        scrm.add_widget(PlayersInputScr(name = 'scr1'))
        scrm.add_widget(PeacefulInputScr(name = 'scr2'))
        return scrm
app = MyApp()
app.run()