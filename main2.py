from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.modalview import ModalView
from kivy.uix.image import Image
money=0
from random import randint
from kivy.uix.gridlayout import GridLayout
import time
from kivy.clock import Clock
from kivy.uix.slider import Slider

nem="Иван"
wodit=False
program=False
preng=False
bog=False
mag=False
eda=100
ura=100
god=100
rasum=100
s=0
den=0
m=0
ilon=21000000000000
gus=0
ping=0
cuc=0
owsa=0
cow=0
all=gus+ping+cuc+owsa+cow

def savescot():
    global s
    try:
        f=open("scot.dat","w")
        s=str(gus)+","+str(ping)+","+str(cuc)+","+str(owsa)+","+str(cow)
        f.write(s)
        f.close()
    except:
        print("ошибка создания фаила,Казино закрывается")
        quit(0)



def loadscot():
    global gus,ping,cuc,owsa,cow,all
    try:
        f=open("scot.dat","r")
        
        
        m=(f.readline())
        f.close()
        i=m.split(",")
        gus=int(i[0])
        ping=int(i[1])
        cuc=int(i[2])
        owsa=int(i[3])
        cow=int(i[4])
        all=gus+ping+cuc+owsa+cow
    except FileNotFoundError:
               print("фаила не существует..")
               m=givemoney

loadscot()
def saveobux():
    global s
    try:
        f=open("saveobus.dat","w")
        s=str(wodit)+","+str(program)+","+str(preng)+","+str(bog)+","+str(mag)
        f.write(s)
        f.close()
    except:
        print("ошибка создания фаила,Казино закрывается")
        quit(0)

def loadobux():
    global wodit,program,preng,bog,mag,m
    f=open("saveobus.dat","r")
    m=(f.readline())
    f.close()
    i=m.split(",")
    if (i[0])=="False":
        wodit=False
    if (i[0])=="True":
        wodit=True
    if (i[1])=="False":
        program=False
    if (i[1])=="True":
        program=True
    if (i[2])=="False":
        preng =False
    if (i[2])=="True":
        preng =True
    if (i[3])=="False":
        bog=False
    if (i[3])=="True":
        bog =True
    if (i[4])=="False":
        mag=False
    if (i[4])=="True":
        mag=True
    
    
        
    
    
    
    
    

loadobux()
    
    
    
    
def saveMoney(x):
    try:
        f=open("money.dat","w")
        
        f.write(str(x))
        f.close()
    except:
        print("ошибка создания фаила,Казино закрывается")
        quit(0)
def loadMoney():
    try:
        f=open("money.dat","r")
        m=int(f.readline())
        f.close()
    except FileNotFoundError:
               print("фаила не существует..")
               m=givemoney
    return m

def loadstaty():
    global eda,ura,god,rasum
    try:
        f=open("staty.dat","r")
        m=(f.readline())
        f.close()
        i=m.split(",")
        eda=int(i[0])
        ura=int(i[1])
        god=int(i[2])
        rasum=int(i[3])
    except FileNotFoundError:
               print("фаила не существует..")
               m=givemoney
    return m
loadstaty()
money=loadMoney()
alt=50
class MyApp(App):
    
    
      
    
    
    def rest(self,instance):
        if money>300:
            
            self.staty(instance,-300,100,0,0,0)
    def tort(self,instance):
        if money>150:
            self.staty(instance,-150,50,0,0,0)
    def pitza(self,instance):
        if money>80:
            self.staty(instance,-80,35,0,0,0)
    def hotdog(self,instance):
        if money>65:
            self.staty(instance,-65,25,0,0,0)
        
    def schaurma(self,instance):
        if money>35:
            self.staty(instance,-35,15,0,0,0)
        
    def dosh(self,instance):
        if money>15:
            self.staty(instance,-15,5,0,0,0)
            
    def corm(self,instance):
        if money>5:
            self.staty(instance,-5,5,0,0,0)
            
    def obwodit(self,instance):
        global wodit,rasum,money,rasum
        if  wodit==False and money>20000 and rasum>50:
            wodit=True
            saveobux()
            money-=20000
            self.saveslt(instance)
     
    def obprogram(self,instance):
        global program,rasum,money,rasum
        if  program==False and money>200000 and rasum>70:
            program=True
            saveobux()
            money-=200000
            self.saveslt(instance)      
    def obpreng(self,instance):
        global preng,rasum,money
        if  preng==False and money>1000000 and rasum>80:
            preng=True
            saveobux()
            money-=1000000
            self.saveslt(instance)
    def obbog(self,instance):
        global bog,rasum,money
        if  bog==False and money>100000000 and rasum==100:
            bog=True
            saveobux()
            money-=100000000
            self.saveslt(instance)
    def obmag(self,instance):
        global mag,rasum,money
        if  mag==False and money>10000000 and rasum>90:
            mag=True
            saveobux()
            money-=10000000
            self.saveslt(instance) 
         
                 
            
            
    def kniga(self,instance):
        if money>1000:
            self.staty(instance,-1000,-10,5,0,1)
    def util(self,instance):
        if money>4500:
            self.staty(instance,-4500,-30,-15,0,5)
            
            
            
    def savestaty(self,instance):
        try:
            f=open("staty.dat","w")
            g=str(eda) +","+str(ura)+","+str(god)+","+str(rasum)
            f.write(str(g))
            f.close()
        except:
            print("ошибка создания фаила,Игра закрывается")
            quit(0)
    def saveMoney(self,instance,x):
        try:
            f=open("money.dat","w")
            f.write(str(x))
            f.close()
        except:
            print("ошибка создания фаила,Казино закрывается")
            quit(0)
    def dobro(self,instance):
        if money>100:
            self.staty(instance,-100,0,100,0,0)
            
    def gladcot(self,instance):
         self.staty(instance,0,0,1,0,0)
         
         
    
    def pop(self,instance):
     self.staty(instance,1,0,0,0,0)
    def wodit(self,instance):
     global wodit
     if wodit==True:
         self.staty(instance,100,0,0,0,0)
    def pahati(self,instance):
        if eda>5 and ura>10:
            self.staty(instance,10,randint(-10,-5),-3,0,0)
    def kolum(self,instance):
      if eda>10 and ura>10 and god>7 and rasum >10:
          self.staty(instance,randint(10,100),randint(-10,-5),randint(-10,-5),randint(-5,0),randint(-2,0))
    def program(self,instance):
      global program
      if program==True:
          self.staty(instance,1000,10,0,0,0)
    def preng(self,instance):
       global preng
       if preng==True:
          self.staty(instance,5000,0,0,0,0)
    def mag(self,instance):
        global mag
        if mag==True:
            self.staty(instance,10000000,-70,0,-50,0)
            
    def dog(self,instance):
        global bog
        if bog==True:
          self.staty(instance,1000000000000000000,0,0,0,0)
              
          
          
          
          
          
          
          
      
    
         
     
     
    def staty(self,instance,x,y,t,k,i):
        global money,eda,ura,god,rasum
        money+=x
        eda+=y
        ura+=t
        god+=k
        rasum+=i
        
        if eda>100:
            eda=100
        if ura>100:
            ura=100
        if god>100:
            god=100
        if rasum>100:
            rasum=100
        if eda<0:
           eda=0
        if ura<0:
            ura=0
        if god<0:
            god=0
        if rasum<0:
            rasum=0
        saveMoney(money)
        self.savestaty(instance)
        self.saveslt(instance)
    def peda(self, instance):
        self.staty(instance,0,1,0,0,0)
        
    def prasum(self, instance):
        self.staty(instance,0,0,0,0,0.01)
    
    def saveslt(self, instance):
        self.textmoney.text=f"У вас на счету{money}руб"
        self.texteda.text=f"Голод:{eda}/100"
        self.textura.text=f"Настроение:{ura}/100"
        self.textgod.text=f"Здоровье:{god}/100"
        self.textrasum.text=f"Разум:{rasum}/100"
        self.textmoney1.text=f"У вас на счету {money}руб"
        saveMoney(money)
        self.savestaty(instance)
        
    def cupscot(self,instance):
        global cuc,gus,ping,cow,owsa
        if instance.text=="Купить.Стоимость 1000":
           if money>=1000:
               cuc+=1
               self.staty(instance,-1000,0,0,0,0)
               savescot()
               self.textcuc.text=str(cuc)
               all=gus+ping+cuc+owsa+cow
               self.textall.text=str(all)
               
        elif instance.text=="Купить.Стоимость 1800":
           if money>=1800:
               gus+=1
               self.staty(instance,-1800,0,0,0,0)
               savescot()
               self.textgus.text=str(gus)
               all=gus+ping+cuc+owsa+cow
               self.textall.text=str(all)
        elif instance.text=="Купить.Стоимость 10000":
           if money>=10000:
               owsa+=1
               self.staty(instance,-10000,0,0,0,0)
               savescot()
               self.textowsa.text=str(owsa)
               all=gus+ping+cuc+owsa+cow
               self.textall.text=str(all)
        elif instance.text=="Купить.Стоимость 20000":
           if money>=20000:
               ping+=1
               self.staty(instance,-20000,0,0,0,0)
               savescot()
               self.textping.text=str(ping)
               all=gus+ping+cuc+owsa+cow
               self.textall.text=str(all)
        elif instance.text=="Купить.Стоимость 50000":
           if money>=50000:
               cow+=1
               self.staty(instance,-50000,0,0,0,0)
               savescot()
               self.textping.text=str(cow)
               all=gus+ping+cuc+owsa+cow
               self.textall.text=str(all)
    def kan(self,instance):
        if int(self.buttonpas.text)==0:
            self.buttonpas.text="Отправить пасти..."
            self.buttonpas.disabled=False
        else:
            
            r=int(self.buttonpas.text)
            self.buttonpas.text=str(r-1)
            Clock.schedule_once(self.kan,1)
            
    def lek(self,instance):
          self.staty(instance,0,0,0,1,0)
          if randint(1,5)==3:
              self.staty(instance,0,0,0,-4,0)
              
    def selo(self,instance):
          sar=0
          sar+=cuc*15
          sar+=gus*30
          sar+=owsa*150
          sar+=ping*300
          sar+=cow*1000
          self.buttonpas.disabled=True
          self.buttonpas.text="10"
          self.kan(instance)
          self.staty(instance,sar,0,0,0,0)
          
          
    def yt(self,instance):
           self.sel.text=str(value.self.slider)    
           
           

        
    
    def build(self):
        image=Image(source="/storage/emulated/0/inshot/InShot_20211230_145653346.jpg",allow_stretch=True,size_hint=(.1,.1),pos=(200,730))
        
        image1=Image(source="/storage/emulated/0/inshot/InShot_20211230_150903252.jpg",allow_stretch=True,size_hint=(.1,.1),pos=(240,790))
      
        image2=Image(source="/storage/emulated/0/inshot/InShot_20211230_200903152.jpg",allow_stretch=True,size_hint=(.1,.1),pos=(200,670))
        
        image3=Image(source="/storage/emulated/0/inshot/InShot_20211230_201936999.jpg",allow_stretch=True,size_hint=(.1,.1),pos=(200,600))
        gr=GridLayout(cols=6,padding=[0,750,0,0])
        gr4=GridLayout(cols=6,padding=[0,0,0,0])
        bx4=BoxLayout(orientation="vertical")
        fl=FloatLayout(size =(1000,1000))
        bx=BoxLayout()
        fl.add_widget(image)
        fl.add_widget(image1)
        fl.add_widget(image2)
        fl.add_widget(image3)
        gr4.add_widget(Label(text="Куриц:"))
        gr4.add_widget(Label(text="Гусей:"))
        gr4.add_widget(Label(text="Овец:"))
        gr4.add_widget(Label(text="Свиней:"))
        gr4.add_widget(Label(text="Коров:"))
        gr4.add_widget(Label(text="Всего:"))
        self.textcuc=Label(text=str(cuc))
        gr4.add_widget(self.textcuc)
        self.textgus=Label(text=str(gus))
        gr4.add_widget(self.textgus)
        self.textowsa=Label(text=str(owsa))
        gr4.add_widget(self.textowsa)
        self.textping=Label(text=str(ping))
        gr4.add_widget(self.textping)
        self.textcow=Label(text=str(cow))
        gr4.add_widget(self.textcow)
        self.textall=Label(text=str(all))
        gr4.add_widget(self.textall)
        bx4.add_widget(gr4)
        bx5=BoxLayout(orientation="vertical")
        self.sel=Label(text="0")
        
        
        self.slider =Slider(min=1,max=100)
        self.slider.bind(value=self.yt)
        
        bx5.add_widget(self.slider)
        bx5.add_widget(self.sel)
        self.buttonpas=(Button(text="Отправить пасти...",on_press=self.selo))
        bx4.add_widget(self.buttonpas)
        bx4.add_widget(Label(text="Курица.За раз даёт 15 руб."))
        bx4.add_widget(Button(text="Купить.Стоимость 1000",on_press=self.cupscot))
        bx4.add_widget(Label(text="Гусь.За раз даёт 30 руб."))
        bx4.add_widget(Button(text="Купить.Стоимость 1800",on_press=self.cupscot))
        bx4.add_widget(Label(text="Овца.За раз даёт 150 руб."))
        bx4.add_widget(Button(text="Купить.Стоимость 10000",on_press=self.cupscot))
        bx4.add_widget(Label(text="Свинья.За раз даёт 300 руб."))
        bx4.add_widget(Button(text="Купить.Стоимость 20000",on_press=self.cupscot))
        bx4.add_widget(Label(text="Корова.За раз даёт 1000 руб."))
        bx4.add_widget(Button(text="Купить.Стоимость 50000",on_press=self.cupscot))
        
        
        
        
        
        
        
        
        
        
        modallobus=ModalView(size_hint=(None,None),size=(630,1000))
        modalsel=ModalView(size_hint=(None,None),size=(630,1000))
        modalyt=ModalView(size_hint=(None,None),size=(630,1000))
        modamag=ModalView(size_hint=(None,None),size=(630,1000))
        modadom=ModalView(size_hint=(None,None),size=(630,1000))
        modabol=ModalView(size_hint=(None,None),size=(630,1000))
        
     
     

        bx2=BoxLayout(orientation="vertical")
        bx3=BoxLayout(orientation="vertical")
        bx3.add_widget(Label(text="Дом",font_size=60))
        bx3.add_widget(Label(text="Поглатить кота .+1 к настроению",font_size=20))
        bx3.add_widget(Button(text="Бесплатно",on_press=self.gladcot))
        bx3.add_widget(Label(text="Сделать доброе дело.+100 к настроению .",font_size=20))
        bx3.add_widget(Button(text="Купить.Стоимость 100",on_press=self.dobro))
        bx3.add_widget(Label(text="Попросить еду у соседей.+1к голоду .",on_press=self.peda))
        bx3.add_widget(Button(text="Бесплатно",on_press=self.peda))
        
        bx3.add_widget(Label(text="Лечится лечебными травами.+1 к здоровью.20% шанс на отравление.",font_size=15))
        bx3.add_widget(Button(text="Бесплатно",on_press=self.lek))
        fl1=FloatLayout(size =(1000,1000))
        bx1=BoxLayout(orientation="vertical")
        bx2.add_widget(Label(text="Магазин Еды",font_size=60))
        bx2.add_widget(Label(text="Кошачий корм.+5 к голоду",font_size=20))
        bx2.add_widget(Button(text="Купить.Стоимость 5",on_press=self.corm))
        bx2.add_widget(Label(text="Доширак.+5 к голоду",font_size=20))
        bx2.add_widget(Button(text="Купить.Стоимость 15",on_press=self.dosh))
        bx2.add_widget(Label(text="Шаурма.+15 к голоду",font_size=20))
        bx2.add_widget(Button(text="Купить.Стоимость 35",on_press=self.schaurma))
        bx2.add_widget(Label(text=" Хот-дог.+25 к голоду",font_size=20))
        bx2.add_widget(Button(text="Купить.Стоимость 65",on_press=self.hotdog))
        bx2.add_widget(Label(text="Пицца.+35 к голоду",font_size=20))
        bx2.add_widget(Button(text="Купить.Стоимость 80",on_press=self.pitza))
        bx2.add_widget(Label(text="Торт.+50 к голоду",font_size=20))
        bx2.add_widget(Button(text="Купить.Стоимость 150",on_press=self.tort))
        bx2.add_widget(Label(text="Поход в кафе.+100 к голоду",font_size=20))
        bx2.add_widget(Button(text="Купить.Стоимость 300",on_press=self.rest))
        
        
        
        
        
        
        
        
        
        
        bx1.add_widget(Label(text="Обучение",font_size=60))
        
        bx1.add_widget(Label(text="Книга.Увеличевает Разум на 1",font_size=40))
        
        bx1.add_widget(Button(text="Читать книгу.Стоимость 1000",on_press=self.kniga))
        bx1.add_widget(Label(text="Прослушать Лекцию.Увеличивает разум на 5",font_size=20))
        bx1.add_widget(Button(text="Прослушать лекцию.Стоимость 4500",on_press=self.util))
        
        bx1.add_widget(Label(text="Научититься водить машину,Требуется 50 разума",font_size=20))
        bx1.add_widget(Button(text="Стоимость 20000",on_press=self.obwodit))
        bx1.add_widget(Label(text="Научится Програмированию.Требуется 70 Разума",font_size=20))
        bx1.add_widget(Button(text="Стоимость 200000",on_press=self.obprogram))
        bx1.add_widget(Label(text="Стать Призедентом,Требуется 80 Разума",font_size=20))
        bx1.add_widget(Button(text="Стоимость 1000000",on_press=self.obpreng))
        bx1.add_widget(Label(text="Стать Магом.Требуется 90 разума",font_size=20))
        bx1.add_widget(Button(text="Стоимость 10000000",on_press=self.obmag))
        bx1.add_widget(Label(text="Стать Богом.Требуется 100 разума",font_size=20))
        bx1.add_widget(Button(text="Стоимость 100000000",on_press=self.obbog))
        
        
        fl1.add_widget(Label(text="Работа",pos=(260,880),size_hint=(.1,.1),font_size=40))
        fl1.add_widget(Label(text="Попрашайничать.Не тратитит сил,но не приносит большого дохода.",pos=(260,800),size_hint=(.1,.1),font_size=18,))
        fl1.add_widget(Label(text="Таксист.Трубуется навык водителя.Не тратит сил.",pos=(260,680),size_hint=(.1,.1),font_size=20))
        fl1.add_widget(Button(text="100",pos=(10,650),size_hint=(.9,.05),on_press=self.wodit))
        fl1.add_widget(Button(text="1",pos=(10,750),size_hint=(.9,.05),on_press=self.pop))
        fl1.add_widget(Label(text="Огород.Тратит силу,настроение,зато приносит нормально.",pos=(260,580),size_hint=(.1,.1),font_size=20))
        fl1.add_widget(Button(text="10",pos=(10,550),size_hint=(.9,.05),on_press=self.pahati))
        fl1.add_widget(Label(text="Колымить.Не трубуется навыков.Тратис силу,здоровье,настроние и даже разум!",pos=(260,490),size_hint=(.1,.1),font_size=15))
        self.textmoney1=(Label(text=f"У вас на счету:{money}руб.",pos=(260,20),size_hint=(.1,.1),font_size=30))
        fl1.add_widget(self.textmoney1)
        fl1.add_widget(Button(text="random",pos=(10,460),size_hint=(.9,.05),on_press=self.kolum))
        fl1.add_widget(Label(text="Майнить.ТРЕБУЕТСЯ НАВЫК ПРОГРАМИСТА.ПРИНОСИТ ОГРОМНЫЙ ДОХОД!",pos=(260,400),size_hint=(.1,.1),font_size=15))
        fl1.add_widget(Button(text="2000",pos=(10,380),size_hint=(.9,.05),on_press=self.program))
        fl1.add_widget(Label(text="Призедент.ТРЕБУЕТСЯ СТАЖ ПРЕЗЕДЕНДА.Приносит колосальный доход!",pos=(260,320),size_hint=(.1,.1),font_size=15))
        fl1.add_widget(Button(text="5000",pos=(10,290),size_hint=(.9,.05),on_press=self.preng))
        fl1.add_widget(Label(text="Маг.Приносит от 1 до 10000000!!!Тратит много голода и здоровья,требуется навык колдуна",pos=(260,230),size_hint=(.1,.1),font_size=12))
        fl1.add_widget(Button(text="10000000",pos=(10,200),size_hint=(.9,.05),on_press=self.mag))
        fl1.add_widget(Label(text="Бог.ДАЕТ 100000000000000000000000000",pos=(260,130),size_hint=(.1,.1),font_size=25))
        fl1.add_widget(Button(text="Благословить",pos=(10,100),size_hint=(.9,.05),on_press=self.dog))
        fl1.add_widget(Label(text="Также деньги можно получить,разводя сельское хозяйство",pos=(260,40),size_hint=(.1,.1),font_size=20))
        
        
        
        
        modallobus.add_widget(fl1)
        modalyt.add_widget(bx1)
        modamag.add_widget(bx2)
        modadom.add_widget(bx3)
        modalsel.add_widget(bx4)
        modabol.add_widget(bx5)
        
        self.tetxname=(Label(text=f"Ваше имя:{nem}",pos=(80,880),size_hint=(.1,.1)))
        self.tetxname=(Label(text=f"Ваше имя:{m}",pos=(400,880),size_hint=(.1,.1)))
        self.textmoney=(Label(text=f"У вас на счету{money}руб",pos=(450,200),size_hint=(.1,.1)))
        fl.add_widget(self.textmoney)
        fl.add_widget(self.tetxname)
        self.textalt=(Label(text=f"Ваш возраст:{alt}лет",pos=(100,850),size_hint=(.1,.1)))
        fl.add_widget(self.textalt)
        self.texteda=(Label(text=f"Голод:{eda}/100",pos=(68,670),size_hint=(.1,.1)))
        fl.add_widget(self.texteda)
        self.textura=(Label(text=f"Настроение:{ura}/100",pos=(100,790),size_hint=(.1,.1)))
        fl.add_widget(self.textura)
        self.textgod=(Label(text=f"Здоровье:{god}/100",pos=(80,730),size_hint=(.1,.1),outline_color=[1,1,1]))
        fl.add_widget(self.textgod)
        self.textrasum=(Label(text=f"Разум:{rasum}/100",pos=(68,600),size_hint=(.1,.1)))
        fl.add_widget(self.textrasum)
        fl.add_widget(Label(text=f"Цель игры:Поднятся с статуса бомжа и стать са-",pos=(260,560),size_hint=(.1,.1)))
        fl.add_widget(Label(text=f"мым богатым человеком на земле.На момент со-",pos=(265,530),size_hint=(.1,.1)))
        fl.add_widget(Label(text="здания игры одним из богатых и извесных людей ",pos=(265,500),size_hint=(.1,.1)))
        fl.add_widget(Label(text="является Илон Маск со бюджетом 300 000 000 000",pos=(265,470),size_hint=(.1,.1)))
        fl.add_widget(Label(text="доролов или 21 000 000 000 000 рублей.Обгони его",pos=(265,440),size_hint=(.1,.1)))
        fl.add_widget(Label(text="Работая на разных работах и разводя своё хозяйство",pos=(265,410),size_hint=(.1,.1)))
        self.textilon=(Label(text=f"До Илон Маска вам осталось:{21000000000000-money}",pos=(265,380),size_hint=(.1,.1)))
        fl.add_widget(Label(text=f"P.s мне 14 лет,не судите строго это моя первая игра",pos=(265,350),size_hint=(.1,.1)))
        fl.add_widget(self.textilon)
        
        
        gr.add_widget(Button(text="Дом",background_color=[1,1,0,1],on_press=modadom.open))
        gr.add_widget(Button(text="Работа",background_color=[0,0,1,1],on_press=modallobus.open))
        gr.add_widget(Button(text="Магазин",background_color=[1,0,0,1],on_press=modamag.open))
        gr.add_widget(Button(text="Больница",background_color=[0,1,0,1],on_press=modabol.open))
        gr.add_widget(Button(text="Обучение",background_color=[225,0,255],on_press=modalyt.open))
        gr.add_widget(Button(text="Сельское хозяйство",background_color=[0,100,255],font_size=15,on_press=modalsel.open))
        fl.add_widget(gr)
        
        
        return fl
            
        

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    MyApp().run()