import tkinter as tk
from tkinter import *

root = tk.Tk()
root.geometry("300x300")

lista = []

listaTk = tk.Listbox(root, width=40)
listaTk.pack()

def cargarLista():
    with open("data.txt") as f:
        linea = f.readlines()
    for i in linea:
        lista.append(i.rstrip())
        listaTk.insert(END, i)
    f.close()

def agregar():
    lista.append(texto.get())
    listaTk.insert(END, txt.get())

def modificar():
    for item in listaTk.curselection():
        eliminar = str(listaTk.get(listaTk.curselection()))
        listaTk.delete(item)
        listaTk.insert(END, txt.get())
        for i in lista:
            if i == eliminar.rstrip():
                lista.remove(i)
        lista.append(texto.get())

def borrar():
    for item in listaTk.curselection():
        eliminar = str(listaTk.get(listaTk.curselection()))
        listaTk.delete(item)
        for i in lista:
            if i == eliminar.rstrip():
                lista.remove(i)

def listar():
    with open("data.txt", "w") as f:
        for s in lista:
            f.write(str(s)+"\n")
    f.close()

cargarLista()

txt = StringVar()
texto = tk.Entry(root, textvariable=txt, width=40)
texto.pack()

botonAnadir = tk.Button(root, height=1, width=17, text="Anadir", command=agregar)
botonAnadir.pack()

botonModificar = tk.Button(root, height=1, width=17, text="Modificar", command=modificar)
botonModificar.pack()

botonEliminar = tk.Button(root, height=1, width=17, text="Eliminar", command=borrar)
botonEliminar.pack()

botonListar = tk.Button(root, height=1, width=17, text="Listar", command=listar)
botonListar.pack()

root.mainloop()