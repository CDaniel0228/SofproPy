from tkinter import *
import traceback

def panelCaracteristicas(self):
    for widget in self.winfo_children():
       widget.destroy()
    frame2 = Frame(self)
    frame2.pack(expand=True, fill=BOTH,side="left") #Configurar el metodo pack()
    #frame2.config(bg="yellow")
    btnNuevo=Button(frame2,text="Caracteristicas", bg="blue", fg="white")
    btnNuevo.place(x=5,y=50,width=80, height=30 )
    