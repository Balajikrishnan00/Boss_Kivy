from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.metrics import dp
from kivy.uix.scrollview import ScrollView
class stacklayout(StackLayout):
    def __init__(self,**kwargs):
        super(stacklayout, self).__init__(**kwargs)

        for i in range(1,101):
            #size = (dp(100), dp(100))
            #size=dp(100)+i*10
            b=Button(text=str(i),size_hint=(None,None),size = (dp(100), dp(100)))
            self.add_widget(b,)


class pepul(BoxLayout):
    pass

class mybox(BoxLayout):
    pass

class boxmainApp(App):
    pass

boxmainApp().run()