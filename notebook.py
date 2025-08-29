# importacion de la libreria
import tkinter as tk
from tkinter import ttk, messagebox

# crear ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("libro de pacientes y doctores")
ventana_principal.geometry("400x600")

# crear contenedor notebook (pestañas)
pestañas = ttk.Notebook(ventana_principal)

# crear frames(uno por pestaña)
frame_pacientes = ttk.Frame(pestañas)

# agregar pestañas al notebook
pestañas.add(frame_pacientes,text = "pacientes")

# mostrar las pestañas en la ventana
pestañas.pack(expand = True, fill= "both")

# Crear frame doctores
frame_doctores = ttk.Frame(pestañas)

# agregar pestaña doctor
pestañas.add(frame_doctores, text = "doctores")

# nombre
labelNombre=tk.Label(frame_pacientes,text="Nombre completo:")
labelNombre.grid(row=0, column=0, sticky="w", padx=5, pady=5)

nombreP=tk.Entry(frame_pacientes)
nombreP.grid(row=0, column=1, sticky="w", padx=5, pady=5)

# Fecha de nacimiento
labelFechaN= tk.Label(frame_pacientes,text="Fecha de nacimiento")
labelFechaN.grid(row=1, column=0, sticky="w", padx=5, pady=5)

fechaN=tk.Entry(frame_pacientes)
fechaN.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# edad 
labelEdad=tk.Label(frame_pacientes, text = "Edad")
labelEdad.grid(row=2, column=0, sticky="w", padx=5, pady=5)

edadP = tk.Entry(frame_doctores, state="readonly")
edadP.grid(row=2, column=1, sticky="w", padx=5, pady=5)

genero=tk.StringVar()
genero.set("masculino")  #valor por defecto)

radioMasculino=ttk.Radiobutton(frame_pacientes,text = "masculino", variable = genero, value = "masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)

radioFemenino=ttk.Radiobutton(frame_pacientes, text = "femenino", variable = genero, value = "femenino")
radioFemenino.grid(row=2, column=1, sticky="w", padx=5, )

#grupo sanguineo
labelGrupoSanguineo = tk.Label(frame_pacientes,text="grupo sanguineo:")
labelGrupoSanguineo.grid(row=4, column = 0, sticky = "w", padx = 5, pady = 5)

entryGrupoSanguineo = tk.Entry(frame_pacientes, text = "grupo sanguineo")
entryGrupoSanguineo.grid(row = 4, column = 1, sticky = "w", padx = 5, pady = 5)

#tipo de seguro
labelTipoSeguro=tk.Label(frame_pacientes,text = "tipo de seguro")
labelTipoSeguro.grid(row=5, column = 0, sticky = "w", padx = 5, pady = 5)

tipo_seguro=tk.StringVar()
tipo_seguro.set("publico") #valor por defecto

comboTipoSeguro=ttk.Combobox(frame_pacientes, values = ["publico","privado","ninguno"], textvariable = tipo_seguro)
comboTipoSeguro.grid(row=5, column=1, sticky="w", padx=5, pady=5)

#centro medico
labelCentroMedico=tk.Label(frame_pacientes,text = "centro de salud:")
labelCentroMedico.grid(row = 6, column = 0, sticky = "w", padx = 5, pady = 5)

centro_medico=tk.StringVar()
centro_medico.set("hospital central")   #valor por defecto

comboCentroMedico=ttk.Combobox(frame_pacientes, values = ["hospital central", "clinica norte", "centro sur"], textvariable = centro_medico)
comboCentroMedico.grid(row = 6, column = 1, sticky = "w", padx = 5, pady = 5)

ventana_principal.mainloop()