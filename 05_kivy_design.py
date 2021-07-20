from os import name
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget



class MWidget(Widget):
    pass





class MykvApp(App):
    def build(self):
        return MWidget()
if __name__=='__main__':
    MykvApp().run()