import tkinter as tk
from tkinter import messagebox

ventana=tk.Tk()
labelEdad=tk.Label(ventana,text="edad")
labelEdad.grid(row=0,column=0,padx=5,pady=5,sticky="w")

spin=tk.Spinbox(ventana,from_=1,to=10)
spin.grid(row=0,column=1,padx=10,pady=10)

def mostrarEdad():
    tk.messagebox.showinfo("edad",f"la edad seleccionada es {spin.get()}")

boton=tk.Button(ventana,text="obtener valor",command= mostrarEdad)
boton.grid(row=1,column=0,padx=10,pady=10)

labelGenero=tk.Label(ventana,text="genero")
labelGenero.grid(row=1,column=1,padx=5,pady=5,sticky="w")

#spinbox de texto para genero 

genero=tk.Spinbox(ventana,values=("masculino","femenino","otro"))
genero.grid(row=2,column=0,padx=10,pady=10)

def mostrarGenero():
    tk.messagebox.showinfo("genero",f"el genero seleccionado es {genero.get()}")

botonGenero=tk.Button(ventana,text="obtener genero",command= mostrarGenero)
botonGenero.grid(row=3,column=1,padx=10,pady=10,sticky="w")


ventana.mainloop()