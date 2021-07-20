from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.button import BaseButton

buttons="""
MDGridLayout:
    size:root.width,root.height
    MDRectangleFlatButton:
        text:'MDRectangleFlatButton'
        pos_hint:{'center_x':.5,'center_y':.9}
        size_hint:.2,.1
        on_release:app.callback()
    MDRaisedButton:
        text:'MDRaisedButton'
        pos_hint:{'center_x':.5,'center_y':.79}
        size_hint:.2,.1
    MDIconButton:
        icon:'message'
        pos_hint:{'center_x':.5,'center_y':.69}
    MDTextButton:
        text:'MDTextButton'
        pos_hint:{'center_x':.5,'center_y':.59}
    MDRoundFlatButton:
        text:'MDRoundFlatButton'
        pos_hint:{'center_x':.5,'center_y':.49}
    BaseButton:
        text:'BaseButton'
    
        
        
"""

class Turorials(MDApp):
    def build(self):
        button=Builder.load_string(buttons)
        return button
    def callback(self):
        print('Hello')


Turorials().run()