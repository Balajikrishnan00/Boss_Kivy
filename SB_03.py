from kivymd.app import MDApp
from kivy.lang import Builder

text_field="""

MDTextFieldRect:
    hint_text:'Username'
    size_hint_x:.5
    size_hint_y:.1
    pos_hint:{'center_x':.5,'center_y':.5}
    mode:'rectangle'
    helper_text:'balaji'
    helper_text_mode:'on_focus'
    multiline:True
    max_text_length:10
"""

class Tutorials(MDApp):
    def build(self):
        self.theme_cls.primary_palette='Red'
        t=Builder.load_string(text_field)
        return t
Tutorials().run()

#['Red', 'Pink', 'Purple', 'DeepPurple', 'Indigo', 'Blue',
# 'LightBlue', 'Cyan', 'Teal', 'Green', 'LightGreen', 'Lime',
# 'Yellow', 'Amber', 'Orange', 'DeepOrange', 'Brown', 'Gray', 'BlueGray']

# mode=['rectangle', 'fill']

# MDTextField,MDTextFieldRound,MDTextFieldRect