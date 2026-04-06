import tkinter as tk

contador = 0

def sumar():
    global contador
    contador += 1
    etiqueta.config(text="Contador: " + str(contador))

def reiniciar():
    global contador
    contador = 0
    etiqueta.config(text="Contador: 0")

ventana = tk.Tk()
ventana.title("Contador")

etiqueta = tk.Label(ventana, text="Contador: 0", font=("Arial", 16))
etiqueta.pack()

boton_sumar = tk.Button(ventana, text="Sumar", command=sumar)
boton_sumar.pack()

boton_reset = tk.Button(ventana, text="Reiniciar", command=reiniciar)
boton_reset.pack()

ventana.mainloop()