# User Preferences Form:
# This GUI application allows users to select their gender and preferred languages
# using radio buttons and checkboxes. It also includes a simple dropdown menu
# for extra actions like Settings and Exit.

from tkinter import *
from tkinter import ttk

yosef = Tk()
yosef.title('Yosef')
yosef.geometry('500x600+500+100')
def kji() :
    text1 = Label(yosef,text='Enter your type :',fg='black',bg='white',font='10')
    text1.place(x=50,y=10)

    tti1=ttk.Radiobutton(yosef,text='man',value=0)
    tti1.place(x=50,y=50)
    tti=ttk.Radiobutton(yosef,text='women',value=1)
    tti.place(x=50,y=80)

    lang=Label(yosef,text='Enter your langht :',fg='black',bg='white',font='10')
    lang.place(x=50,y=120)

    lang1=Checkbutton(yosef,text='Arbc',variable=0)
    lang1.place(x=50,y=140)

    lang2=Checkbutton(yosef,text='English',variable=1)
    lang2.place(x=50,y=160)

    lang3=Checkbutton(yosef,text='French',variable=2)
    lang3.place(x=50,y=180)


    menu1=Menubutton(yosef,text='Menu',fg='black',bg='white',font='10',relief='groove')
    menu1.place(x=50,y=220)

kji()



yosef.mainloop()