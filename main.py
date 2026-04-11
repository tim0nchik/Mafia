from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from players_input_scr import PlayersInputScr
from peaceful_input_scr import PeacefulInputScr
from mafia_input_scr import MafiaInputScr
from doctor_input_scr import DoctorInputScr
from prostitute_input_scr import ProstituteInputScr
from comisar_input_scr import ComisarInputScr

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
        scrm.add_widget(MafiaInputScr(name = 'scr3'))
        scrm.add_widget(DoctorInputScr(name = 'scr4'))
        scrm.add_widget(ProstituteInputScr(name = 'scr5'))
        scrm.add_widget(ComisarInputScr(name = 'scr6'))
        return scrm
app = MyApp()
app.run()