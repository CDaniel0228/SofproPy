from ctypes import alignment
from tkinter import *
from Home import *


def main():
    root = Tk()
    root.title("Inicio")
    root.resizable(0,0)
    ancho_ventana = 800
    alto_ventana = 500
    x_ventana = root.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = root.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    root.geometry(posicion)
    app = Home(root) 
    app.mainloop()



if __name__ == "__main__":
    main()
    