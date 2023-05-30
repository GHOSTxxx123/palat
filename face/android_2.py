from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from datetime import datetime
import os
import ast
import time


Window.clearcolor = (80/255, 170/255, 170/255)

class Kyrs(Screen):
    def __init__(self, **kw):
        super(Kyrs, self).__init__(**kw)

        self.floatL = FloatLayout()

        self.label_1 = Label(text = 'Оцени вкус еды !!!', font_size = (55), size_hint = (.70, .15), pos = (135, 500),) #color = (80/255, 170/255, 0/255)))
        self.label_2 = Label(text = 'Выберите курс', font_size = (40), pos = (105, 400), size_hint = (.2, .15),) #color = (80/255, 170/255, 0/255)))
        self.btn_1 = Button(text = '1', size_hint = (.2, .15), pos =(10, 270), font_size = (25), background_normal = 'normal.png', background_down = 'down1.png', on_press=lambda x:set_screen('list'))
        self.btn_2 = Button(text = '2', size_hint = (.2, .15), pos =(190, 270), font_size = (25), background_normal = 'normal.png', background_down = 'down1.png', on_press=lambda x:set_screen('list'))
        self.btn_3 = Button(text = '3', size_hint = (.2, .15), pos =(10, 120), font_size = (25), background_normal = 'normal.png', background_down = 'down1.png', on_press=lambda x:set_screen('list'))
        self.btn_4 = Button(text = '4', size_hint = (.2, .15), pos =(190, 120), font_size = (25), background_normal = 'normal.png', background_down = 'down1.png', on_press=lambda x:set_screen('list'))
        self.label_3 = Label(text = 'Рейтинг', font_size = (40), pos = (500, 400), size_hint = (.2, .15),)# color = (80/255, 170/255, 0/255)))
        self.btn_5 = Button(text = '', size_hint = (.55, .45), pos =(360, 160), font_size = (25), background_normal = 'в.png', background_down = 'в.png',)
        self.btn_6 = Button(text = '', size_hint = (.10, .10), pos =(540, 150), font_size = (25), background_normal = 'up_arrow.png', background_down = 'down1.png',)

        self.floatL.add_widget(self.label_1)
        self.floatL.add_widget(self.label_2)
        self.floatL.add_widget(self.label_3)
        self.floatL.add_widget(self.btn_1)
        self.floatL.add_widget(self.btn_2)
        self.floatL.add_widget(self.btn_3)
        self.floatL.add_widget(self.btn_4)
        self.floatL.add_widget(self.btn_5)
        self.floatL.add_widget(self.btn_6)

        self.add_widget(self.floatL)

class Vibor(Screen):
    def __init__(self, **kw):
        super(Vibor, self).__init__(**kw)

        self.floatl = FloatLayout()

        self.label_1_1 = Label(text = 'Как вам обед ?', font_size = (55), size_hint = (.70, .15), pos = (135, 500),)
        self.btn_1_1 = Button(text = '', size_hint = (.2, .25), pos =(50, 270), font_size = (25), background_normal = 'bad.png', background_down = 'down1.png', on_press=lambda x:set_screen('list'))
        self.btn_1_2 = Button(text = '', size_hint = (.2, .25), pos =(190, 270), font_size = (25), background_normal = 'dont_like.png', background_down = 'down1.png', on_press=lambda x:set_screen('list'))
        


        self.floatl.add_widget(self.label_1_1)
        self.floatl.add_widget(self.btn_1_1)
        self.floatl.add_widget(self.btn_1_2)

        self.add_widget(self.floatl)


def set_screen(name_screen):
    sm.current = name_screen





sm = ScreenManager()
sm.add_widget(Kyrs(name = 'menu'))
sm.add_widget(Vibor(name = 'list'))

class Golos(App):

    def btn_click(self):
        pass

    def build(self):
        return sm



if __name__ == "__main__":
    Golos().run()