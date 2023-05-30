import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.recycleview import RecycleView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.progressbar import ProgressBar
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.config import ConfigParser
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.metrics import dp
from datetime import datetime
from kivy.lang import Builder
import os
import ast
import time
import smtplib

#Builder.load_file('test_kv.kv')

class Start(Screen):
    def __init__(self, **kw):
        super(Start, self).__init__(**kw)
        box = BoxLayout(orientation='vertical')
        box.add_widget(Button(text='',
        background_normal = 'back.jpg',
        on_press=lambda x:
        set_screen('menu')))
        self.add_widget(box)

class MenuScreen(Screen):
    def __init__(self, **kw):
        super(MenuScreen, self).__init__(**kw)
    
    def on_enter(self):
        Window.clearcolor = (255, 255, 255, 255)
        boxsl = BoxLayout(orientation='vertical')
        lb1 = Label(text='Выберете курс',
        color = (0, 0, 0, 1),
        font_size = 30,
        markup = True,
        halign="center",
        size_hint = (1, 0.50))
        SL = FloatLayout()
        btn1 = Button(text ="1",
                    background_normal = '11.png',
                    border = (15, 15, 15, 15),
        			font_size = 20,
					size_hint =(0.40, 0.30), 
                    on_press=lambda x:
                    set_screen('list_food'),
                    pos = (10, 250))
        btn2 = Button(text ="2",
                    background_normal = '11.png',
        			font_size = 20,
					size_hint =(0.40, 0.30),
                    on_press=lambda x:
                    set_screen('list_food'),
                    pos = (220, 250))
        btn3 = Button(text ="3",
                    background_normal = '11.png',
        			font_size = 20,
					size_hint =(0.40, 0.30),
                    on_press=lambda x:
                    set_screen('list_food'),
                    pos = (10, 130))
        btn4 = Button(text ="4",
                    background_normal = '11.png',
        			font_size = 20,
					size_hint =(0.40, 0.30),
                    on_press=lambda x:
                    set_screen('list_food'),
                    pos = (220, 130))

        SL.add_widget(btn1)
        SL.add_widget(btn2)
        SL.add_widget(btn3)
        SL.add_widget(btn4)

        boxsl.add_widget(lb1)
        boxsl.add_widget(SL)


        box = BoxLayout(orientation='vertical')
        lb2 = Label(text='Оцените вкус еды в столовой',
        markup = True,
        font_size = 40,
        color = (0, 0, 0, 1),
        halign = 'center',
        size_hint = (1, 0.30))
        box.add_widget(lb2)
        box1 = BoxLayout(orientation='horizontal')
        box2 = BoxLayout(orientation='vertical')

        self.lbzz = Label(text = '',
        markup = True,
        halign = 'center',
        color = (0, 0, 0, 1),
        size_hint = (1, 0.02))

        self.lbz = Label(text = 'Рейтинг',
        markup = True,
        halign = 'center',
        color = (0, 0, 0, 1),
        size_hint = (1, 0.03), 
        font_size = 30)

        self.lbp1 = Label(text = "Отлично",
        markup = True,
        color = (0, 0, 0, 1),
        halign = 'center',
        size_hint = (1, 0.01))
        self.p1 = ProgressBar(max = 10,
        size_hint = (1, 0.01))
        self.p1.value = 0
        self.lbp2 = Label(text = "Хорошо",
        markup = True,
        color = (0, 0, 0, 1),
        halign = 'center',
        size_hint = (1, 0.01))
        self.p2 = ProgressBar(max = 10,
        size_hint = (1, 0.01))
        self.lbp3 = Label(text = "Нормально",
        markup = True,
        color = (0, 0, 0, 1),
        halign = 'center',
        size_hint = (1, 0.01))
        self.p3 = ProgressBar(max = 10,
        size_hint = (1, 0.01))
        self.lbp4 = Label(text = "Плохо", 
        markup = True,
        color = (0, 0, 0, 1),
        halign = 'center',
        size_hint = (1, 0.01))
        self.p4 = ProgressBar(max = 10,
        size_hint = (1, 0.01))
        self.lbp5 = Label(text = "Отвратително", 
        markup = True,
        color = (0, 0, 0, 1),
        halign = 'center',
        size_hint = (1, 0.01))
        self.p5 = ProgressBar(max = 10,
        size_hint = (1, 0.01))


        lb3 = Label(text='Создатель: Негматов Азам и Юсупов Мухаммедалсаид \n Группа: П22-1зк и Т22-1Б',
        markup = True,
        color = (0, 0, 0, 1),
        halign = 'center',
        size_hint = (1, 0.05),
        font_size = 12)

        box2.add_widget(self.lbzz)
        box2.add_widget(self.lbz)
        box2.add_widget(self.lbp1)
        box2.add_widget(self.p1)
        box2.add_widget(self.lbp2)
        box2.add_widget(self.p2)
        box2.add_widget(self.lbp3)
        box2.add_widget(self.p3)
        box2.add_widget(self.lbp4)
        box2.add_widget(self.p4)
        box2.add_widget(self.lbp5)
        box2.add_widget(self.p5)
        box2.add_widget(lb3)
        
        box1.add_widget(boxsl)
        box1.add_widget(box2)
        box.add_widget(box1)

        self.add_widget(box)


        d1 = ast.literal_eval(App.get_running_app().config.get('General', 'p1'))
        d2 = ast.literal_eval(App.get_running_app().config.get('General', 'p2'))
        d3 = ast.literal_eval(App.get_running_app().config.get('General', 'p3'))
        d4 = ast.literal_eval(App.get_running_app().config.get('General', 'p4'))
        d5 = ast.literal_eval(App.get_running_app().config.get('General', 'p5'))

        for f1, d in sorted(d1.items(), key=lambda x: x[1]):
            self.p1.value = f1
            ld = "Отлично " + str(f1)
            self.lbp1.text = ld
            if self.p1.value == 10:
                self.p1.max = 100
                self.p2.max = 100
                self.p3.max = 100
                self.p4.max = 100
                self.p5.max = 100
            elif self.p1.value == 100:
                self.p1.max = 500
                self.p2.max = 500
                self.p3.max = 500
                self.p4.max = 500
                self.p5.max = 500
            elif self.p1.value == 500:
                self.p1.max = 1000
                self.p2.max = 1000
                self.p3.max = 1000
                self.p4.max = 1000
                self.p5.max = 1000
            elif self.p1.value == 1000:
                self.p1.max = 5000
                self.p2.max = 5000
                self.p3.max = 5000
                self.p4.max = 5000
                self.p5.max = 5000
        for f2, d in sorted(d2.items(), key=lambda x: x[1]):
            self.p2.value = f2
            ld2 = "Хорошо " + str(f2)
            self.lbp2.text = ld2
            if self.p2.value == 10:
                self.p1.max = 100
                self.p2.max = 100
                self.p3.max = 100
                self.p4.max = 100
                self.p5.max = 100
            elif self.p2.value == 100:
                self.p1.max = 500
                self.p2.max = 500
                self.p3.max = 500
                self.p4.max = 500
                self.p5.max = 500
            elif self.p2.value == 500:
                self.p1.max = 1000
                self.p2.max = 1000
                self.p3.max = 1000
                self.p4.max = 1000
                self.p5.max = 1000
            elif self.p2.value == 1000:
                self.p1.max = 5000
                self.p2.max = 5000
                self.p3.max = 5000
                self.p4.max = 5000
                self.p5.max = 5000
        for f3, d in sorted(d3.items(), key=lambda x: x[1]):
            self.p3.value = f3
            ld3 = "Нормально " + str(f3)
            self.lbp3.text = ld3
            if self.p3.value == 10:
                self.p1.max = 100
                self.p2.max = 100
                self.p3.max = 100
                self.p4.max = 100
                self.p5.max = 100
            elif self.p3.value == 100:
                self.p1.max = 500
                self.p2.max = 500
                self.p3.max = 500
                self.p4.max = 500
                self.p5.max = 500
            elif self.p3.value == 500:
                self.p1.max = 1000
                self.p2.max = 1000
                self.p3.max = 1000
                self.p4.max = 1000
                self.p5.max = 1000
            elif self.p3.value == 1000:
                self.p1.max = 5000
                self.p2.max = 5000
                self.p3.max = 5000
                self.p4.max = 5000
                self.p5.max = 5000
        for f4, d in sorted(d4.items(), key=lambda x: x[1]):
            self.p4.value = f4
            ld4 = "Плохо " + str(f4)
            self.lbp4.text = ld4
            if self.p4.value == 10:
                self.p1.max = 100
                self.p2.max = 100
                self.p3.max = 100
                self.p4.max = 100
                self.p5.max = 100
            elif self.p4.value == 100:
                self.p1.max = 500
                self.p2.max = 500
                self.p3.max = 500
                self.p4.max = 500
                self.p5.max = 500
            elif self.p4.value == 500:
                self.p1.max = 1000
                self.p2.max = 1000
                self.p3.max = 1000
                self.p4.max = 1000
                self.p5.max = 1000
            elif self.p1.value == 1000:
                self.p1.max = 5000
                self.p2.max = 5000
                self.p3.max = 5000
                self.p4.max = 5000
                self.p5.max = 5000
        for f5, d in sorted(d5.items(), key=lambda x: x[1]):
            self.p5.value = f5
            ld5 = "Отвратително " + str(f5)
            self.lbp5.text = ld5
            if self.p5.value == 10:
                self.p1.max = 100
                self.p2.max = 100
                self.p3.max = 100
                self.p4.max = 100
                self.p5.max = 100
            elif self.p5.value == 100:
                self.p1.max = 500
                self.p2.max = 500
                self.p3.max = 500
                self.p4.max = 500
                self.p5.max = 500
            elif self.p5.value == 500:
                self.p1.max = 1000
                self.p2.max = 1000
                self.p3.max = 1000
                self.p4.max = 1000
                self.p5.max = 1000
            elif self.p5.value == 1000:
                self.p1.max = 5000
                self.p2.max = 5000
                self.p3.max = 5000
                self.p4.max = 5000
                self.p5.max = 5000

        qwa = self.p1.value + self.p2.value + self.p3.value + self.p4.value + self.p5.value
        user = "shaggymufson21@gmail.com"
        passwd = "bfjhcjwhfxivjyrh"
        server = "smtp.gmail.com"
        port = 587
        charset = 'Content-Type: text/plain; charset=utf-8'
        mime = 'MIME-Version: 1.0'
        to = "shaggymufson21@gmail.com"
        subject = "Общее количество голосов: " + str(qwa)
        text = "Голосов Отвратительно: " + str(self.p5.value) + "\nГолосов Плохо: " + str(self.p4.value) + "\nГолосов Нормально: " + str(self.p3.value) + "\nГолосов Хорошо: " + str(self.p2.value) + "\nГолосов Отлчино: " + str(self.p1.value)

        body = "\r\n".join((f"From: {user}", f"To: {to}", f"Subject: {subject}", mime, charset, "", text))

        smtp = smtplib.SMTP(server, port)
        smtp.starttls()
        smtp.login(user, passwd)
        smtp.sendmail(user, to, body.encode('utf-8'))
        smtp.quit()

    def on_leave(self): 
        self.clear_widgets() 


class SortedListFood(Screen):
    def __init__(self, **kw):
        super(SortedListFood, self).__init__(**kw)

    def on_enter(self):
        self.layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
        box = BoxLayout(orientation = 'vertical')
        self.layout.bind(minimum_height=self.layout.setter('height'))
        back_button = Button(text='< Назад в главное меню',
                             background_color = (0, 0, 0, 1),
                             on_press=lambda x: set_screen('menu'),
                             size_hint_y=None, height=dp(40))
        self.layout.add_widget(back_button)

        self.btn1 = Button(text = "Отлично",
        font_size = 30,
        on_release = self.func_btn1)
        self.btn2 = Button(text = "Хорошо", 
        font_size = 30,
        on_release = self.func_btn2)
        self.btn3 = Button(text = "Нормально", 
        font_size = 30,
        on_release = self.func_btn3)
        self.btn4 = Button(text = "Плохо", 
        font_size = 30,
        on_release = self.func_btn4)
        self.btn5 = Button(text = "Отвратително", 
        font_size = 30,
        on_release = self.func_btn5)
        box.add_widget(self.layout)
        box.add_widget(self.btn1)
        box.add_widget(self.btn2)
        box.add_widget(self.btn3)
        box.add_widget(self.btn4)
        box.add_widget(self.btn5)
        root = RecycleView(size_hint=(1, None), size=(Window.width,
                                                      Window.height))
        root.add_widget(box)
        self.add_widget(root)

        self.p1 = 1
        self.p2 = 1
        self.p3 = 1
        self.p4 = 1
        self.p5 = 1

    def on_leave(self): 
        self.layout.clear_widgets() 

    def func_btn1(self, btn1):
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'p1'))
        d1 = ast.literal_eval(App.get_running_app().config.get('General', 'p1'))
        for f, d in sorted(d1.items(), key=lambda x: x[1]):
            if f == '':
                f = 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p1', self.app.user_data)
                self.app.config.write()
            else:
                f += 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p1', self.app.user_data)
                self.app.config.write()
        if self.p1 == 1:
            self.app.user_data[self.p1] = int(time.time())

            self.app.config.set('General', 'p1', self.app.user_data)
            self.app.config.write()

        set_screen('start')

    def func_btn2(self, btn1):
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'p2'))
        d2 = ast.literal_eval(App.get_running_app().config.get('General', 'p2'))
        for f, d in sorted(d2.items(), key=lambda x: x[1]):
            if f == '':
                f = 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p2', self.app.user_data)
                self.app.config.write()
            else:
                f += 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p2', self.app.user_data)
                self.app.config.write()
        if self.p2 == 1:
            self.app.user_data[self.p2] = int(time.time())

            self.app.config.set('General', 'p2', self.app.user_data)
            self.app.config.write()

        set_screen('start')

    def func_btn3(self, btn1):
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'p3'))
        d3 = ast.literal_eval(App.get_running_app().config.get('General', 'p3'))
        for f, d in sorted(d3.items(), key=lambda x: x[1]):
            if f == '':
                f = 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p3', self.app.user_data)
                self.app.config.write()
            else:
                f += 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p3', self.app.user_data)
                self.app.config.write()
        if self.p3 == 1:
            self.app.user_data[self.p3] = int(time.time())

            self.app.config.set('General', 'p3', self.app.user_data)
            self.app.config.write()

        set_screen('start')
    
    def func_btn4(self, btn1):
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'p4'))
        d4 = ast.literal_eval(App.get_running_app().config.get('General', 'p4'))
        for f, d in sorted(d4.items(), key=lambda x: x[1]):
            if f == '':
                f = 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p4', self.app.user_data)
                self.app.config.write()
            else:
                f += 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p4', self.app.user_data)
                self.app.config.write()
        if self.p4 == 1:
            self.app.user_data[self.p4] = int(time.time())

            self.app.config.set('General', 'p4', self.app.user_data)
            self.app.config.write()

        set_screen('start')
    
    def func_btn5(self, btn1):
        self.app = App.get_running_app()
        self.app.user_data = ast.literal_eval(
            self.app.config.get('General', 'p5'))
        d5 = ast.literal_eval(App.get_running_app().config.get('General', 'p5'))
        for f, d in sorted(d5.items(), key=lambda x: x[1]):
            if f == '':
                f = 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p5', self.app.user_data)
                self.app.config.write()
            else:
                f += 1
                self.app.user_data[f] = int(time.time())

                self.app.config.set('General', 'p5', self.app.user_data)
                self.app.config.write()
        if self.p5 == 1:
            self.app.user_data[self.p5] = int(time.time())

            self.app.config.set('General', 'p5', self.app.user_data)
            self.app.config.write()

        set_screen('start')
    
def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManager()
sm.add_widget(Start(name='start'))
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SortedListFood(name='list_food'))


class FoodOptionsApp(App):
    def __init__(self, **kvargs):
        super(FoodOptionsApp, self).__init__(**kvargs)
        self.config = ConfigParser()

    def build_config(self, config):
        config.adddefaultsection('General')
        config.setdefault('General', 'p1', '{}')
        config.setdefault('General', 'p2', '{}')
        config.setdefault('General', 'p3', '{}')
        config.setdefault('General', 'p4', '{}')
        config.setdefault('General', 'p5', '{}')

    def set_value_from_config(self):
        self.config.read(os.path.join(self.directory, '%(appname)s.ini'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'p1'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'p2'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'p3'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'p4'))
        self.user_data = ast.literal_eval(self.config.get(
            'General', 'p5'))

    def get_application_config(self):
        return super(FoodOptionsApp, self).get_application_config(
            '{}/%(appname)s.ini'.format(self.directory))


    def build(self):
        return sm


if __name__ == '__main__':
    FoodOptionsApp().run()

