# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:53:50 2021

@author: USUARIO
"""

from tkinter import*
from tkinter import ttk

salas=Tk()
salas.title("Salas")
salas.geometry("650x550")

#Labels
lblNumSala=Label(salas,text="Número Sala: ")
lblNumSala.grid(row=0,column=0)
lblNumSala.config(padx=40,pady=40,font=('Arial',18))

lblNumAsiento=Label(salas,text="Núm. Asiento: ")
lblNumAsiento.grid(row=1,column=0)
lblNumAsiento.config(padx=40,pady=40,font=('Arial',18))

lblTipoSala=Label(salas,text="Tipo Sala: ")
lblTipoSala.grid(row=2,column=0)
lblTipoSala.config(padx=40,pady=40,font=('Arial',18))

lblDisponibilidad=Label(salas,text="Disponibilidad: ")
lblDisponibilidad.grid(row=3,column=0)
lblDisponibilidad.config(padx=40,pady=40,font=('Arial',18))

#Textbox
numsala=StringVar()
txtNumSala=Entry(salas,width=25,textvariable=numsala)
txtNumSala.grid(row=0,column=1)
txtNumSala.config(font=('Arial',18))

numasi=IntVar()
txtNumAsiento=Entry(salas,width=25,textvariable=numasi)
txtNumAsiento.grid(row=1,column=1)
txtNumAsiento.config(font=('Arial',18))

#Combobox
tipsala=StringVar()
cbbxTipoSala=ttk.Combobox(salas,width=23,textvariable=tipsala)
#Llenar la lista desplegable
cbbxTipoSala['values']=("2D","3D")
cbbxTipoSala.grid(row=2,column=1)
cbbxTipoSala.config(font=('Arial',18))

dispo=StringVar()
cbbxDisponibilidad=ttk.Combobox(salas,width=23,textvariable=dispo)
#Llenar la lista desplegable
cbbxDisponibilidad['values']=("Disponible","NO Disponible")
cbbxDisponibilidad.grid(row=3,column=1)
cbbxDisponibilidad.config(font=('Arial',18))

#Button
btnAceptar=Button(salas,text="Aceptar")
btnAceptar.grid(row=4,column=1)
btnAceptar.config(font=('Arial',18))







salas.mainloop()
