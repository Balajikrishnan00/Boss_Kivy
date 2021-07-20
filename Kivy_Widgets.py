from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class widgetsExample(GridLayout):
    my_text=StringProperty('HEllO')
    count=1
    def on_button_click(self):

        print('Button Clicked')
        self.my_text=str(self.count)
        self.count+=1



class testMainApp(App):
    pass
testMainApp().run()
