import tkinter as tk

def crear_libro():
    ventana = tk.Toplevel()
    ventana.title("Formulario libros")

    tk.Label(ventana,text="Ingrese ISBN:").grid(row=0, column=0, sticky="e")
    input_isbn = tk.Entry(ventana)
    input_isbn.grid(row=0, column=1, padx=5, pady=5)
    
    tk.Label(ventana,text="Ingrese título:").grid(row=1, column=0, sticky="e")
    input_titulo = tk.Entry(ventana)
    input_titulo.grid(row=1, column=1, padx=5, pady=5)
    
    tk.Label(ventana,text="Ingrese autor:").grid(row=2, column=0, sticky="e")
    input_autor = tk.Entry(ventana)
    input_autor.grid(row=2, column=1, padx=5, pady=5)
    
    tk.Label(ventana,text="Ingrese año publicación:").grid(row=3, column=0, sticky="e")
    input_anio = tk.Entry(ventana)
    input_anio.grid(row=3, column=1, padx=5, pady=5)
    
    tk.Label(ventana,text="Seleccione Biblioteca:").grid(row=4, column=0, sticky="e")
    select_biblioteca = tk.StringVar(ventana)
    select_biblioteca.set("Seleccionar")

    try:
        from models.biblioteca_modelo import obtener_bibliotecas
        from tkinter import messagebox
        bibliotecas = obtener_bibliotecas()
        if not bibliotecas:
            raise ValueError("No se encontraron bibliotecas en la base de datos!")
        bibliotecas_dict = {nombre: id_biblioteca for id_biblioteca, nombre in bibliotecas}
    except Exception as ex:
        messagebox.showerror("Error","No se pudieron cargar las bibliotecas")
        ventana.destroy()
        return
    tk.OptionMenu(ventana, select_biblioteca, *bibliotecas_dict.keys() ).grid(row=4, column=1, padx=5, pady=5)

    def agregar():
        try:
            isbn = input_isbn.get()
            titulo = input_titulo.get()
            autor = input_autor.get()
            anio = int(input_anio.get())
            nombre_biblio = select_biblioteca.get()
            if not(isbn and titulo and autor and anio) or select_biblioteca=="Seleccionar":
                messagebox.showwarning("Warning","Debe ingresar valores")
                return
            from models.libro_modelo import agregar_libro
            agregar_libro(isbn,titulo,autor,anio, bibliotecas_dict[nombre_biblio] )
            messagebox.showinfo("Info","Libro agregado con éxito!")
        except Exception as ex:
            messagebox.showerror("Error",f"No se pudo registrar el libro: {ex}")

    tk.Button(ventana, text="Registrar", command=agregar).grid(row=5, column=1, padx=5, pady=5)