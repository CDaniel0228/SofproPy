from functools import partial
from textwrap import fill
from tkinter import *
from turtle import left

from Productos import *
from Caracteristicas import *
from Calificar import *

class Home(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.Widgets()
        
    def Widgets(self):
        frame1 = Frame(self.parent)
        #frame1.place(x=0,y=0,width=100, height=500)
        frame1.pack(fill="y", side="left") #Configurar el metodo pack()
        frame1.config(bg="ivory3")
        frame1.config(width="150")
        frame2 = Frame(self.parent)
        frame2.pack(expand=True, fill=BOTH,side="left")
             
        btnNuevo=Button(frame1,text="Producto", bg="snow", fg="black", command=partial(panelProducto,frame2))
        btnNuevo.place(x=5,y=60,width=100, height=40 )
                
        btnModificar=Button(frame1,text="Caracteristicas", bg="snow", fg="black", command=partial(panelCaracteristicas,frame2))
        btnModificar.place(x=5,y=120,width=100, height=40, ) 
                      
        btnEliminar=Button(frame1,text="Calificar", bg="snow", fg="black", command=partial(panelCalificar,frame2))
        btnEliminar.place(x=5,y=180,width=100, height=40)  
        
        btnSalir=Button(frame1,text="Salir", bg="snow", fg="black", command=lambda:exit(self.destroy()))
        btnSalir.place(x=5,y=300,width=100, height=40) 
        
        panelProducto(frame2)
           