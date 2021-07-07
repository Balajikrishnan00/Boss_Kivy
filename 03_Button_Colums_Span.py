from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class MyGrid(GridLayout):
    def __init__(self,**kwargs):
        super(MyGrid, self).__init__(**kwargs)
        self.cols=1
        self.topGrid=GridLayout()
        self.add_widget(self.topGrid)
        self.topGrid.cols=2

        self.topGrid.add_widget(Label(text='name'))
        self.name=TextInput(multiline=False)
        self.topGrid.add_widget(self.name)
        self.topGrid.add_widget(Label(text='Pizza'))
        self.pizza=TextInput(multiline=False)
        self.topGrid.add_widget(self.pizza)
        self.topGrid.add_widget(Label(text='Color'))
        self.color=TextInput(multiline=False)
        self.topGrid.add_widget(self.color)

        self.btn=Button(text='Submit')
        self.add_widget(self.btn)
        self.btn.bind(on_press=self.press)
    def press(self,i):
        name=self.name.text
        pizza=self.pizza.text
        color=self.color.text
        #print(name,pizza,color)
        self.add_widget(Label(text=f'%s %s %s'%(name,pizza,color)))

        self.name.text=''
        self.pizza.text=''
        self.color.text=''




class myApp(App):
    def build(self):
        Window.size=(320,480)
        return MyGrid()
myApp().run()
