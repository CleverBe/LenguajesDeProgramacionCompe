# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:53:50 2021

@author: USUARIO
"""

from tkinter import*


salas=Tk()
salas.title("Salas")
salas.geometry("650x550")

#Labels
lblIdSala=Label(salas,text="Id Sala: ")
lblIdSala.grid(row=0,column=0)
lblIdSala.config(padx=40,pady=40,font=('Arial',18))

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
idsala=StringVar()
txtIdSala=Entry(salas,width=25,textvariable=idsala)
txtIdSala.grid(row=0,column=1)
txtIdSala.config(font=('Arial',18))

numasi=IntVar()
txtNumAsiento=Entry(salas,width=25,textvariable=numasi)
txtNumAsiento.grid(row=1,column=1)
txtNumAsiento.config(font=('Arial',18))

tipsala=StringVar()
txtTipoSala=Entry(salas,width=25,textvariable=tipsala)
txtTipoSala.grid(row=2,column=1)
txtTipoSala.config(font=('Arial',18))

dispo=StringVar()
txtDisponibilidad=Entry(salas,width=25,textvariable=dispo)
txtDisponibilidad.grid(row=3,column=1)
txtDisponibilidad.config(font=('Arial',18))

#Button
btnAceptar=Button(salas,text="Aceptar")
btnAceptar.grid(row=4,column=1)
btnAceptar.config(font=('Arial',18))







salas.mainloop()
