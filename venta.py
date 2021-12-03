# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:54:52 2021

@author: USUARIO
"""

from tkinter import*


ventas=Tk()
ventas.title("Ventas")
ventas.geometry("650x450")

#Labels
lblPelicula=Label(ventas,text="Pelicula: ")
lblPelicula.grid(row=0,column=0)
lblPelicula.config(padx=40,pady=30,font=('Arial',18))

lblHorario=Label(ventas,text="Horario: ")
lblHorario.grid(row=1,column=0)
lblHorario.config(padx=40,pady=30,font=('Arial',18))

lblCantBoletos=Label(ventas,text="Cant.Boletos: ")
lblCantBoletos.grid(row=2,column=0)
lblCantBoletos.config(padx=40,pady=30,font=('Arial',18))

lblTotal=Label(ventas,text="Total: ")
lblTotal.grid(row=3,column=0)
lblTotal.config(padx=40,pady=30,font=('Arial',18))

#Text Box
peli=StringVar()
txtPelicula=Entry(ventas,width=25,textvariable=peli)
txtPelicula.grid(row=0,column=1)
txtPelicula.config(font=('Arial',18))

hora=StringVar()
txtHorario=Entry(ventas,width=25,textvariable=hora)
txtHorario.grid(row=1,column=1)
txtHorario.config(font=('Arial',18))

cantbol=IntVar()
txtCantBoletos=Entry(ventas,width=25,textvariable=cantbol)
txtCantBoletos.grid(row=2,column=1)
txtCantBoletos.config(font=('Arial',18))

tot=IntVar()
txtTotal=Entry(ventas,width=25,textvariable=tot)
txtTotal.grid(row=3,column=1)
txtTotal.config(font=('Arial',18),state='disabled')

#Button
aceptar=Button(ventas,text="Aceptar")
aceptar.grid(row=4,column=1)
aceptar.config(font=('Arial',18))



ventas.mainloop()

