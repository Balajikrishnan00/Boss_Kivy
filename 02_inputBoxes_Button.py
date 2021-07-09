from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window

Window.core=(220,480)

class myGrid(GridLayout):
    def __init__(self,**kwargs):
        super(myGrid, self).__init__(**kwargs)
        self.cols=1
        self.size_hint=(.4,.2)

        self.pos_hint={'center_x':.5,'center_y':.5}
        self.username=TextInput(hint_text='Username',multiline=False)
        self.password=TextInput(hint_text='Password',password=True,multiline=False)
        self.btn=Button(text='Login',pos_hint={'center_x':.5,'center_y':.5},color=(1, 1, 1,1),background_color=(1030, 0, 0))


        self.add_widget(self.username)
        self.add_widget(self.password)
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.press)

    def press(self,i):
        username=self.username.text
        password=self.password.text
        #print(f'Hi {username} your Password Is {password}')
        self.add_widget(Label(text=f'Hi {username} your Password Is {password}',bold=True))
        self.username.text=''
        self.password.text=''


class MYApp(App):
    def build(self):

        return myGrid()

MYApp().run()
