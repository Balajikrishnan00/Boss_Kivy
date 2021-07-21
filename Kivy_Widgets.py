from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

class widgetsExample(GridLayout):

    my_text=StringProperty('1')
    count=1
    def plus(self):

        print('Button Clicked')
        self.count += 1
        self.my_text=str(self.count)
    def minus(self):
        self.count=int(self.my_text)
        if self.count == 0:
            return 0
        else:
            self.count-=1
            self.my_text=str(self.count)






class testMainApp(App):
    pass
testMainApp().run()
