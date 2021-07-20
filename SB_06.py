from kivymd.app import MDApp
from kivy.lang import Builder

checkBox="""
MDFloatLayout:
    MDCheckbox:
        group:'group'
        size_hint:.1,.1
        pos_hint:{'center_x':.5,'center_y':.5}
        color:(1,0,0,1)
        on_active:app.check()
    MDCheckbox:
        group:'group'
        size_hint:.1,.1
        pos_hint:{'center_x':.5,'center_y':.4}
        on_active:app.check1()
        
        
    
"""
class TestApp(MDApp):
    def build(self):
        checkbox=Builder.load_string(checkBox)
        return checkbox
    def check(self,):
        print('Hello')

    def check1(self):
        print("world")
TestApp().run()

