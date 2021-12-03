# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:22:16 2021

@author: USUARIO
"""

from tkinter import*
from tkinter import scrolledtext
from tkinter import ttk

peliculas=Tk()
peliculas.title("Peliculas")
peliculas.geometry("750x750")

#Labels

lblNombrePeli=Label(peliculas,text="Nombre Pelicula: ")
lblNombrePeli.grid(row=0,column=0)
lblNombrePeli.config(padx=40,pady=30,font=('Arial',18))

lblDuracion=Label(peliculas,text="Duración: ")
lblDuracion.grid(row=1,column=0)
lblDuracion.config(padx=40,pady=30,font=('Arial',18))

lblGenero=Label(peliculas,text="Género: ")
lblGenero.grid(row=2,column=0)
lblGenero.config(padx=40,pady=30,font=('Arial',18))

lblIdioma=Label(peliculas,text="Idioma: ")
lblIdioma.grid(row=3,column=0)
lblIdioma.config(padx=40,pady=30,font=('Arial',18))

lblSinopsis=Label(peliculas,text="Sinopsis: ")
lblSinopsis.grid(row=4,column=0)
lblSinopsis.config(padx=40,pady=80,font=('Arial',18))

#TextBox
nompeli=StringVar()
txtNombrePeli=Entry(peliculas,width=25,textvariable=nompeli)
txtNombrePeli.grid(row=0,column=1)
txtNombrePeli.config(font=('Arial',18))

durac=StringVar()
txtDuracion=Entry(peliculas,width=25,textvariable=durac)
txtDuracion.grid(row=1,column=1)
txtDuracion.config(font=('Arial',18))

genero=StringVar()
cbbxGenero=ttk.Combobox(peliculas,width=23,textvariable=genero)
#Llenar la lista desplegable
cbbxGenero['values']=("Terror","Comedia","Drama","Acción","Suspenso")
cbbxGenero.grid(row=2,column=1)
cbbxGenero.config(font=('Arial',18))

idiom=StringVar()
cbbxIdioma=ttk.Combobox(peliculas,width=23,textvariable=idiom)
#Llenar la lista desplegable
cbbxIdioma['values']=("Español","Inglés")
cbbxIdioma.grid(row=3,column=1)
cbbxIdioma.config(font=('Arial',18))


#Sinopsis:
#Caja de texto con varias líneas
scrol_ancho=25
scrol_alto=5
sinopsis=scrolledtext.ScrolledText(peliculas,width=scrol_ancho,height=scrol_alto,wrap=WORD)
sinopsis.grid(row=4,column=1,columnspan=3)
sinopsis.config(font=('Arial',18))

#Button
btnRegistrar=Button(peliculas,text="Registrar")
btnRegistrar.grid(row=6,column=1)
btnRegistrar.config(font=('Arial',18))




peliculas.mainloop()
