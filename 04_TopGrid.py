from kivy.app import App
from kivy.base import Builder
KV="""
GridLayout:
    cols:1
    GridLayout:
        cols:2
        row_force_default:True
        row_default_height:50
        Label:
            text:'Name'
            bold:True
        TextInput:
            multiline:False
            id:'name'
        Label:
            text:'Pizza'
        TextInput:
        Label:
            text:'Color'
        TextInput:
    Button:
        text:'Submit'
        size_hint:(None,None)
        width:200
        height:50
        pos_hint:{'center_x':.5,'center_y':.5}
        
            
"""

class MainApp(App):
    def build(self):
        return Builder.load_string(KV)

MainApp().run()