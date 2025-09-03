# importacion de la libreria
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

#funcion para enmascarar fecha
def enmascarar_fecha(texto):
    limpio= ''.join(filter(str.isdigit,texto))
    formato_final=""
    if len(limpio)>8:
        limpio=limpio[:8]
    if len(limpio)>4:
        formato_final=f"{limpio[:2]}-{limpio[2:4]}-{limpio[4:]}"
    elif len(limpio)>2:
        formato_final= f"{limpio[:2]}-{limpio[2:]}"
    else: 
        formato_final= limpio
    if fechaN.get() !=formato_final:
        fechaN.delete(0,tk.END)
        fechaN.insert(0,formato_final)
    if len(fechaN.get())==10:
        fecha_actual=datetime.now().date()
        fecha_nacimiento=datetime.striptime(fechaN.get(),"%d-%m-%Y").date()
        edad=fecha_actual.year-fecha_nacimiento
        edadVar.set(edad)
    else:
        edadVar.set("")
    return True
        

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

validacion_fecha=ventana_principal.register(enmascarar_fecha)
fechaN=ttk.Entry(frame_pacientes,validate="key", validatecommand=(validacion_fecha,'%P'))
fechaN.grid(row=1, column=1, sticky="w", padx=5, pady=5)

# edad 
labelEdad=tk.Label(frame_pacientes, text = "Edad")
labelEdad.grid(row=2, column=0, sticky="w", padx=5, pady=5)

edadVar=tk.StringVar()
edadP=tk.Entry(frame_pacientes,textvariable=edadVar)
edadP.grid(row=2, column=1, sticky="w", padx=5, pady=5)


genero=tk.StringVar()
genero.set("masculino")  #valor por defecto)

labelgenero= tk.Label(frame_pacientes,text="Genero")
labelgenero.grid(row=3, column=0, sticky="w", padx=5, pady=5)

radioMasculino=ttk.Radiobutton(frame_pacientes,text = "masculino", variable = genero, value = "masculino")
radioMasculino.grid(row=3, column=1, sticky="w", padx=5)

radioFemenino=ttk.Radiobutton(frame_pacientes, text = "femenino", variable = genero, value = "femenino")
radioFemenino.grid(row=3, column=2, sticky="w", padx=5, )

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

#frame para los botones
btn_frame=tk.Frame(frame_pacientes)
btn_frame.grid(row=9,column=0,columnspan=2,pady=5,sticky="w")

#Boton registrar
btn_registrar=tk.Button(btn_frame,text="registrar",command="",bg="light blue")
btn_registrar.grid(row=0,column=0,padx=5)

#boton eliminar
btn_eliminar=tk.Button(btn_frame,text="eliminar",command="",bg="red")
btn_eliminar.grid(row=0,column=1,padx=5)

#crear treeview para mostrar pacientes
treeview=ttk.Treeview(frame_pacientes,columns=("nombre","fechaN","edad","genero","grupoS","tipoS","centroM"),show="headings")

#definir encabezados 
treeview.heading("nombre",text="nombre completo")
treeview.heading("fechaN",text="fecha de nacimiento")
treeview.heading("edad",text="edad")
treeview.heading("genero",text="genero")
treeview.heading("grupoS",text="grupo sanguineo")
treeview.heading("tipoS",text="tipo seguro")
treeview.heading("centroM",text="centro medico")

#definir ancho de columnas
treeview.column("nombre",width=120)
treeview.column("fechaN",width=120)
treeview.column("edad",width=50,anchor="center")
treeview.column("genero",width=60,anchor="center")
treeview.column("grupoS",width=100,anchor="center")
treeview.column("tipoS",width=100,anchor="center")
treeview.column("centroM",width=120)

#ubicar el treeview en la cuadricula
treeview.grid(row=7,column=0,columnspan=2,sticky="nsew",padx=5,pady=10)

#scrollbar vertical
scroll_y=ttk.Scrollbar(frame_pacientes,orient="vertical",command=treeview.yview)
treeview.configure(yscrollcommand=scroll_y.set)
scroll_y.grid(row=7,column=2,sticky="ns")

#Nombre doctores
labelNombreD=tk.Label(frame_doctores,text="Nombr completo:")
labelNombreD.grid(row=0,column=0,padx=5,pady=5,sticky="w")

nombrePd=tk.Entry(frame_doctores)
nombrePd.grid(row=0,column=1,padx=5,pady=5,sticky="w")

#especialidad
labelEspecialidad=tk.Label(frame_doctores,text="Especialidad:")
labelEspecialidad.grid(row=2,column=0,padx=5,pady=5,sticky="w")

especialidad=tk.StringVar()
especialidad.set("traumatologo") #valor por defecto

comboEspecialidad=ttk.Combobox(frame_doctores, values = ["traumatologo","pediatra","neurologo","cardiologo","ninguna"], textvariable = especialidad)
comboEspecialidad.grid(row=2, column=1, sticky="w", padx=5, pady=5)

#edad
labelEdadD=tk.Label(frame_doctores, text = "Edad:")
labelEdadD.grid(row=3, column=0, sticky="w", padx=5, pady=5)

spinEdad=tk.Spinbox(frame_doctores,from_=1,to=100)
spinEdad.grid(row=3, column=1, sticky="w", padx=5, pady=5)

#telefono
labelTelefono=tk.Label(frame_doctores, text = "Telfono:")
labelTelefono.grid(row=4, column=0, sticky="w", padx=5, pady=5)

Telefonopf=tk.Entry(frame_doctores)
Telefonopf.grid(row=4,column=1,padx=5,pady=5,sticky="w")

#frame para los botones
btn_frame=tk.Frame(frame_doctores)
btn_frame.grid(row=9,column=0,columnspan=2,pady=5,sticky="w")

#Boton registrar
btn_registrar=tk.Button(btn_frame,text="registrar",command="",bg="light blue")
btn_registrar.grid(row=0,column=1,padx=5)

#boton eliminar
btn_eliminar=tk.Button(btn_frame,text="eliminar",command="",bg="red")
btn_eliminar.grid(row=0,column=2,padx=5)

#crear treeview para mostrar pacientes
treeview2=ttk.Treeview(frame_doctores,columns=("nombre","fecha","edad","genero","especialidad","centroM"),show="headings")

#definir encabezados 
treeview2.heading("nombre",text="nombre completo")
treeview2.heading("fecha",text="fecha de nacimiento")
treeview2.heading("edad",text="edad")
treeview2.heading("genero",text="genero")
treeview2.heading("especialidad",text="especialidad")
treeview2.heading("centroM",text="centroM")

#definir ancho de columnas
treeview2.column("nombre",width=120)
treeview2.column("fecha",width=120)
treeview2.column("edad",width=50,anchor="center")
treeview2.column("genero",width=60,anchor="center")
treeview2.column("especialidad",width=100,anchor="center")
treeview2.column("centroM",width=120)

#no ha funcionao

ventana_principal.mainloop()