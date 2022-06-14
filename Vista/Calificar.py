from tkinter import *

def panelCalificar(self):
    for widget in self.winfo_children():
       widget.destroy()
    frame3 = Frame(self)
    frame3.pack(expand=True, fill=BOTH,side="left") #Configurar el metodo pack()
    #frame2.config(bg="yellow")
    btnNuevo=Button(frame3,text="Calificar", bg="blue", fg="white")
    btnNuevo.place(x=5,y=50,width=80, height=30 )