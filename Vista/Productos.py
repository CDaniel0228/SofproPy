from tkinter import *
from tkinter import messagebox
from Caracteristicas import *

def panelProducto(self):
    for widget in self.winfo_children():
       widget.destroy()
    frame = Frame(self)
    frame.pack(expand=True, fill=BOTH,side="left") #Configurar el metodo pack()
    #frame2.config(bg="yellow")
    btnNuevo=Button(frame,text="Producto", bg="blue", fg="white", command=saludar)
    btnNuevo.place(x=5,y=50,width=80, height=30 ) 

def saludar():
    messagebox.showinfo(message="hola",title="dos")