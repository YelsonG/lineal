import tkinter as tk

def busqueda_lineal(lista, elemento_buscado):
    
   
for i in range(len(lista)):
        
       
if lista[i] == elemento_buscado:
            
           
return i  # Se encontró el elemento en el índice i

    return -1  # Elemento no encontrado

def buscar_elemento():
    lista = [int(x) for x in entrada_lista.get().split(",")]
    elemento = int(entrada_elemento.get())

    indice_encontrado = busqueda_lineal(lista, elemento)
    

    indice_encontrado = busqueda_lineal(lista, elemento


    indice
if indice_encontrado != -1:
        resultado.config(text=
        resultado.config(text=f
f"El elemento {elemento} se encuentra en el índice {indice_encontrado}.")
    else:
        resultado.config(text=f"El elemento {elemento} no está presente en la lista.")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title(
ventana = tk.Tk()
ventana.title

ventana = tk.Tk()
ventana

ventana = tk.Tk

vent
"Búsqueda Lineal")
ventana.geometry("400x200")

# Etiquetas y campos de entrada
etiqueta_lista = tk.Label(ventana, text=
etiqueta_lista = tk.Label(vent

et
"Ingrese la lista separada por comas:")
etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista.pack()

etiqueta_elemento = tk.Label(ventana, text=
etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista.pack()

etiqueta_elemento = tk.Label(

etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana)
entrada_lista.pack()

etiqueta

etiqueta_lista.pack()

entrada_lista = tk.Entry(ventana

etiqueta_lista.pack()

entrada_lista = tk

etiqueta_lista.pack()


etiqueta_lista.pack
"Ingrese el elemento a buscar:")
etiqueta_elemento.pack()

entrada_elemento = tk.Entry(ventana)
entrada_elemento.pack()


etiqueta_elemento.pack()

entrada_elemento = tk.Entry(ventana)
entrada

etiqueta_elemento.pack()

entrada_elemento = tk.Entry(ventana)

etiqueta_elemento.pack()

entrada

etiqueta_elemento.pack()


etiqueta_elemento
# Botón para realizar la búsqueda
boton_buscar = tk.Button(ventana, text=
boton_buscar = tk.Button(vent

boton_buscar = tk.Button

bot
"Buscar", command=buscar_elemento)
boton_buscar.pack()


boton_buscar

bot
# Etiqueta para mostrar el resultado
resultado = tk.Label(ventana, text=
resultado = tk.Label(vent

resultado = tk.Label(

resultado
"")
resultado.pack()

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()

ventana.mainloop()
``

ventana.mainloop()
