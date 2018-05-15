from tkinter import*
import random
import time;
import dateline


root= TK()

root.gemometry("1350X750+0+0")
root.title("SISTEMA DE VENDAS")
root.configure(backgrounds= 'blue')

Tops = Frame (root, width=1350 , height=100 , bd=9, relief ="raise")
Tops.pack(side=TOP)

fleftl = Frame (root, width=900 , height=650, bd=8, relief ="raise")
fleft.pack(side=LEFT)

fright = Frame (root, width=440 , heidth=650 , bd=8 , relief ="raise")
fright.pack(side=RIGHT)

root.mailoop()
