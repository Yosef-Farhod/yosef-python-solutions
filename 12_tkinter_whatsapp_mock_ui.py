# Basic Tkinter WhatsApp-like UI:
# This script creates a simple GUI using Tkinter with a top menu bar,
# buttons, radio buttons, and checkboxes for user interaction.

from tkinter import *
from tkinter import ttk

yosef = Tk()
yosef.title('Appliton Yosef')
yosef.geometry('350x650+750+50')
yosef.resizable(False,False)

fra1 =Frame(width='350',height='50',bg='green')
fra1 .place(x=0,y=0)

fra2 =Frame(width='350',height='50',bg='green')
fra2.place(x=0 , y=600)
def button_nothor() :
    bt_search = Entry(fra1,justify='center',fg='white',width=4,bg='green')
    bt_search.place(x=210,y=12)

    bt2_camera = Button(fra1,text='Camera',fg='white',width=5,height=1,bg='green')
    bt2_camera.place(x=270,y=10)

    #زر الخيارات 
    menu1=Menubutton(yosef,text=':',fg='white',bg='green',relief='flat',font=5)
    menu1.place(x=330,y=10)
    ss=Menu(menu1)
    menu1['menu']=ss
    
    ss.add_checkbutton(label='New group')
    ss.add_checkbutton(label='New broadcst ')
    ss.add_checkbutton(label='Linked devices')
    ss.add_checkbutton(label='Settings')
    
    la_whatsApp = Label(fra1,text='Whats App',fg='white',bg='green',font=5)
    la_whatsApp.place(x=20,y=10)
button_nothor()
def kji() :
    text1 = Label(yosef,text='Enter your type :',fg='black',bg='wh# Basic Tkinter WhatsApp-like UI:
# This script creates a simple GUI using Tkinter with a top menu bar,
# buttons, radio buttons, and checkboxes for user interaction.

from tkinter import *
from tkinter import ttk

yosef = Tk()
yosef.title('Appliton Yosef')
yosef.geometry('350x650+750+50')
yosef.resizable(False,False)

fra1 =Frame(width='350',height='50',bg='green')
fra1 .place(x=0,y=0)

fra2 =Frame(width='350',height='50',bg='green')
fra2.place(x=0 , y=600)
def button_nothor() :
    bt_search = Entry(fra1,justify='center',fg='white',width=4,bg='green')
    bt_search.place(x=210,y=12)

    bt2_camera = Button(fra1,text='Camera',fg='white',width=5,height=1,bg='green')
    bt2_camera.place(x=270,y=10)

    #زر الخيارات 
    menu1=Menubutton(yosef,text=':',fg='white',bg='green',relief='flat',font=5)
    menu1.place(x=330,y=10)
    ss=Menu(menu1)
    menu1['menu']=ss
    
    ss.add_checkbutton(label='New group')
    ss.add_checkbutton(label='New broadcst ')
    ss.add_checkbutton(label='Linked devices')
    ss.add_checkbutton(label='Settings')
    
    la_whatsApp = Label(fra1,text='Whats App',fg='white',bg='green',font=5)
    la_whatsApp.place(x=20,y=10)
button_nothor()
def kji() :
    text1 = Label(yosef,text='Enter your type :',fg='black',bg='white',font='10')
    text1.place(x=25,y=50)

    tti1=ttk.Radiobutton(yosef,text='man',value=0)
    tti1.place(x=25,y=80)
    tti=ttk.Radiobutton(yosef,text='women',value=1)
    tti.place(x=25,y=100)

    lang=Label(yosef,text='Enter your langht :',fg='black',bg='white',font='10')
    lang.place(x=25,y=130)

    lang1=Checkbutton(yosef,text='Arbc',variable=0)
    lang1.place(x=25,y=160)

    lang2=Checkbutton(yosef,text='English',variable=1)
    lang2.place(x=25,y=180)

    lang3=Checkbutton(yosef,text='French',variable=2)
    lang3.place(x=25,y=200)
text1= Label(yosef,text='Wellcom to ap')

yosef.mainloop()