import tkinter as tk
from tkinter import messagebox, ttk
import random
from models.juego_modelo import agregar_resultado, obtener_resultados, borrar_resultados

def principal_juego(ventana):
    # Título
    ventana.title("Cachipun")
    titulo = tk.Label(ventana, text="Juego Piedra, Papel o Tijera")
    titulo.grid(row=0, column=0, columnspan=3, pady=10)

    # Entry para nombre
    tk.Label(ventana,text="Ingrese su nombre:").grid(row=1,column=0, sticky="e")
    input_nombre = tk.Entry(ventana)
    input_nombre.grid(row=1, column=1, columnspan=2, pady=5)

    # Cargar imágenes y guardar referencia en ventana
    ventana.imagen_piedra = tk.PhotoImage(file="assets/img/piedra.png")
    ventana.imagen_papel = tk.PhotoImage(file="assets/img/papel.png")
    ventana.imagen_tijera = tk.PhotoImage(file="assets/img/tijera.png")

    # Botones con imágenes y métodos para jugar:
    def calcular_resultado(eleccion_jugador, eleccion_computador):
        if eleccion_jugador == eleccion_computador:
            return "Empate"
        elif (eleccion_jugador=="piedra" and eleccion_computador=="tijera") or (eleccion_jugador=="papel" and eleccion_computador=="piedra") or (eleccion_jugador=="tijera" and eleccion_computador=="papel"):
            return "Ganaste"
        else:
            return "Perdiste"

    def jugar(eleccion_jugador):
        try:
            nombre = input_nombre.get().title()
            if not nombre:
                messagebox.showwarning("Warning","Debe ingresar nombre jugador")
                return
            eleccion_computador = random.choice(["piedra","papel","tijera"])
            resultado = calcular_resultado(eleccion_jugador,eleccion_computador)
            messagebox.showinfo("Resultado",resultado)
            agregar_resultado(nombre,eleccion_jugador,eleccion_computador,resultado)
            cargar_resultados()
            input_nombre.delete(0,tk.END)
        except Exception as ex:
            print("Error:",ex)

    boton_piedra = tk.Button(ventana, text="Piedra", image=ventana.imagen_piedra, command=lambda: jugar("piedra"),background="gray")
    boton_piedra.grid(row=2, column=0, padx=10, pady=10)

    boton_papel = tk.Button(ventana, text="Papel", image=ventana.imagen_papel, command=lambda: jugar("papel"), background="black")
    boton_papel.grid(row=2, column=1, padx=10, pady=10)

    boton_tijera = tk.Button(ventana, text="Tijera", image=ventana.imagen_tijera, command=lambda: jugar("tijera"), background="pink")
    boton_tijera.grid(row=2, column=2, padx=10, pady=10)

    # Vamos a mostrar una tablita:
    tk.Label(ventana,text="Listado resultados").grid(row=3,column=0, columnspan=3)
    tabla = ttk.Treeview(ventana,columns=("Nombre","Jugador","Computador","Resultado"),show="headings")
    tabla.heading("Nombre",text="Nombre")
    tabla.heading("Jugador",text="Jugador")
    tabla.heading("Computador",text="Computador")
    tabla.heading("Resultado",text="Resultado")
    tabla.grid(row=4,column=0, columnspan=3, padx=10, pady=5)

    def cargar_resultados():
        try:
            resultados = obtener_resultados()
            filas = tabla.get_children()
            for f in filas:
                tabla.delete(f)
            for r in resultados:
                tabla.insert("","end", values=r)
        except Exception as ex:
            messagebox.showerror("Error",f"No se pudieron cargar los resultados: {ex}")
    cargar_resultados()
    
    def borrar():
        borrar_resultados()
        cargar_resultados()
    boton_borrar = tk.Button(ventana, text="Borrar resultados", command=borrar)
    boton_borrar.grid(row=5, column=0, columnspan=3)