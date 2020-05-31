import tkinter as tk 
from tkinter import ttk 
import pickle
import paho.mqtt.client as mqtt
import time 
import os

temp_action =  []
 
pkl_file = open('users.pkl', 'rb')
dic = pickle.load(pkl_file)
pkl_file.close()

def save():
    global temp_action 
    dic[userchosen.get()] = temp_action 
    temp_action = []
    output = open('users.pkl', 'wb')
    pickle.dump(dic, output)
    output.close()
    return 1

def Clear():
    dic[userchosen.get()] = []
    temp_action = []
    x = " "
    label1.configure(text = " ")
    return 1


def show():
    global label1 
    x = "User : " + str(userchosen.get()) + "Actions :" + str(temp_action)
    label1.configure(text = x)
    return 1

def Add():
    temp_action.append(actionchosen.get())
    return 1

def goingOut():
    ourClient = mqtt.Client("TEST") 
    ourClient.connect("test.mosquitto.org", 1883) 
    ourClient.loop_start()
    ourClient.publish("WELCOME_HOME", "-all-off")
    
def WELCOMEHOME():
    exec(open('WELCOMEHOMESYSTEM.py').read())


window = tk.Tk() 
window.geometry('900x550') 

  
# label text for title 
ttk.Label(window, text = "Welcome Home Control Centre",  
          background = 'black', foreground ="white",  
          font = ("Times New Roman", 15)).grid(row = 0, column = 0)

ttk.Label(window, text = "Please add all users data before saving", background = 'white',
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 1, padx = 10, pady = 25)

# label 
ttk.Label(window, text = "Select the Action :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 6, padx = 10, pady = 25)

ttk.Label(window, text = "Select  User :", 
          font = ("Times New Roman", 10)).grid(column = 0, 
          row = 5, padx = 10, pady = 25)

label1 = ttk.Label(window, text = "No user selected to view", background = 'white',
          font = ("Times New Roman", 10))

label1.grid(column = 0, 
          row = 9,  padx = 10, pady = 25)
 
 
# Combobox creation 
n = tk.StringVar()
actionchosen = ttk.Combobox(window, width = 27, textvariable = n)  
actionchosen['values'] = ("-study-light-on", "-kettle-on","-altered-carbon-on","-atypical-on","-loung-light-on") 
actionchosen.grid(column = 1, row = 6) 
actionchosen.current()

p = tk.StringVar() 
userchosen = ttk.Combobox(window, width = 27, textvariable = p)
userchosen['values'] = ('Nick','Sawako') 
userchosen.grid(column = 1, row = 5) 
userchosen.current()


button = tk.Button(window, text="Add action", bg="White", command=Add)
button.grid(row=7, column=1)

buttonclear = tk.Button(window, text="Clear User Data", bg="White", command=Clear)
buttonclear.grid(row=8, column=1)

buttonsave = tk.Button(window, text="Save User Data", bg="White", command=save)
buttonsave.grid(row=7, column=0)

buttonsave = tk.Button(window, text="Show user data", bg="White", command=show)
buttonsave.grid(row=8, column=0)

buttonoff = tk.Button(window, text="Going out", bg="White", command=goingOut)
buttonoff.grid(row=10, column=0)

buttonhome = tk.Button(window, text="I'm home", bg="White", command=WELCOMEHOME)
buttonhome.grid(row=10, column=1)

window.mainloop() 