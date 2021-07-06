from kivy.app import App
from kivy.uix.label import Label

print(dir(App))
print(dir(Label))
for x in dir(Label):
    if x=='canvas':
        help(x)
