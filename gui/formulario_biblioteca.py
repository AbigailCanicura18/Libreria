import tkinter as tk
from models.biblioteca_modelo import agregar_biblioteca
from tkinter import messagebox
from gui.formulario_libro import crear_libro

def crear_biblioteca(interfaz):
    interfaz.title("Formulario biblioteca")
    tk.Label(interfaz,text="Id biblioteca:").grid(row=0, column=0, sticky="e")
    input_id = tk.Entry(interfaz)
    input_id.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(interfaz,text="Nombre:").grid(row=1, column=0, sticky="e")
    input_nombre = tk.Entry(interfaz)
    input_nombre.grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(interfaz,text="Ubicación:").grid(row=2, column=0, sticky="e")
    input_ubicacion = tk.Entry(interfaz)
    input_ubicacion.grid(row=2, column=1, padx=5, pady=5)

    def agregar():
        try:
            id_biblioteca = input_id.get()
            nombre_biblioteca = input_nombre.get()
            ubicacion_biblioteca = input_ubicacion.get()
            if not (id_biblioteca and nombre_biblioteca and ubicacion_biblioteca):
                messagebox.showwarning("Advertencia", "Debes rellenar los campos!")
                return
            agregar_biblioteca(id_biblioteca, nombre_biblioteca, ubicacion_biblioteca)
            messagebox.showinfo("Mensaje","Biblioteca agregada con éxito!")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    tk.Button(interfaz, text="Registrar", command=agregar ).grid(row=3, column=1, padx=5, pady=5)
    
    tk.Button(interfaz, text="Agregar libro", command=crear_libro).grid(row=4, column=1, padx=5, pady=5)