# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 20:30:30 2021

@author: USUARIO
"""

from tkinter import*


login=Tk()
login.title("Login")
login.geometry("600x280")

#Labels
lblUsuario=Label(login,text="Usuario: ")
lblUsuario.grid(row=0,column=0)
lblUsuario.config(padx=40,pady=30,font=('Arial',18))

lblContrasena=Label(login,text="Contraseña: ")
lblContrasena.grid(row=1,column=0)
lblContrasena.config(padx=40,pady=30,font=('Arial',18))

#Cajas de texto
usu=StringVar()
txtUsuario=Entry(login,width=25,textvariable=usu)
txtUsuario.grid(row=0,column=1)
txtUsuario.config(font=('Arial',18))

contr=StringVar()
txtContrasena=Entry(login,width=25,textvariable=contr)
txtContrasena.grid(row=1,column=1)
txtContrasena.config(font=('Arial',18),show='*')

#Button
btnIngresar=Button(login,text="Ingresar")
btnIngresar.grid(row=2,column=1)
btnIngresar.config(font=('Arial',18))


login.mainloop()
