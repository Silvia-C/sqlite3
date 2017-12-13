from tkinter import *

window= Tk() #main window

def kg_to_grams():
    #fetch the object as string with get()
    grams=float(e1_value.get())*1000
    t1.insert(END, grams) #put the string in the object

def kg_to_pounds():
    #fetch the object as string with get()
    pounds=float(e1_value.get())*2.20462
    t2.insert(END, pounds) #put the string in the object

def kg_to_ounces():
    #fetch the object as string with get()
    ounces=float(e1_value.get())*35.274
    t3.insert(END, ounces) #put the string in the object
def convert():
    kg_to_ounces()
    kg_to_pounds()
    kg_to_grams()

b1=Button(window, text="Convert", command=convert)
b1.grid(row=1, column=0) #position object

e2=Label(window, text="Kg")
e2.grid(row=0, column=0)

e1_value=StringVar()
e1=Entry(window, textvariable=e1_value)
e1.grid(row=0, column=1)

t1=Text(window, height=1, width=20)
t1.grid(row=1, column=1)

t2=Text(window, height=1, width=20)
t2.grid(row=1, column=2)

t3=Text(window, height=1, width=20)
t3.grid(row=1, column=3)

window.mainloop()
