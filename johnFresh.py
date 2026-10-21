
from tkinter import *
from tkinter import ttk
from tkinter import messagebox  #Permite mostrar mensajes de aviso y confirmación

#Configuración de los colores para el sistema
CANELA = "#713F35"
TERRACOTA = "#A65D45"
DURAZNO = "#E8B99A"
CREMA = "#F8EBDD"
BLANCO = "#FFF9F2"
TEXTO = "#49312B"
BORDE = "#D3A18A"

#Lista temporal para guardar los productos
productos = []

#Ventana principal
raiz = Tk()
raiz.title("John's Fresh - Inventario")
raiz.geometry("1100x650")
raiz.minsize(900, 550)
raiz.config(bg=CREMA)

#Icono de la ventana
raiz.iconbitmap("Logo_JF_pequenio.ico")

#Estilo de las pestañas
estilo = ttk.Style()
estilo.theme_use("default")
estilo.configure("JF.TNotebook", background=CREMA, borderwidth=0)
estilo.configure("JF.TNotebook.Tab", background=DURAZNO, foreground=CANELA, padding=(18, 10), font=("Segoe UI", 10, "bold"))
estilo.map("JF.TNotebook.Tab", background=[("selected", CANELA)], foreground=[("selected", BLANCO)])

#Contenedor principal de las pestañas
pestanias = ttk.Notebook(raiz, style="JF.TNotebook")
pestanias.pack(fill="both", expand=True, padx=15, pady=15)

#Pestaña de INICIO
pestaniaInicio = Frame(pestanias, bg=CREMA)
pestanias.add(pestaniaInicio, text="Inicio")

#Dos columnas, izquierda grande y derecha pequeña
pestaniaInicio.grid_columnconfigure(0, weight=7, uniform="columnas")
pestaniaInicio.grid_columnconfigure(1, weight=4, uniform="columnas")
pestaniaInicio.grid_rowconfigure(0, weight=1)

#Lado izquierdo, imagen
panelIzquierdo = Frame(pestaniaInicio, bg=CREMA)
panelIzquierdo.grid(row=0, column=0, sticky="nsew", padx=(0, 12))

#Cargar y reducir la imagen PNG
try:
    logoPNG = PhotoImage(file="Logo_JF_grande.png").subsample(3, 3)
    etiquetaLogo = Label(panelIzquierdo, image=logoPNG, bg=CREMA)
    etiquetaLogo.place(relx=0.5, rely=0.5, anchor="center")
except TclError:
    etiquetaLogo = Label(panelIzquierdo, text="Aquí aparecerá el logo de John's Fresh", font=("Segoe UI", 12), fg=TEXTO, bg=CREMA)
    etiquetaLogo.place(relx=0.5, rely=0.5, anchor="center")

#Lado derecho, datos de los productos
panelDerecho = Frame(pestaniaInicio, bg=DURAZNO, bd=0, padx=18, pady=18)
panelDerecho.grid(row=0, column=1, sticky="nsew")
panelDerecho.grid_columnconfigure(0, weight=1)

#Título del formulario
titulo = Label(panelDerecho, text="Datos del producto", font=("Segoe UI", 17, "bold"), fg=CANELA, bg=DURAZNO)
titulo.grid(row=0, column=0, sticky="w", pady=(0, 5))

subtitulo = Label(panelDerecho, text="Registro de inventario", font=("Segoe UI", 10), fg=TEXTO, bg=DURAZNO)
subtitulo.grid(row=1, column=0, sticky="w", pady=(0, 10))

#Función para crear etiquetas y entradas
def crearCampo(fila, texto, solo_lectura=False):
    etiqueta = Label(panelDerecho, text=texto, font=("Segoe UI", 10, "bold"), fg=TEXTO, bg=DURAZNO)
    etiqueta.grid(row=fila, column=0, sticky="w", pady=(3, 2))

    cuadro = Entry(panelDerecho, font=("Segoe UI", 10), bg=BLANCO, fg=TEXTO, insertbackground=CANELA, relief="flat", bd=0)
    cuadro.grid(row=fila + 1, column=0, sticky="ew", ipady=5, pady=(0, 3))

    if solo_lectura:
        cuadro.config(state="readonly")

    return cuadro

#Campos del producto
cuadroID = crearCampo(2, "ID del producto", solo_lectura=True)
cuadroNombre = crearCampo(4, "Nombre del producto")
cuadroMarca = crearCampo(6, "Marca / proveedor")
cuadroCantidad = crearCampo(8, "Cantidad en existencia")
cuadroPrecio = crearCampo(10, "Precio por unidad ($ MXN)")
cuadroCategoria = crearCampo(12, "Categoría")
cuadroUnidad = crearCampo(14, "Unidad de medida (kg, pieza, litro, paquete...)")

#Función para limpiar los campos
def limpiarCampos():
    for cuadro in [cuadroNombre, cuadroMarca, cuadroCantidad, cuadroPrecio, cuadroCategoria, cuadroUnidad]:
        cuadro.delete(0, END)

#Función para registrar un producto
def registrarProducto():
    nombre = cuadroNombre.get().strip()
    marca = cuadroMarca.get().strip()
    cantidadTexto = cuadroCantidad.get().strip().replace(",", ".")
    precioTexto = cuadroPrecio.get().strip().replace(",", ".")
    categoria = cuadroCategoria.get().strip()
    unidad = cuadroUnidad.get().strip()

    #Validar que los campos obligatorios no estén vacíos
    if not nombre or not cantidadTexto or not precioTexto or not unidad:
        messagebox.showwarning("Campos incompletos", "Escribe el nombre, la cantidad, el precio y la unidad de medida.")
        return

    #Validar que la cantidad y el precio sean números
    try:
        cantidad = float(cantidadTexto)
        precio = float(precioTexto)
    except ValueError:
        messagebox.showerror("Datos incorrectos", "La cantidad y el precio deben ser números.")
        return

    #Comprobar que los valores sean válidos
    if cantidad <= 0:
        messagebox.showwarning("Cantidad incorrecta", "La cantidad debe ser mayor que cero.")
        return

    if precio < 0:
        messagebox.showwarning("Precio incorrecto", "El precio no puede ser negativo.")
        return

    #Asignar un ID automático al producto
    identificador = len(productos) + 1

    producto = {
        "ID": identificador,
        "Nombre": nombre,
        "Marca": marca,
        "Cantidad": cantidad,
        "Precio": precio,
        "Categoría": categoria,
        "Unidad": unidad
    }

    #Guardar el producto en la lista
    productos.append(producto)

    #Mostrar el ID asignado
    cuadroID.config(state="normal")
    cuadroID.delete(0, END)
    cuadroID.insert(0, identificador)
    cuadroID.config(state="readonly")

    #Confirmar el registro
    messagebox.showinfo("Producto registrado", f"El producto '{nombre}' se registró correctamente con el ID {identificador}.")

    #Limpiar los campos para el siguiente producto
    limpiarCampos()

#Botones del formulario
panelBotones = Frame(panelDerecho, bg=DURAZNO)
panelBotones.grid(row=16, column=0, sticky="ew", pady=(10, 0))
panelBotones.grid_columnconfigure(0, weight=1)
panelBotones.grid_columnconfigure(1, weight=1)

botonRegistrar = Button(panelBotones, text="Registrar producto", font=("Segoe UI", 10, "bold"), bg=CANELA, fg=BLANCO, activebackground=TERRACOTA, activeforeground=BLANCO, relief="flat", cursor="hand2", command=registrarProducto)
botonRegistrar.grid(row=0, column=0, sticky="ew", padx=(0, 5), ipady=6)

botonLimpiar = Button(panelBotones, text="Limpiar campos", font=("Segoe UI", 10, "bold"), bg=BLANCO, fg=CANELA, activebackground=DURAZNO, relief="flat", cursor="hand2", command=limpiarCampos)
botonLimpiar.grid(row=0, column=1, sticky="ew", padx=(5, 0), ipady=6)

#Pestaña INVENTARIO
pestaniaInventario = Frame(pestanias, bg=CREMA)
pestanias.add(pestaniaInventario, text="Inventario")

tituloInventario = Label(pestaniaInventario, text="Inventario", font=("Segoe UI", 20, "bold"), fg=CANELA, bg=CREMA)
tituloInventario.place(relx=0.5, rely=0.5, anchor="center")

#Pestaña de VENTAS
pestaniaVentas = Frame(pestanias, bg=CREMA)
pestanias.add(pestaniaVentas, text="Ventas")

tituloVentas = Label(pestaniaVentas, text="Ventas", font=("Segoe UI", 20, "bold"), fg=CANELA, bg=CREMA)
tituloVentas.place(relx=0.5, rely=0.5, anchor="center")

#Pestaña CLIENTES
pestaniaClientes = Frame(pestanias, bg=CREMA)
pestanias.add(pestaniaClientes, text="Clientes")

tituloClientes = Label(pestaniaClientes, text="Clientes", font=("Segoe UI", 20, "bold"), fg=CANELA, bg=CREMA)
tituloClientes.place(relx=0.5, rely=0.5, anchor="center")

#Ejecutar el programa
raiz.mainloop()
