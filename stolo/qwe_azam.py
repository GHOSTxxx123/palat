import random
from kivy.animation import Animation
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout 
from kivy.uix.button import Button  
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.gridlayout import GridLayout


class Main(Screen):
    def __init__(self, **kw):
        super(Main, self).__init__(**kw)
        Window.celarcolor = (255, 255, 255, 255)
        self.all = 0
        self.haveToUse = True
        self.bad = 0
        self.good = 0
        self.wq = .495
        self.wqa = .495 - .05
        self.smileState = 3
        self.fl = FloatLayout()
        bl = BoxLayout(orientation="horizontal", size_hint=(.4, .4))
        bar = Image(source="gradient.png", pos_hint={'x':.8,'y':.1}, size_hint=(.1, .8))
        self.point = Image(color="red", size_hint=(.07, .005), pos_hint={'x':.9,'y':.495})
        text = Label(text="Выберите ваш курс обучения", font_size=35, pos_hint={'x':-.1,'y':.05})

        self.img1 = Image(source="img1.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=0)
        self.img2 = Image(source="img2.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=0)
        self.img3 = Image(source="img3.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=0)
        self.img4 = Image(source="img4.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=0)
        self.img5 = Image(source="img5.png", size_hint=(.1, .1), pos_hint={'x':.73,'y':self.wqa}, opacity=0)

        gl = GridLayout(cols=2, size_hint=(.4, .4), spacing=10, pos_hint={'x':.05,'y':.05})

        gl.add_widget(Button(text="1", font_size=30, on_press=lambda x:self.change(kurs=1)))
        gl.add_widget(Button(text="2", font_size=30, on_press=lambda x:self.change(kurs=2)))
        gl.add_widget(Button(text="3", font_size=30, on_press=lambda x:self.change(kurs=3)))
        gl.add_widget(Button(text="4", font_size=30, on_press=lambda x:self.change(kurs=4)))

        self.fl.add_widget(text)
        self.fl.add_widget(bar)
        self.fl.add_widget(self.point)
        self.fl.add_widget(gl)

        self.fl.add_widget(self.img1)
        self.fl.add_widget(self.img2)
        self.fl.add_widget(self.img3)
        self.fl.add_widget(self.img4)
        self.fl.add_widget(self.img5)
        
        self.fl.add_widget(bl)
        self.add_widget(self.fl)

        self.fl2 = FloatLayout()        


    def change(self, kurs):
        if self.haveToUse == True:
            set_screen('golos')
            self.haveToUse = False
        


    def tomain(self):
        self.fl.opacity = 0
        set_screen('main')
        anom = Animation(
            opacity=1,
            duration=2
        )

        anom += Animation(
            opacity=0,
            duration=1.5
        )
        

        anim = Animation(
            opacity=1,
            duration=1
        )

        achko = Animation(
            pos_hint={'x':.9,'y':self.wq},
            duration=random.uniform(0.5, 1.5),
        )
        


        def tvushka(instance):
            self.haveToUse = True
            self.smile_Check()



        def por(instance):
            if self.wq == 0:
                pass
                self.haveToUse = True
            else:
                achko.start(self.point)
                achko.on_complete=tvushka

        def lor(instance):
            anim.start(self.fl)
            anim.on_complete=por

    

    def smile_Check(self):
        if self.wq < .190:
            self.img1.opacity = 1
            self.img1.pos_hint={'x':.73,'y':self.wqa}

    def enjoy(self, num):
        self.all += 1
        if num > 0:
            self.good += num
        else:
            cum = str(num)
            sum = cum.replace("-", "")
            zum = int(sum)
            self.bad += num

        #Максимум вверх 5
        if self.bad * 5 < self.good and self.bad * 4.7 > self.good:
            self.wq = .895
        elif self.bad == 0 and self.good != 0:
            self.wq = .895
        
        #Больше вверх 4
        if self.bad * 2.5 < self.good and self.bad * 2.7 > self.good:
            self.wq = .695

        #Центр 3
        if self.good == self.bad:
            self.wq = .495

        # Больше в низ 2
        if self.good * 2.5 < self.bad and self.good * 2.7 > self.bad:
            self.wq = .295

        #Максимум вниз 1
        if self.good * 5 < self.bad:
            self.wq = .095
        elif self.good == 0 and self.bad != 0:
            self.wq = .095


        # 4 блока 4 блока 4 блока 4 блока 4 блока 4 блока 4 блока
        if self.bad > self.good:
            # Блок 1
            if self.good * 4.7 < self.bad and self.good * 5 > self.bad:
                self.wq = .115
            elif self.good * 4.4 < self.bad and self.good * 4.7 > self.bad:
                self.wq = .130
            elif self.good * 4.1 < self.bad and self.good * 4.4 > self.bad:
                self.wq = .155
            elif self.good * 3.8 < self.bad and self.good * 4.1 > self.bad:
                self.wq = .180
            elif self.good * 3.5 < self.bad and self.good * 3.8 > self.bad:
                self.wq = .205
            elif self.good * 3.2 < self.bad and self.good * 3.5 > self.bad:
                self.wq = .240
            elif self.good * 2.9 < self.bad and self.good * 3.2 > self.bad:
                self.wq = .275
            elif self.good * 2.7 < self.bad and self.good * 2.9 > self.bad:
                self.wq = .280

            # Блок 2
            elif self.good * 2.2 < self.bad and self.good * 2.5 > self.bad:
                self.wq = .325
            elif self.good * 1.9 < self.bad and self.good * 2.2 > self.bad:
                self.wq = .350
            elif self.good * 1.6 < self.bad and self.good * 1.9 > self.bad:
                self.wq = .375
            elif self.good * 1.3 < self.bad and self.good * 1.6 > self.bad:
                self.wq = .400
            elif self.good * 1.0 < self.bad and self.good * 1.3 > self.bad:
                self.wq = .425
            elif self.good * 0.7 < self.bad and self.good * 1.0 > self.bad:
                self.wq = .450
            elif self.good * 0.5 < self.bad and self.good * 0.7 > self.bad:
                self.wq = .475
            elif self.good * 0.3 < self.bad and self.good * 0.5 > self.bad:
                self.wq = .485

        if self.good > self.bad:
                # Блок 3
            if self.bad * 0.3 < self.good and self.bad * 0.5 > self.good:
                self.wq = .525
            elif self.bad * 0.5 < self.good and self.bad * 0.7 > self.good:
                self.wq = .550
            elif self.bad * 0.7 < self.good and self.bad * 1.0 > self.good:
                self.wq = .575
            elif self.bad * 1.0 < self.good and self.bad * 1.3 > self.good:
                self.wq = .600
            elif self.bad * 1.3 < self.good and self.bad * 1.6 > self.good:
                self.wq = .625
            elif self.bad * 1.6 < self.good and self.bad * 1.9 > self.good:
                self.wq = .650
            elif self.bad * 1.9 < self.good and self.bad * 2.2 > self.good:
                self.wq = .675
            elif self.bad * 2.2 < self.good and self.bad * 2.5 > self.good:
                self.wq = .685

                # Блок 4
            if self.bad * 2.7 < self.good and self.bad * 2.9 > self.good:
                self.wq = .725
            elif self.bad * 3.0 < self.good and self.bad * 3.2 > self.good:
                self.wq = .750
            elif self.bad * 3.3 < self.good and self.bad * 3.5 > self.good:
                self.wq = .775
            elif self.bad * 3.6 < self.good and self.bad * 3.8 > self.good:
                self.wq = .800
            elif self.bad * 3.9 < self.good and self.bad * 4.1 > self.good:
                self.wq = .825
            elif self.bad * 4.2 < self.good and self.bad * 4.4 > self.good:
                self.wq = .850
            elif self.bad * 4.5 < self.good and self.bad * 4.7 > self.good:
                self.wq = .875
            elif self.bad * 4.7 < self.good and self.bad * 5.0 > self.good:
                self.wq = .885

        self.wqa = self.wq
        self.wqa = self.wq - .04
        

        #self.tomain


class Golos(Screen):
    def __init__(self, **kw):
        super(Golos, self).__init__(**kw)

        self.main = Main(name = 'main')
        self.than = Thank(name = 'thank')

        self.blq = BoxLayout(orientation="vertical")
        self.blq.add_widget(Button(text="Назад к главному окну --->", size_hint=(1, .2),on_press=lambda x:self.tomain()))
        self.blq.add_widget(Button(text="Отвратительно!", on_press=lambda x:self.main.enjoy(num=-3)))
        self.blq.add_widget(Button(text="Плохо", on_press=lambda x:self.main.enjoy(num=-2)))
        self.blq.add_widget(Button(text="Нормально", on_press=lambda x:self.main.enjoy(num=1)))
        self.blq.add_widget(Button(text="Хорошо", on_press=lambda x:self.main.enjoy(num=2)))
        self.blq.add_widget(Button(text="Превосходно!", on_press=lambda x:self.main.enjoy(num=3)))
        self.add_widget(self.blq)

    def tomain(self):
        self.blq.opacity = 0
        set_screen('main')
        anom = Animation(
            opacity=1,
            duration=2
        )

        anom += Animation(
            opacity=0,
            duration=1.5
        )
        

        anim = Animation(
            opacity=1,
            duration=1
        )

        achko = Animation(
            pos_hint={'x':.9,'y':self.main.wq},
            duration=random.uniform(0.5, 1.5),
        )

        def tvushka(instance):
            self.haveToUse = True
            self.smile_Check()



        def por(instance):
            if self.wq == 0:
                pass
                self.haveToUse = True
            else:
                achko.start(self.point)
                achko.on_complete=tvushka

        def lor(instance):
            anim.start(self.fl)
            anim.on_complete=por

        anom.start(self.than.thanksText)
        anom.on_complete=self.lor()

class Thank(Screen):
    def __init__(self, **kw):
        super(Thank, self).__init__(**kw)
        self.thanksText = Label(text="Спасибо за голос!", font_size=70, opacity=0)
        self.add_widget(self.thanksText)

def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManager()
#sm.add_widget(Start(name = 'start'))
sm.add_widget(Main(name = 'main'))
sm.add_widget(Golos(name = 'golos'))
sm.add_widget(Thank(name = 'thank'))


class Application(App):
    def build(self):
        return sm
    

Application().run()