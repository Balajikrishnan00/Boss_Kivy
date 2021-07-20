from kivymd.app import MDApp
from kivy.lang import Builder
Card="""
MDFloatLayout:
    MDCard:
        pos_hint:{'center_x':.5,'center_y':.5}
        size_hint:.5,.5
        md_bg_color:.556,0,0,1
        MDLabel:
            text:'Welcome'
            halign:'center'
            valign:'top'
            theme_text_color:'Custom'
            text_color:1,1,1,1
            font_style:'H4'
            bold:True
            pos_hint:{'center_y':.95 }
    MDLabel:
        text:'Welcome'
        halign:'center'
        valign:'top'
        theme_text_color:'Custom'
        #text_color:,1,1,1
        font_style:'H4'
        bold:True
        pos_hint:{'center_y':.55 }
    MDIconButton:
        icon:'facebook'
        theme_text_color:'Custom'
        text_color:0,0,1,1
        #size:(300,300)         
        pos_hint:{'center_x':.25,'center_y':.9}
        user_font_size:'100sp'
        md_bg_color:1,1,1,1
    MDIconButton:
        icon:'whatsapp'
        theme_text_color:'Custom'
        text_color:0,1,0,1
        #size:(300,300)         
        pos_hint:{'center_x':.1,'center_y':.9}
        user_font_size:'100sp'
        #md_bg_color:1,1,1,1
    MDIconButton:
        icon:'instagram'
        theme_text_color:'Custom'
        text_color:1,0,0,1
        #size:(300,300)         
        pos_hint:{'center_x':.5,'center_y':.9}
        user_font_size:'100sp'
        md_bg_color:1,1,1,1
    MDIconButton:
        icon:'twitter'
        theme_text_color:'Custom'
        text_color:0,0,1,1
        #size:(300,300)         
        pos_hint:{'center_x':.7,'center_y':.9}
        user_font_size:'100sp'
        md_bg_color:1,1,1,1
"""
class card(MDApp):
    def build(self):
        card=Builder.load_string(Card)
        return card
card().run()