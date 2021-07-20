from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout

class Tutorial(MDApp):
    def build(self):
        b=MDBoxLayout(orientation='vertical')
        label1=  MDLabel(text="Primary",halign='center',font_style='H3',bold=True,theme_text_color='Primary')
        label2 = MDLabel(text="Secondary", halign='center', font_style='H3', bold=True, theme_text_color='Secondary')
        label3 = MDLabel(text="Hint", halign='center', font_style='H3', bold=True, theme_text_color='Hint')
        label4 = MDLabel(text="Error", halign='center', font_style='H3', bold=True, theme_text_color='Error')
        label5 = MDLabel(text="Custom", halign='center', font_style='H3', bold=True, theme_text_color='Custom')
        label6 = MDLabel(text="ContrastParentBackground", halign='center', font_style='H3', bold=True, theme_text_color='ContrastParentBackground')
        b.add_widget(label1)
        b.add_widget(label2)
        b.add_widget(label3)
        b.add_widget(label4)
        b.add_widget(label5)
        b.add_widget(label6)
        return b
Tutorial().run()