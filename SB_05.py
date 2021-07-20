from kivymd.app import MDApp
from kivy.lang import Builder

switches="""
MDSwitch:
    pos_hint:{'center_x':.5,'center_y':.5}
    width:dp(40)
    on_active:app.check(*args)
  
"""

class TestApp(MDApp):
    def build(self):
        switch=Builder.load_string(switches)
        return switch
    def check(self,instance,value):
        if value:
            self.theme_cls.theme_style='Yellow'
        else:
            self.theme_cls.theme_style='Orange'
TestApp().run()