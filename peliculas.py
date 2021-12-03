# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 21:22:16 2021

@author: USUARIO
"""

from tkinter import*
from tkinter import scrolledtext

peliculas=Tk()
peliculas.title("Peliculas")
peliculas.geometry("750x750")

#Labels
lblIdPelicula=Label(peliculas,text="Id Pelicula: ")
lblIdPelicula.grid(row=0,column=0)
lblIdPelicula.config(padx=40,pady=30,font=('Arial',18))

lblNombrePeli=Label(peliculas,text="Nombre Pelicula: ")
lblNombrePeli.grid(row=1,column=0)
lblNombrePeli.config(padx=40,pady=30,font=('Arial',18))

lblDuracion=Label(peliculas,text="Duración: ")
lblDuracion.grid(row=2,column=0)
lblDuracion.config(padx=40,pady=30,font=('Arial',18))

lblGenero=Label(peliculas,text="Género: ")
lblGenero.grid(row=3,column=0)
lblGenero.config(padx=40,pady=30,font=('Arial',18))

lblIdioma=Label(peliculas,text="Idioma: ")
lblIdioma.grid(row=4,column=0)
lblIdioma.config(padx=40,pady=30,font=('Arial',18))

lblSinopsis=Label(peliculas,text="Sinopsis: ")
lblSinopsis.grid(row=5,column=0)
lblSinopsis.config(padx=40,pady=80,font=('Arial',18))

#TextBox
idpeli=StringVar()
txtIdPelicula=Entry(peliculas,width=25,textvariable=idpeli)
txtIdPelicula.grid(row=0,column=1)
txtIdPelicula.config(font=('Arial',18))

nompeli=StringVar()
txtNombrePeli=Entry(peliculas,width=25,textvariable=nompeli)
txtNombrePeli.grid(row=1,column=1)
txtNombrePeli.config(font=('Arial',18))

durac=StringVar()
txtDuracion=Entry(peliculas,width=25,textvariable=durac)
txtDuracion.grid(row=2,column=1)
txtDuracion.config(font=('Arial',18))

gener=StringVar()
txtGenero=Entry(peliculas,width=25,textvariable=gener)
txtGenero.grid(row=3,column=1)
txtGenero.config(font=('Arial',18))

idiom=StringVar()
txtIdioma=Entry(peliculas,width=25,textvariable=idiom)
txtIdioma.grid(row=4,column=1)
txtIdioma.config(font=('Arial',18))

#Sinopsis:
#Caja de texto con varias líneas
scrol_ancho=25
scrol_alto=5
sinopsis=scrolledtext.ScrolledText(peliculas,width=scrol_ancho,height=scrol_alto,wrap=WORD)
sinopsis.grid(row=5,column=1,columnspan=3)
sinopsis.config(font=('Arial',18))

#Button
btnRegistrar=Button(peliculas,text="Registrar")
btnRegistrar.grid(row=6,column=1)
btnRegistrar.config(font=('Arial',18))




peliculas.mainloop()
