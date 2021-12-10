from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.lang.builder import Builder
from kivy.properties import StringProperty, BooleanProperty, NumericProperty, ObjectProperty
import threading
import time
import datetime
from kivy.core.window import Window
from playsound import playsound
Window.size = (960, 720)

class TimerApp(MDApp):

    pause_time = StringProperty('')
    running_time = StringProperty('')
    current_running_time = NumericProperty(0)
    current_pause_time = NumericProperty(0)
    how_long_to_work = NumericProperty(0)
    how_long_to_pause = NumericProperty(0)

    def __init__(self, **kwargs):
        self.current_running_time = 0
        self.current_pause_time = 0

        self.in_work = True
        self.in_pause = False
        super().__init__(**kwargs)
    def build(self):

        self.how_long_to_work = self.root.ids.work_spinner.value
        self.how_long_to_pause = self.root.ids.pause_spinner.value
        self.pause_time = str(datetime.timedelta(seconds=self.how_long_to_pause*60))
        self.running_time = str(datetime.timedelta(seconds=self.how_long_to_work*60))
        self.running = False
        app = Builder.load_file('timer.kv')

        return app

    def start(self):
        def run_thread():
            while self.running:
                if self.current_running_time > 0:
                    self.current_running_time-=1

                    if self.current_running_time == 0:
                        playsound('finish_work.wav')
                    
                
                    
                elif self.current_pause_time > 0:
                    self.current_pause_time-=1 
                    if self.current_pause_time == 0:
                        playsound('finish_pause.wav')
                      
                   
                else:
                    self.current_running_time = self.how_long_to_work
                    self.current_pause_time = self.how_long_to_pause
                
                self.running_time =  str(datetime.timedelta(seconds=self.current_running_time))
                self.pause_time =  str(datetime.timedelta(seconds=self.current_pause_time))
                time.sleep(1)
        self.running = True
        thread = threading.Thread(target=run_thread)
        thread.start()

    
    def stop(self):
        self.running=False
    
    def reset(self):
        self.running=False
        self.current_running_time = self.how_long_to_work*60
        self.current_pause_time = self.how_long_to_pause*60
        self.running_time =  str(datetime.timedelta(seconds=self.current_running_time))
        self.pause_time =  str(datetime.timedelta(seconds=self.current_pause_time))

    def set_running_time(self, value):
        self.running_time = str(datetime.timedelta(seconds=value*60))
        self.how_long_to_work = int(value*60)
        self.current_running_time = self.how_long_to_work

    def set_pause_time(self, value):
        self.pause_time = str(datetime.timedelta(seconds=value*60))
        self.how_long_to_pause = int(value*60)
        self.current_pause_time = self.how_long_to_pause





TimerApp().run()
