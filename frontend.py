# Este script es la interfaz gráfica de usuario (GUI) para una aplicación de gestión de libros.
# Utiliza la biblioteca tkinter para crear la GUI y el módulo backend.py para manejar la lógica de la base de datos.
# La aplicación permite al usuario agregar, buscar, actualizar y eliminar libros de una base de datos SQLite.
# La GUI incluye etiquetas, entradas de texto, una lista para mostrar los libros y botones para realizar las operaciones.

from tkinter import *
import backend

# Para crear el ejecutable con PyInstaller, usé el comando --> pyinstaller --onefile --windowed frontend.py"
# Hay que tener instalado pyinstaller, se instala con --> pip install pyinstaller


# --- Funciones para los botones de la interfaz ---
# Estas funciones llaman a las funciones de backend.py para realizar las operaciones de la base de datos 
# Por ejemplo, la función view_command() llama a la función view() de backend.py para mostrar todos los registros de la base de datos

def view_command():
    list1.delete(0, END)
    for row in backend.view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in backend.search(title_text.get(), author_text.get(), year_text.get(), isbn_text.get()):
        list1.insert(END, row)

def add_command():
    backend.insert(title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(), year_text.get(), isbn_text.get()))

def delete_command():
    backend.delete(selected_tuple[0])
    view_command()

def update_command():
    backend.update(selected_tuple[0], title_text.get(), author_text.get(), year_text.get(), isbn_text.get())
    view_command()

def get_selected_row(event): # Esta función se llama cuando se selecciona una fila en el Listbox
    try:
        global selected_tuple # Se declara como global para poder usarla en otras funciones
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass  # No hay nada seleccionado o es una línea vacía


# --- Ventana ---
window = Tk()
window.title("Book Manager")  # Nombre de la ventana
window.geometry("390x210")    # Tamaño de la ventana

# --- Etiquetas de la parte superior ---
l1 = Label(window, text="Title")
l1.grid(row=0, column=0)

l2 = Label(window, text="Author")
l2.grid(row=0, column=2)

l3 = Label(window, text="Year")
l3.grid(row=1, column=0)

l4 = Label(window, text="ISBN")
l4.grid(row=1, column=2)

# --- Entradas ---
title_text = StringVar()
e1 = Entry(window, textvariable=title_text)
e1.grid(row=0, column=1)

author_text = StringVar()
e2 = Entry(window, textvariable=author_text)
e2.grid(row=0, column=3)

year_text = StringVar()
e3 = Entry(window, textvariable=year_text)
e3.grid(row=1, column=1)

isbn_text = StringVar()
e4 = Entry(window, textvariable=isbn_text)
e4.grid(row=1, column=3)


# --- Caja de texto y Scrollbar ---
list1=Listbox(window, height=6, width=35)
list1.grid(row=2, column=0, rowspan=6, columnspan=2)

sb1=Scrollbar(window)
sb1.grid(row=2, column=2, rowspan=6) # Posición del scrollbar

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)


# --- Vincula selección del Listbox ---
list1.bind('<<ListboxSelect>>', get_selected_row)


# --- Botones ---
b1=Button(window, text="View all", width=12, command=view_command)
b1.grid(row=2, column=3)

b2=Button(window, text="Search entry", width=12, command=search_command)
b2.grid(row=3, column=3)

b3=Button(window, text="Add entry", width=12, command=add_command)
b3.grid(row=4, column=3)

b4=Button(window, text="Update", width=12, command=update_command)
b4.grid(row=5, column=3)

b5=Button(window, text="Delete", width=12, command=delete_command)
b5.grid(row=6, column=3)

b6=Button(window, text="Close", width=12, command=window.destroy)
b6.grid(row=7, column=3)

window.mainloop()
