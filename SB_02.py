from kivymd.app import MDApp
from kivy.lang import Builder

image="""
Image:
    source:'flower1.jpg'
    pos_hint:{'center_x':.5,'center_y':.5}
    size_hint:.5,.3
    
"""

class Tutorial(MDApp):
    def build(self):
        i=Builder.load_string(image)
        return i
Tutorial().run()