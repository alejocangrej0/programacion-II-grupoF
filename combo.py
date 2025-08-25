import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
#crear una ventana principal
ventana =tk.Tk()
ventana.title("Ejemplo Combobox")
ventana.geometry("300x200")
#etiqueta
etiqueta= tk.Label(ventana, text="selecciones especialidad")
etiqueta.grid(row=0, column=1, padx=10, pady=10)
#crear combobox
opciones=["cardiologia","neurologia","pediatria","dermatologia"]
combo=ttk.Combobox(ventana, values=opciones, state="readonly")
combo.current(0)      #seleccionar primera opcion por defecto
combo.grid(row=0,column=1,padx=10,pady=10)
#funciones para demostar la seleccion
def mostrar():
    seleccion=combo.get()
    tk.messagebox.showinfo("seleccion",f"has elegido:{seleccion}")
#boton para comfirmar seleccion
boton=tk.Button(ventana,text="aceptar",command=mostrar)
boton.grid(row=1,column=0,columnspan=2,pady=15)
ventana.mainloop()