from kivymd.app import MDApp
from kivy.lang import Builder

ProgressBar="""
MDFloatLayout:
    MDProgressBar:
        id:process
        size_hint_x:.5
        pos_hint:{'center_x':.5,'center_y':.5}
        color:0,1,0,1
        #value:10
        
        
    MDIconButton:
        icon:'minus'
        pos_hint:{'center_x':.2,'center_y':.5}
        on_press:app.Minus()
    MDIconButton:
        icon:'plus'
        pos_hint:{'center_x':.8,'center_y':.5}
        on_release:app.Plus()
        
"""


class MainApp(MDApp):
    p=0
    def build(self):

        progressbar=Builder.load_string(ProgressBar)
        return progressbar
    def Minus(self):
        self.p=self.p + 1
        self.root.ids.process.vaule=self.p
    def Plus(self):
        pass
MainApp().run()
