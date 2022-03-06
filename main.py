from cgitb import text
from csv import writer
from msilib.schema import tables
from this import s
from winsound import PlaySound
from kivy.uix.popup import Popup
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import ScreenManager, Screen, WipeTransition
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivymd.uix.label import MDLabel
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.animation import Animation
from kivy.clock import Clock
from datetime import datetime
from congrat import Congrat
from kivymd.toast import toast
from kivy.config import Config
from kivymd.uix.datatables import MDDataTable
from kivy.properties import ObjectProperty
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.picker import MDDatePicker
from kivymd.uix.picker import MDTimePicker
import time
from datetime import timedelta
from kivy.clock import Clock
from datetime import datetime as d
from threading import Timer
import os


class Starting(Screen, FloatLayout):
    pass
class Event(Screen):
    pass

class Main(Screen):
    pass

class WindowManager(ScreenManager):
    pass


card=1
class list:
    date,time,b1,b2=0,0,0,0
screen=1
table=1
write=1
def Write1(self,t1,t2):
    global card,write
    card.remove_widget(screen)
    manager= self.root.ids.screen_manager
    manager.transition= WipeTransition()
    manager.transition.duration= 0.8
    manager.current= 'start_screen'
    list.date=str(list.date)
    list.time=str(list.time )
    s=open("database.txt","r")
    k2=s.readlines()
    s.close()
    
    write=[]
    lol=[]
    s=open("database.txt","w")
    if k2!=['\n'] and k2!=[]:
        for i in k2:
            h=eval(i)
            write.append(h)
            lol.append(h[0])
        if t1 in lol:
            write[lol.index(t1)][1],write[lol.index(t1)][2],write[lol.index(t1)][3]=list.date,list.time,t2
        else:
            k=[t1,list.date,list.time,t2]
            write.append(k)
        u=[]
        for i in write:
            u.append(repr(i)+'\n')
        s.writelines(u)
    else:
        k=[t1,list.date,list.time,t2]
        write.append(k)
        u=[]
        for i in write:
            u.append(repr(i)+'\n')
        s.writelines(u)
    s.close()
def DATE(MYAPP):
    # Click OK
    def on_save(instance, value,value_range):
        list.date=value

    # Click Cancel
    def on_cancel(instance, value):
        pass

    #date_dialog = MDDatePicker(year=2000, month=2, day=14)
    date_dialog = MDDatePicker()
    date_dialog.bind(on_save=on_save, on_cancel=on_cancel)
    date_dialog.open()



def Time(MYAPP):
    def get_time(instance, time):
        list.time=time
    # Cancel
    def on_cancel(instance, time):
        pass

    from datetime import datetime

    # Define default time
    default_time = datetime.strptime("4:20:00", '%H:%M:%S').time()

    time_dialog = MDTimePicker()
    # Set default Time
    time_dialog.set_time(default_time)
    time_dialog.bind(on_cancel=on_cancel, time=get_time)
    time_dialog.open()
def update_clock(self, *args):
    now = d.now() + timedelta(seconds = 10)
    T = now.strftime('%Y-%m-%d %H:%M').split()
    ON=open('database.txt','r')
    data=ON.readlines()
    ON.close()
    write=[]
    if data!=['\n'] and data!=[]:
        for i in data:
            h=eval(i)
            write.append(h)
    for i in write:
        if i[1]==T[0] and i[2][:-3]==T[1]:
            layout = GridLayout(cols = 1, padding = 10)
            label = Label(text = i[3])
            closeButton = Button(text = "Close the pop-up")
            layout.add_widget(label)
            layout.add_widget(closeButton) 
            popup = Popup(title =i[0],
                        content = layout,
                        size_hint =(None, None), size =(200, 200))  
            popup.open()   
            closeButton.bind(on_press = popup.dismiss) 
    
class MainApp(MDApp):
    ind= 0
    minutes= 0
    sub_mins= 0
    secs= range(59, -1, -1)
    is50= 'no'
    isbreak= False
    
    def build(self):
        Config.set('graphics', 'resizable', False)
        Window.size= (360, 640)
        Window.minimum_width, Window.minimum_height = (360, 640)
        return Builder.load_file("main.kv")
    def lol():
        Clock.schedule_interval(update_clock,10)
    lol()
    
    def enable_btn(self, name, *args):
        self.btn.disabled= False
        with open('data/username.txt', 'w') as file:
            file.write(name.strip())

    def on_start(self):
        card= self.root.ids.start_screen.ids['the_card']
        self.btn= self.root.ids.start_screen.ids['btn']
        with open('data/username.txt', 'r') as username:
            content= username.read()
        if content == '':
            card.height= 150
            self.btn.disabled= True
            self.container= FloatLayout()
            self.text= Label(text='let us know your username:',
                             size_hint=[.7, .2],
                             pos_hint={"top":.95, 'x':.1},
                             font_size='20sp',
                             bold=True,
                             color=[0,0,0,1])
            self.feild= TextInput(background_color=get_color_from_hex('#730000'),
                             size_hint=[.9, .3],
                             pos_hint={"top":.6, 'center_x':.5},
                             hint_text='your username...'.upper(),
                             hint_text_color=[0,0,0,1],
                             multiline=False)
            self.butn= Button(text='Done',
                             background_normal='',
                             color=[0,0,0,1],
                             background_color=get_color_from_hex('#730088'),
                             size_hint=[.9, .2],
                             pos_hint={"top":.25, 'center_x':.5},
                             font_size="20sp",
                             bold=True)
            self.butn.bind(on_release= lambda x: self.enable_btn(self.feild.text) if
                           self.feild.text!='' else print('enter your name'))
            self.container.add_widget(self.text)
            self.container.add_widget(self.feild)
            self.container.add_widget(self.butn)
            card.add_widget(self.container)
        elif content != '':
            card.height= 190
            self.container= FloatLayout()
            self.text1= Label(text='Welcome Back {}!'.format(content.title()),
                              size_hint=[.8, .2],
                              pos_hint={"top":.9, 'x':.1},
                              font_size='27sp',
                              bold=True,
                              color=[0,0,0,1])
            self.text2= Label(text='HAPPY FOCUS :)',
                              size_hint=[.6, .2],
                              pos_hint={"top":.23, 'x':.1},
                              font_size='27sp',
                              bold=True,
                              color=[0,0,0,1])
            self.para= Label(text='''make sure that you\'re not surrounded\nby any sort of distractions...\nyou can click the green button\nwhenever you\'re ready.''',
                             font_size='17sp',
                             size_hint=[.7, .4],
                             pos_hint={"top":.7, 'x':.18},
                             color= [0,0,0,1])
            self.container.add_widget(self.text1)
            self.container.add_widget(self.para)
            self.container.add_widget(self.text2)
            card.add_widget(self.container)

    def switch_to_main(self):
        manager= self.root.ids.screen_manager
        manager.transition= WipeTransition()
        manager.transition.duration= 0.8
        manager.current= 'main_screen'
    def switch_to_main_cal(self,instance):
        global card
        card.remove_widget(screen)
        manager= self.root.ids.screen_manager
        manager.transition= WipeTransition()
        manager.transition.duration= 0.8
        manager.current= 'start_screen'
    def input1(self,l):
        global table,screen,b4,row_data
        if table!=1:
            screen.remove_widget(table)
            screen.remove_widget(b4)
        def Write(l):
            Write1(self,t1.text,t3.text)
        l2= Label(
            text="Add Name",pos_hint = {'x': 0.1, 'y': 0.5},
            size_hint=(0.3, 0.05))
        l3= Label(
            text="Add brief",
            pos_hint = {'x': 0.1, 'y': 0.4},
            size_hint=(0.3, 0.05))
        t1= TextInput(
            text='',
            pos_hint = {'x': 0.45, 'y': 0.5},
            size_hint=(0.3, 0.05))
        t3= TextInput(
            text='',
            pos_hint = {'x': 0.45, 'y': 0.4},
            size_hint=(0.3, 0.05))
        b1 = Button(
            text="SET DATE",
            pos_hint={'x':.1, 'y': .3},
            size_hint=(0.3, 0.05))
        screen.add_widget(b1)
        b1.bind(on_press=DATE)
        b2 = Button(
            text="Set TIME",
            pos_hint={'x': .45, 'y': .3},
            size_hint=(0.3, 0.05))
        screen.add_widget(b2)
        b2.bind(on_press=Time)
        if l==["Event"]:
            change="Submit"
        else:
            change="Submit"
            l=str(l)
            for i in row_data:
                if l[:5]!='<kivy' and i[0]==l[0]:
                    change="Edit"
                    label1=Label(
                    text="Event:"+str(i[0])+"\nTime:"+str(i[1])+"\nDate:"+str(i[2])+"\nBrief:"+str(i[3]),
                    size_hint=[.6, .35],
                    pos_hint={'x':.18,'y':.6,},
                    font_size='18sp',color=get_color_from_hex('#FFC300'))
                    screen.add_widget(label1)
                    break
        b3 = Button(
            text=change,
            pos_hint={'x': .5, 'y': .2},
            size_hint=(0.3, 0.05))
        screen.add_widget(b3)
        
        b3.bind(on_press=Write)
        screen.add_widget(l2)
        screen.add_widget(t1)
        screen.add_widget(t3)
        screen.add_widget(l3)
    def switch_to_Calender(self):
        global screen
        global card,table,b4,row_data
        manager= self.root.ids.screen_manager
        manager.transition= WipeTransition()
        manager.transition.duration= 0.8
        manager.current= 'event_screen'
        card= self.root.ids.event_screen.ids['the_card']
        s1=open("database.txt","r")
        k1=s1.readlines()
        row_data=[]
        name=[]
        if k1!=['\n'] and k1!=[]:
            for i in k1:
                h=eval(i)
                j=(h[0],h[1],h[2],h[3])
                row_data.append(j)
                k1=(h[0],)
                name.append(k1)
            
        else:
            name.append(("ADD Event",))
        
        screen= Screen()
        
        table= MDDataTable(
            use_pagination=True,
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint =(0.9, 0.6),
            column_data = [
                ("Event", dp(40),),
            ],
            row_data=name
            )
        Go_back= Button(
            text="GO BACK",
            pos_hint={'center_x': .8, 'center_y': .9},
            size_hint=(0.3, 0.05))
        
        Go_back.bind(on_press=self.switch_to_main_cal)
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.on_row_press)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        screen.add_widget(table)
        screen.add_widget(Go_back)
        

        if name!=[("Event",)]:
            b4 = Button(
            text="ADD EVENT",
            pos_hint={'center_x': .8, 'center_y': .15},
            size_hint=(0.3, 0.05))
            screen.add_widget(b4)
            b4.bind(on_release=self.input1)
        card.add_widget(screen)
    

    def checked(self, instance_table, current_row):
        pass
    # Function for row presses
    def on_row_press(self,  table1, row):
        global screen,table
        screen.remove_widget(table1)
        start_index, end_index = row.table.recycle_data[row.index]["range"]
        l=[]
        for i in range(start_index, end_index+1):
            l.append(row.table.recycle_data[i]["text"])
        table=1
        self.input1(l)

    def get_time(self, period):
        self.minutes= period
        self.updater=Clock.schedule_interval(self.countdown, 1)
        self.play_sound()

    def countdown(self, *args):
        timer_lbl= self.root.ids.main_screen.ids.timer
        btn25= self.root.ids.main_screen.ids.the25
        btn50= self.root.ids.main_screen.ids.the50
        timer= [1,1]
        if self.minutes == 0 and self.ind == 60:
            if self.isbreak == True:
                self.call_popup()
                toast('Take a Break!', 1)
            else: pass
            self.stop_it()
            self.updater.cancel() #this function cancels the countdown
            btn25.disabled= False
            btn50.disabled= False
        else:
            if self.ind == 60:
                self.ind=0
                self.seconds= self.secs[self.ind]
                self.ind+=1
            else:
                self.seconds= self.secs[self.ind]
                self.ind+=1
            timer[1]=str(self.seconds)
            if timer[1] == '59':
                #self.sub_mins+=1
                self.minutes= self.minutes - 1
            else:
                pass
            timer[0]=str(self.minutes)
            timer_lbl.text= f'{timer[0].zfill(2)}:{timer[1].zfill(2)}'
            self.clock_highlighting()

    def clock_highlighting(self):
        self.min_nums= [self.root.ids.main_screen.ids.n1, self.root.ids.main_screen.ids.n2,
                    self.root.ids.main_screen.ids.n3, self.root.ids.main_screen.ids.n4,
                    self.root.ids.main_screen.ids.n5, self.root.ids.main_screen.ids.n6,
                    self.root.ids.main_screen.ids.n7, self.root.ids.main_screen.ids.n8,
                    self.root.ids.main_screen.ids.n9, self.root.ids.main_screen.ids.n10,
                    self.root.ids.main_screen.ids.n11, self.root.ids.main_screen.ids.n12,
                    self.root.ids.main_screen.ids.n13]
        if (self.is50 == 'yes' and self.minutes == 20) and self.ind == 60:
            self.min_nums[6].color= [0,1,0,1]
        elif  (self.is50 == 'yes' and self.minutes == 15) and self.ind == 60:
            self.min_nums[7].color= [0,1,0,1]
        elif  (self.is50 == 'yes' and self.minutes == 10) and self.ind == 60:
            self.min_nums[8].color= [0,1,0,1]
        elif  (self.is50 == 'yes' and self.minutes == 5) and self.ind == 60:
            self.min_nums[9].color= [0,1,0,1]
        elif  (self.is50 == 'yes' and self.minutes == 0) and self.ind == 60:
            self.min_nums[10].color= [0,1,0,1]
        elif (self.minutes == 24 or self.minutes == 49) and self.ind == 60:
            self.min_nums[0].color= [0,1,0,1]
        elif (self.minutes == 20 or self.minutes == 45) and self.ind == 60:
            self.min_nums[1].color= [0,1,0,1]
        elif (self.minutes == 15 or self.minutes == 40) and self.ind == 60:
            self.min_nums[2].color= [0,1,0,1]
        elif (self.minutes == 10 or self.minutes == 35) and self.ind == 60:
            self.min_nums[3].color= [0,1,0,1]
        elif (self.minutes == 5 or self.minutes == 30) and self.ind == 60:
            self.min_nums[4].color= [0,1,0,1]
        elif(self.minutes == 0 or self.minutes == 25) and self.ind == 60:
            self.min_nums[5].color= [0,1,0,1]
        else: pass

    # gives all self.min_nums a black color
    def reseter(self):
        for lbl in self.min_nums:
            lbl.color= [0,0,0,1]

    def stop_it(self):
        tbtn25= self.root.ids.main_screen.ids.the25
        rr= self.root.ids.main_screen.ids.tt
        tbtn50= self.root.ids.main_screen.ids.the50
        ttimer_lbl= self.root.ids.main_screen.ids.timer
        stoper= self.root.ids.main_screen.ids.stop_timer
        self.updater.cancel()
        tbtn25.disabled= False
        tbtn50.disabled= False
        stoper.disabled= True
        rr.source='imgs/timer.png'
        ttimer_lbl.text= '00:00'
        self.reseter()
        self.ind= 0
        self.minutes= 0
        self.sub_mins= 0
        self.secs= range(59, -1, -1)
        self.sound.stop()

    def call_popup(self):
        pop= Congrat(app)
        pop.open()
        self.pomodone_sound()

    def play_sound(self):
        i=1
        self.sound= SoundLoader.load("sounds/"+str(i)+".mp3")
        self.sound.play()
        s=self.sound.length
        self.sound.loop=True
    
    def pomodone_sound(self):
        self.noise= SoundLoader.load('sounds/noise.wav')
        self.noise.play()


    def reset_btns(self):
        self.root.ids.main_screen.ids.the25.disabled= True
        self.root.ids.main_screen.ids.the50.disabled= True
        self.root.ids.main_screen.ids.stop_timer.disabled= False

if __name__ == '__main__':
    app= MainApp()
    app.run()
