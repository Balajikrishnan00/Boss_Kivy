from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty,BooleanProperty

class widgetsExample(GridLayout):

    my_text=StringProperty('1')
    count=1
    count_Enable=False
    Slider_value=StringProperty('0')
    text_input_str=StringProperty('foo')


    def plus(self):
        if self.count_Enable:

            print('Button Clicked')
            self.count += 1
            self.my_text=str(self.count)
        else:
            self.my_text='On the Button'
    def minus(self):
        if self.count_Enable:
            self.count=int(self.my_text)
            if self.count == 0:
                return 0
            else:
                self.count-=1
                self.my_text=str(self.count)
        else:
            self.my_text = 'On the Button'
    def on_State(self,Button_state):
        Button_state.text=''
        print('Toggle state:' +Button_state.state)
        if Button_state.state=='normal':
            Button_state.text = 'OFF'
            self.count_Enable=False
        else:
            Button_state.text='ON'
            self.count_Enable=True
    def on_Switch(self,widget):
        print(widget.active)
        if widget.active:
            self.Slider_value=str(100)
        else:
            self.Slider_value=str(0)



    def on_Slider(self,widget):
        print('Slider:',str(int(widget.value)))
        self.Slider_value=str(int(widget.value))

    def On_Text_Validate(self,widget):
        print(widget.text)
        self.text_input_str=widget.text




class testMainApp(App):
    pass
testMainApp().run()
