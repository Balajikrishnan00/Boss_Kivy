from kivy.app import App
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class scroll(ScrollView):
    def __init__(self,**kwargs):
        super(scroll, self).__init__(**kwargs)
        layout=BoxLayout()

        for i in range(1,101):
            b=Button(text=str(i),size_hint=(.2,.1))
            layout.add_widget(b)





class MainApp(App):
    def build(self):
        return scroll()
MainApp().run()