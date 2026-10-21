from tkinter import *

#Configuración de los colores para el sistema
CANELA = "#713F35"
TERRACOTA = "#A65D45"
DURAZNO = "#E8B99A"
CREMA = "#F8EBDD"
BLANCO = "#FFF9F2"
TEXTO = "#49312B"
BORDE = "#D3A18A"

#Ventana Principal
raiz = Tk()
raiz.title("John's Fresh - Inventario")
raiz.geometry("1100x650")
raiz.minsize(900, 550)
raiz.config(bg=CREMA)

#Icono de la ventana
raiz.iconbitmap("Logo_JF_pequenio.ico")

#Marco principal del sistema
miFrame = Frame(raiz, bg=CREMA)
miFrame.pack(fill="both", expand=True, padx=15, pady=15)

# Dos columnas, izquierda grande y derecha pequeña para separar las pestañas
miFrame.grid_columnconfigure(0, weight=7, uniform="columnas")
miFrame.grid_columnconfigure(1, weight=4, uniform="columnas")
miFrame.grid_rowconfigure(0, weight=1)

#Lado izquierdo, por ahora está vacío
panelIzquierdo = Frame(miFrame, bg=CREMA)

panelIzquierdo.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

#Lado derecho, datos de los productos
panelDerecho = Frame(miFrame, bg=DURAZNO, bd=0, padx=18, pady=18)

panelDerecho.grid(row=0, column=1, sticky="nsew")

panelDerecho.grid_columnconfigure(0, weight=1)

#Título del formulario
titulo = Label(panelDerecho, text="Datos del producto",
    font=("Segoe UI", 17, "bold"), fg=CANELA,bg=DURAZNO)

titulo.grid(row=0, column=0, sticky="w", pady=(0, 5))

subtitulo = Label(panelDerecho, text="Registro de inventario", font=("Segoe UI", 10),
    fg=TEXTO, bg=DURAZNO )

subtitulo.grid(row=1, column=0, sticky="w", pady=(0, 15))

#Función para crear las etiquetas y entradas
def crearCampo(fila, texto, solo_lectura=False):

    etiqueta = Label(panelDerecho, text=texto, font=("Segoe UI", 10, "bold"),
        fg=TEXTO, bg=DURAZNO)

    etiqueta.grid(row=fila, column=0, sticky="w", pady=(5, 3))

    cuadro = Entry(panelDerecho, font=("Segoe UI", 10), bg=BLANCO, fg=TEXTO,
        insertbackground=CANELA, relief="flat", bd=0)

    cuadro.grid(row=fila + 1, column=0, sticky="ew", ipady=7, pady=(0, 5))

    #El ID se reservará para asignarlo automáticamente
    if solo_lectura:
        cuadro.config(state="readonly")

    return cuadro


#Campos de los productos, donde se podrán escribir

cuadroID = crearCampo(2, "ID del producto", solo_lectura=True)

cuadroNombre = crearCampo(4, "Nombre del producto")

cuadroMarca = crearCampo(6, "Marca / proveedor")

cuadroCantidad = crearCampo(8, "Cantidad en existencia")

cuadroPrecio = crearCampo(10, "Precio por kilo ($ MXN)")

cuadroCategoria = crearCampo(12, "Categoría")

cuadroUnidad = crearCampo(14, "Unidad de medida/kg")

#Ejecuta el programa en un loop (repetición)
raiz.mainloop()
