import tkinter as tk
from gui.formulario_biblioteca import crear_biblioteca

ventana = tk.Tk()
ventana.title("Formulario")

crear_biblioteca(ventana)

ventana.mainloop()