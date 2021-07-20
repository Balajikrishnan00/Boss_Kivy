from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label


class MYAPP(App):

    def build(self):
        return Button(text='Button1',font_size=32,size_hint=(None,None),height=50,width=200,pos_hint={'center_x':.5,'center_y':.5},on_press=self.press)
    def press(self,i):
        print('Button Clicked!')
MYAPP().run()