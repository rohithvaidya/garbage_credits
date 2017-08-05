from Tkinter import *

import tkFont
import tkMessageBox
import tkFileDialog
from Tkinter import Label
from Tkinter import Listbox
from Tkinter import Entry
import os
import time

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from skimage import io,data

import requests
from requests.auth import HTTPBasicAuth




import sys
def quit():
    root.quit()


def reset():
    file_names.clear()
    items.clear()
    items.clear()
    status_str.set("All values reseted")

def login():
    try:
        r=requests.get('http://localhost:5000/login', auth=(e1.get(), e2.get()))
    except:
        tkMessageBox.showinfo("Sign in", "Could not connect to server ")

    print r.text
    if(len(str(r.text)) != 37):
        tkMessageBox.showinfo("Sign in", "Logged in successfully")
        uname=e1.get()
        pas=e2.get()
        window()

    else:
        tkMessageBox.showinfo("Sign in", "Credentials incorrect .. Try again")
        return

def set_credit():
    url = 'http://localhost:5000/set_credit/{}'.format(e_credit.get())
    try:
        cmd = "curl -i "+url
        os.system(cmd)

    except:
        tkMessageBox.showinfo("Status", "Could not connect to server ")

def get_credit():
    url = 'http://localhost:5000/get_credit'
    try:
        r=requests.get(url)
        credit.set(r.text)
    except:
        tkMessageBox.showinfo("Status", "Could not connect to server ")

def remove_users():
    url = 'http://localhost:5000/remove'
    try:
        cmd = "curl -i "+url
        os.system(cmd)

    except:
        tkMessageBox.showinfo("Status", "Could not connect to server ")

def plot():
    url = 'http://localhost:5000/sort_by_loc/{}'.format(e_l.get())
    try:
        r=requests.get(url)
        print list(r.text)

    except:
        tkMessageBox.showinfo("Status", "Could not connect to server ")

def window():
    root1 = Tk()
    root.quit()

    root1.title("Admin panel")
    #root1.geometry("800x450")

    menubar = Menu(root1)
    root1.config(menu=menubar)


    file_menu = Menu(menubar,tearoff=False)
    menubar.add_cascade(label="File",menu=file_menu)
    file_menu.add_command(label="Quit",command=quit)



    credit = StringVar(root1)
    global credit
    status_str = StringVar(root1)


    root1.attributes("-fullscreen",True)                    #Uncomment if full screen is needed
    tfont = tkFont.Font(root=root1 , family="Eurostyle",size=20)
    button_font = tkFont.Font(root=root1, family="Eurostyle",size=20)
    label_font = tkFont.Font(root=root1 , family="Eurostyle",size=20)
    login_font = tkFont.Font(root=root1 , family="Eurostyle",size=30)


    title = Label(root1 , text = "Login" , font=tfont,background='white')
    title.pack(fill = X)
    title.configure(background="steel blue")

    frame = Frame(root1)
    frame.pack(fill = BOTH)
    frame.configure(background='sky blue')

    frame1 = Frame(root1)
    frame1.pack(fill = BOTH)
    frame1.configure(background='sky blue')


    status = Label(frame,textvariable = status_str,font = label_font)

    l1 = Label(frame,text="User Management",font = label_font)


    l2 = Label(frame,text="Current credit cost /kg",font = label_font)
    l3 = Label(frame,textvariable=credit,font = label_font)
    l4 = Label(frame,text="Set new credit cost /kg",font = label_font)
    e_credit = Entry(frame, width=30)
    global e_credit
    b1 = Button(frame,command=set_credit,font=button_font,text="set credit value")
    b2 = Button(frame,command=get_credit,font=button_font,text="get credit value")
    b3 = Button(frame,command=remove_users,font=button_font,text="Remove all users")



    a1 = Label(frame1,text="Graphical Analysis based on location",font = label_font)
    a2 = Label(frame1,text="Enter location id",font = label_font)
    e_l = Entry(frame1, width=30)
    a3 = Button(frame1,command=plot,font=button_font,text="Plot")




    l1.grid(row=0,column=0,padx=50,pady=50)
    l2.grid(row=1,column=0,padx=50,pady=50)
    l3.grid(row=1,column=1,padx=50,pady=50)
    b2.grid(row=1,column=2,padx=50,pady=50)
    l4.grid(row=2,column=0,padx=50,pady=50)
    e_credit.grid(row=2,column=1,padx=50,pady=50,ipady=5)
    b1.grid(row=2,column=2,padx=50,pady=50)
    b3.grid(row=3,column=0,padx=50,pady=50)


    a1.grid(row=0,column=1,padx=5)
    a2.grid(row=1,column=0,padx=5)
    e_l.grid(row=1,column=1,padx=5)
    a2.grid(row=2,column=0,padx=5)



    root1.mainloop()










root = Tk()
root.title("Login")
root.geometry("800x450")

menubar = Menu(root)
root.config(menu=menubar)


file_menu = Menu(menubar,tearoff=False)
menubar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Reset all users",command=reset)
file_menu.add_command(label="Quit",command=quit)






var = StringVar(root)
status_str = StringVar(root)

uname=""
pas=""



root.attributes("-fullscreen",True)                    #Uncomment if full screen is needed
tfont = tkFont.Font(root=root , family="Eurostyle",size=20)
button_font = tkFont.Font(root=root , family="Eurostyle",size=20)
label_font = tkFont.Font(root=root , family="Eurostyle",size=20)
login_font = tkFont.Font(root=root , family="Eurostyle",size=30)


title = Label(root , text = "Login" , font=tfont,background='white')
title.pack(fill = X)
title.configure(background="steel blue")

frame = Frame(root)
frame.pack(fill = BOTH)
frame.configure(background='sky blue')


l1 = Label(frame,text="Username",font = login_font)
e1 = Entry(frame, width=30)

l2 = Label(frame,text="Password",font = login_font)
e2 = Entry(frame, width=30)

login = Button(frame,text="Sign in",command=login,font=login_font)



l1.grid(row=0,column=0,padx=100,pady=200)
e1.grid(row=0,column=1,padx=100,pady=200,ipady=10)

l2.grid(row=1,column=0,padx=100,pady=200)
e2.grid(row=1,column=1,padx=100,pady=200,ipady=10)

login.grid(row=5,padx=200)
root.mainloop()
