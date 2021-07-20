from kivymd.app import MDApp
from kivy.lang import Builder

Sliders="""
MDFloatLayout:
    MDSlider:
        id:s1
        max:5
        min:1
        pos_hint:{'center_x':.5,'center_y':.5}
        size_hint:.5,.1
        on_touch_down:app.hi()
        on_touch_up:app.bye()
    MDLabel:
        text:str(int(s1.value))
        pos_hint:{'center_y':.7}
        halign:'center'
        
        
"""

class TestApp(MDApp):
    def build(self):
        slider=Builder.load_string(Sliders)
        return slider
    def hi(self):
        print('welcome')
    def bye(self):
        print('goood')

TestApp().run()