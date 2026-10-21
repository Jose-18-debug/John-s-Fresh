from tkinter import *
from tkinter import ttk     #Nos sirve para crear las pestañas de una mejor forma

# Configuración de los colores para el sistema
CANELA = "#713F35"
TERRACOTA = "#A65D45"
DURAZNO = "#E8B99A"
CREMA = "#F8EBDD"
BLANCO = "#FFF9F2"
TEXTO = "#49312B"
BORDE = "#D3A18A"

# Ventana principal
raiz = Tk()
raiz.title("John's Fresh - Inventario")
raiz.geometry("1100x650")
raiz.minsize(900, 550)
raiz.config(bg=CREMA)

# Icono de la ventana
raiz.iconbitmap("Logo_JF_pequenio.ico")

# Estilo de las pestañas
estilo = ttk.Style()
estilo.theme_use("default")

estilo.configure("JF.TNotebook", background=CREMA, borderwidth=0)

estilo.configure("JF.TNotebook.Tab", background=DURAZNO, foreground=CANELA,
    padding=(18, 10), font=("Segoe UI", 10, "bold"))

estilo.map("JF.TNotebook.Tab", background=[("selected", CANELA)],
           foreground=[("selected", BLANCO)])

#Contenedor principal de las pestañas
pestanas = ttk.Notebook(raiz, style="JF.TNotebook")
pestanas.pack(fill="both", expand=True, padx=15, pady=15)

#Pestaña de INICIO
pestanaInicio = Frame(pestanas, bg=CREMA)

pestanas.add(pestanaInicio, text="Inicio")

#Dos columnas, izquierda grande y derecha pequeña
pestanaInicio.grid_columnconfigure(0, weight=7, uniform="columnas")
pestanaInicio.grid_columnconfigure(1, weight=4, uniform="columnas")
pestanaInicio.grid_rowconfigure(0, weight=1)

#Lado izquierdo, imagen
panelIzquierdo = Frame(pestanaInicio, bg=CREMA)

panelIzquierdo.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

#Cargamos la imagen grande en png
try:
    logoPNG = PhotoImage(file="Logo_JF_grande.png")

    etiquetaLogo = Label(panelIzquierdo, image=logoPNG, bg=CREMA)

    #Centrar la imagen horizontal y verticalmente
    etiquetaLogo.place(relx=0.5, rely=0.5, anchor="center")

except TclError:
    Label(panelIzquierdo, text="Aquí aparecerá el logo de John's Fresh",
        font=("Segoe UI", 12), fg=TEXTO, bg=CREMA).place(relx=0.5, rely=0.5, anchor="center")

#Lado derecho, datos de los productos
panelDerecho = Frame(pestanaInicio, bg=DURAZNO, bd=0, padx=18, pady=18)

panelDerecho.grid(row=0, column=1, sticky="nsew")
panelDerecho.grid_columnconfigure(0, weight=1)

#Título del formulario
titulo = Label(panelDerecho, text="Datos del producto", font=("Segoe UI", 17, "bold"),
    fg=CANELA, bg=DURAZNO)

titulo.grid(row=0, column=0, sticky="w", pady=(0, 5))

subtitulo = Label(panelDerecho, text="Registro de inventario", font=("Segoe UI", 10),
    fg=TEXTO, bg=DURAZNO
)

subtitulo.grid(row=1, column=0, sticky="w", pady=(0, 15))

#Función para crear etiquetas y entradas
def crearCampo(fila, texto, solo_lectura=False):

    etiqueta = Label(panelDerecho, text=texto, font=("Segoe UI", 10, "bold"),
        fg=TEXTO, bg=DURAZNO)

    etiqueta.grid(row=fila, column=0, sticky="w", pady=(5, 3))

    cuadro = Entry(panelDerecho, font=("Segoe UI", 10), bg=BLANCO, fg=TEXTO,
        insertbackground=CANELA, relief="flat", bd=0)

    cuadro.grid(row=fila + 1, column=0, sticky="ew", ipady=7, pady=(0, 5))

    if solo_lectura:
        cuadro.config(state="readonly")

    return cuadro


# Campos del producto
cuadroID = crearCampo(2, "ID del producto", solo_lectura=True)
cuadroNombre = crearCampo(4, "Nombre del producto")
cuadroMarca = crearCampo(6, "Marca / proveedor")
cuadroCantidad = crearCampo(8, "Cantidad en existencia")
cuadroPrecio = crearCampo(10, "Precio por unidad ($ MXN)")
cuadroCategoria = crearCampo(12, "Categoría")
cuadroUnidad = crearCampo(14, "Unidad de medida (kg, pieza, litro...)")


#Pestaña INVENTARIO
pestanaInventario = Frame(pestanas, bg=CREMA)

pestanas.add(pestanaInventario, text="Inventario")

tituloInventario = Label(pestanaInventario, text="Inventario",
    font=("Segoe UI", 20, "bold"), fg=CANELA, bg=CREMA)

tituloInventario.place(relx=0.5, rely=0.5, anchor="center")


#Pestaña de VENTAS
pestanaVentas = Frame(pestanas, bg=CREMA)

pestanas.add(pestanaVentas, text="Ventas")

tituloVentas = Label(pestanaVentas, text="Ventas", font=("Segoe UI", 20, "bold"),
    fg=CANELA, bg=CREMA)

tituloVentas.place(relx=0.5, rely=0.5, anchor="center")


#Pestaña CLIENTES
pestanaClientes = Frame(pestanas, bg=CREMA)

pestanas.add(pestanaClientes, text="Clientes")

tituloClientes = Label(pestanaClientes, text="Clientes", font=("Segoe UI", 20, "bold"),
    fg=CANELA, bg=CREMA)

tituloClientes.place(relx=0.5, rely=0.5, anchor="center")

#Ejecutar el programa
raiz.mainloop()
