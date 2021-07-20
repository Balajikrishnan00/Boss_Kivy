from kivymd.app import MDApp
from kivymd.uix.label import MDLabel

class Tutorial(MDApp):
    def build(self):
        label=MDLabel(text="Hello World",halign='center',font_style='H3',bold=True)
        return label
Tutorial().run()