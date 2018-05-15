import tkinter
from time import strftime

def tic():
    rel['text'] = strftime('%H:%M:%S')

def tac():
    tic()
    rel.after(1000, tac)

rel = tkinter.Label()
rel['font'] = 'Arial 30'
rel.pack()
tac()
# para que funcione como um script, temos que chamar mainloop,
# senão o programa termina imediatamente após a chamada tac()
rel.mainloop()