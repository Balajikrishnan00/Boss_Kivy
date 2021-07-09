from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class mywidget(Widget):
    name=ObjectProperty()
    pizza=ObjectProperty()
    color=ObjectProperty()
    def press(self,i):
        print('Hai')


class MykvApp(App):
    def build(self):
        return mywidget()
if __name__ == '__main__':
    MykvApp().run()