from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty

ProgressBar="""
MDFloatLayout:
    MDProgressBar:
        id:process
        size_hint_x:.5
        pos_hint:{'center_x':.5,'center_y':.5}
        color:0,1,0,1
        value:1
        
        
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

    def build(self):

        progressbar=Builder.load_string(ProgressBar)
        return progressbar

    def Plus(self):
        self.p=self.root.ids.process.value
        self.p+=1
        self.root.ids.process.value=self.p




    def Minus(self):
        self.p = self.root.ids.process.value
        self.p-=1
        self.root.ids.process.value=self.p

MainApp().run()
