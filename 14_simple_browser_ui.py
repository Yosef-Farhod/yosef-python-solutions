# Simple Browser UI:
# This script creates a basic web browser interface using Tkinter.
# The user can enter a URL and open it in the default browser,
# or click buttons to quickly open YouTube, Facebook, or Instagram.

from tkinter import *
from tkinter import ttk 
import webbrowser
 
def go () :
    web=link.get()
    webbrowser.open(web)
def link_youtub () :
    webbrowser.open('https://www.youtube.com/')
def link_face () :
    webbrowser.open('https://www.facebook.com/')
def link_insta () :
    webbrowser.open('https://www.instagram.com/')

op = Tk()
op.title('Fire Fox')
op.geometry('600x500')
op.config(background='gray')

shoo_text = Label(op ,text=' Fire Fox',fg='black',bg='yellow',font='tahoma 30 bold',padx=10,pady=10)
shoo_text.pack()

link = Entry(op,width=50)
link.pack(pady=30)

button_link = Button(op,text='Go to link',command=go)
button_link.pack()

youtub=Button(op,text='youtub',fg='red',command=link_youtub)
youtub.place(x=50,y=400)

face_book =Button(op,text='face book',fg='blue',command=link_face)
face_book.place(x=150,y=400)

insta =Button(op,text='insta',fg='red',command=link_insta)
insta.# Simple Browser UI:
# This script creates a basic web browser interface using Tkinter.
# The user can enter a URL and open it in the default browser,
# or click buttons to quickly open YouTube, Facebook, or Instagram.

from tkinter import *
from tkinter import ttk 
import webbrowser
 
def go () :
    web=link.get()
    webbrowser.open(web)
def link_youtub () :
    webbrowser.open('https://www.youtube.com/')
def link_face () :
    webbrowser.open('https://www.facebook.com/')
def link_insta () :
    webbrowser.open('https://www.instagram.com/')

op = Tk()
op.title('Fire Fox')
op.geometry('600x500')
op.config(background='gray')

shoo_text = Label(op ,text=' Fire Fox',fg='black',bg='yellow',font='tahoma 30 bold',padx=10,pady=10)
shoo_text.pack()

link = Entry(op,width=50)
link.pack(pady=30)

button_link = Button(op,text='Go to link',command=go)
button_link.pack()

youtub=Button(op,text='youtub',fg='red',command=link_youtub)
youtub.place(x=50,y=400)

face_book =Button(op,text='face book',fg='blue',command=link_face)
face_book.place(x=150,y=400)

insta =Button(op,text='insta',fg='red',command=link_insta)
insta.place(x=275,y=400)


op.mainloop()