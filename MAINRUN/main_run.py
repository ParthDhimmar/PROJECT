import kivy 
import subprocess
from kivy.app import App
from kivy.uix.widget import Widget 
from kivy.uix.button import Button
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

class mode(BoxLayout):
    def __init__(self, **kwargs): 
        super(mode, self).__init__(**kwargs)

    def galaxy(self,value):
        return subprocess.call("python3 GALAXY\main.py",shell = True)
    def snakes(self,value):
        return subprocess.call(" python3 SNAKES\main.py",shell=True)
    def pingpong(self,value):
        return subprocess.call(" python3 PINGPONG\main.py",shell=True)
    pass
class run(App):
     def build(self):
            return mode()
if __name__ == '__main__':
    run().run()
