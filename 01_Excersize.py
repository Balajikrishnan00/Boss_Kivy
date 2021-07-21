from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.floatlayout import FloatLayout
kv_Design="""

<mywidget>

    ToggleButton:
        text:'OFF'
        size_hint:(.2,.1)
        pos_hint:{'center_x':.5,'center_y':.9}
        on_state:root.Toggle_Button(self)
    Button:
        text:'-'
        size_hint:(.2,.1)
        pos_hint:{'center_x':.3,'center_y':.5}
        on_press:root.minus()
    Label:
        id:l1
        font_name:'fonts/Lcd.ttf'
        text:root.my_text
        font_size:'80dp'
        size_hint:(.2,.1)
        pos_hint:{'center_x':.5,'center_y':.5}
    Button:
        text:'+'
        size_hint:(.2,.1)
        pos_hint:{'center_x':.7,'center_y':.5} 
        on_press:root.plus()
"""
class mywidget(FloatLayout):
    my_text=StringProperty('0')
    count=1
    Toggle_is_Enable=False
    def minus(self):
        if self.Toggle_is_Enable:
            if self.my_text=='0':
                return 0

            else:
                self.count=int(self.my_text)-1
                self.my_text=str(self.count)


    def plus(self):
        if self.Toggle_is_Enable:

            self.my_text=str(self.count)
            self.count += 1
    def Toggle_Button(self,i):
        print(i.state)
        if i.state =='normal':
            i.text='OFF'
            self.Toggle_is_Enable=False
        else:
            i.text='ON'
            self.Toggle_is_Enable=True
class Main(App):
    def build(self):
        Builder.load_string(kv_Design)
        return mywidget()


Main().run()
