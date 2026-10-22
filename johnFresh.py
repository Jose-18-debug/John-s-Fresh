
from tkinter import *
from tkinter import ttk  #Importa componentes de Tkinter con estilos modernos
from tkinter import messagebox  #Importa ventanas emergentes para mostrar mensajes

#Configuración de los colores para el sistema
CANELA = "#713F35"
TERRACOTA = "#A65D45"
DURAZNO = "#E8B99A"
CREMA = "#F8EBDD"
BLANCO = "#FFF9F2"
TEXTO = "#49312B"
BORDE = "#D3A18A"
DURAZNO_CLARO = "#F0D9C5"

#Lista temporal para guardar los productos
productos = []
siguienteID = 1

#Configuración de la ventana principal
raiz = Tk()
raiz.title("John's Fresh - Sistema de punto de venta")
raiz.geometry("1050x750")
raiz.minsize(900, 650)
raiz.configure(bg=CREMA)

#Configuración del icono de la aplicación
try:
    raiz.iconbitmap("Logo_JF_pequenio.ico")
except TclError:
    pass

#Configuración de los estilos
estilo = ttk.Style()
estilo.theme_use("clam")

estilo.configure(
    "TNotebook",
    background=CREMA,
    borderwidth=0
)

estilo.configure(
    "TNotebook.Tab",
    background=DURAZNO,
    foreground=TEXTO,
    padding=[18, 10],
    font=("Arial", 10, "bold")
)

estilo.map(
    "TNotebook.Tab",
    background=[("selected", CANELA)],
    foreground=[("selected", BLANCO)]
)

estilo.configure(
    "Treeview",
    background=BLANCO,
    foreground=TEXTO,
    fieldbackground=BLANCO,
    rowheight=30,
    font=("Arial", 10)
)

estilo.configure(
    "Treeview.Heading",
    background=CANELA,
    foreground=BLANCO,
    font=("Arial", 10, "bold")
)

estilo.map(
    "Treeview",
    background=[("selected", TERRACOTA)],
    foreground=[("selected", BLANCO)]
)

#Encabezado principal
titulo = Label(
    raiz,
    text="John's Fresh",
    font=("Arial", 25, "bold"),
    bg=CREMA,
    fg=CANELA
)
titulo.pack(pady=(15, 0))

subtitulo = Label(
    raiz,
    text="Sistema de punto de venta e inventario",
    font=("Arial", 11),
    bg=CREMA,
    fg=TEXTO
)
subtitulo.pack(pady=(0, 15))

#Creación de las pestañas principales
pestania = ttk.Notebook(raiz)
pestania.pack(fill="both", expand=True, padx=20, pady=(0, 15))

inicio = Frame(pestania, bg=CREMA)
inventario = Frame(pestania, bg=CREMA)
ventas = Frame(pestania, bg=CREMA)
clientes = Frame(pestania, bg=CREMA)

pestania.add(inicio, text="Inicio")
pestania.add(inventario, text="Inventario")
pestania.add(ventas, text="Ventas")
pestania.add(clientes, text="Clientes")

#========================================
#PESTAÑA INICIO
#========================================

#Panel del logo
panelLogo = Frame(inicio, bg=CREMA)
panelLogo.pack(
    side="left",
    fill="both",
    expand=True,
    padx=(15, 8),
    pady=10
)

#Panel del formulario
panelFormulario = Frame(inicio, bg=BLANCO)
panelFormulario.pack(
    side="right",
    fill="both",
    expand=True,
    padx=(8, 15),
    pady=10
)

#Carga del logo
try:
    logo = PhotoImage(file="Logo_JF_grande.png")
    logo = logo.subsample(3, 3)

    etiquetaLogo = Label(
        panelLogo,
        image=logo,
        bg=CREMA,
        bd=0
    )
    etiquetaLogo.pack(expand=True)

except (TclError, RuntimeError):
    etiquetaLogo = Label(
        panelLogo,
        text="John's Fresh",
        font=("Arial", 27, "bold"),
        bg=CREMA,
        fg=CANELA
    )
    etiquetaLogo.pack(expand=True)

#Título del formulario
tituloFormulario = Label(
    panelFormulario,
    text="Registro de productos",
    font=("Arial", 17, "bold"),
    bg=BLANCO,
    fg=CANELA
)
tituloFormulario.pack(pady=(20, 15))

#Función para crear etiquetas del formulario
def crearEtiqueta(texto):
    etiqueta = Label(
        panelFormulario,
        text=texto,
        font=("Arial", 10, "bold"),
        bg=BLANCO,
        fg=TEXTO,
        anchor="w"
    )
    etiqueta.pack(fill="x", padx=25, pady=(5, 2))
    return etiqueta

#Función para crear campos de texto
def crearCampo():
    return Entry(
        panelFormulario,
        font=("Arial", 10),
        bg=BLANCO,
        fg=TEXTO,
        relief="solid",
        bd=1,
        highlightbackground=BORDE
    )

#Campo ID
crearEtiqueta("ID del producto")
cuadroID = crearCampo()
cuadroID.pack(fill="x", padx=25, ipady=4)
cuadroID.configure(state="readonly")

#Campo nombre
crearEtiqueta("Nombre del producto")
cuadroNombre = crearCampo()
cuadroNombre.pack(fill="x", padx=25, ipady=4)

#Campo marca
crearEtiqueta("Marca")
cuadroMarca = crearCampo()
cuadroMarca.pack(fill="x", padx=25, ipady=4)

#Campo cantidad
crearEtiqueta("Cantidad")
cuadroCantidad = crearCampo()
cuadroCantidad.pack(fill="x", padx=25, ipady=4)

#Campo precio
crearEtiqueta("Precio")
cuadroPrecio = crearCampo()
cuadroPrecio.pack(fill="x", padx=25, ipady=4)

#Campo categoría
crearEtiqueta("Categoría")
cuadroCategoria = crearCampo()
cuadroCategoria.pack(fill="x", padx=25, ipady=4)

#Campo unidad
crearEtiqueta("Unidad de medida")
cuadroUnidad = crearCampo()
cuadroUnidad.pack(fill="x", padx=25, ipady=4)

#Función para limpiar el formulario
def limpiarCampos():
    cuadroID.configure(state="normal")
    cuadroID.delete(0, END)
    cuadroID.configure(state="readonly")

    cuadroNombre.delete(0, END)
    cuadroMarca.delete(0, END)
    cuadroCantidad.delete(0, END)
    cuadroPrecio.delete(0, END)
    cuadroCategoria.delete(0, END)
    cuadroUnidad.delete(0, END)

#Botón para limpiar el formulario
botonLimpiar = Button(
    panelFormulario,
    text="Limpiar campos",
    command=limpiarCampos,
    font=("Arial", 10, "bold"),
    bg=DURAZNO,
    fg=TEXTO,
    activebackground=TERRACOTA,
    activeforeground=BLANCO,
    relief="flat",
    cursor="hand2"
)
botonLimpiar.pack(fill="x", padx=25, pady=(15, 20), ipady=5)

#========================================
#PESTAÑA INVENTARIO
#========================================

#Título del inventario
tituloInventario = Label(
    inventario,
    text="Inventario de productos",
    font=("Arial", 18, "bold"),
    bg=CREMA,
    fg=CANELA
)
tituloInventario.pack(pady=(20, 5))

mensajeInventario = Label(
    inventario,
    text="Productos registrados en John's Fresh",
    font=("Arial", 11),
    bg=CREMA,
    fg=TEXTO
)
mensajeInventario.pack(pady=(0, 12))

#Panel que contiene la tabla
panelTabla = Frame(inventario, bg=CREMA)
panelTabla.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 15)
)

#Columnas de la tabla
columnas = (
    "ID",
    "Nombre",
    "Marca",
    "Cantidad",
    "Precio",
    "Categoría",
    "Unidad"
)

#Creación de la tabla
tablaInventario = ttk.Treeview(
    panelTabla,
    columns=columnas,
    show="headings",
    selectmode="browse"
)

#Colores otoñales para las filas
tablaInventario.tag_configure(
    "fila_clara",
    background=BLANCO,
    foreground=TEXTO
)

tablaInventario.tag_configure(
    "fila_otoñal",
    background=DURAZNO_CLARO,
    foreground=TEXTO
)

#Configuración de los encabezados y las columnas
anchos = {
    "ID": 55,
    "Nombre": 150,
    "Marca": 110,
    "Cantidad": 85,
    "Precio": 90,
    "Categoría": 120,
    "Unidad": 100
}

for columna in columnas:
    tablaInventario.heading(
        columna,
        text=columna
    )

    tablaInventario.column(
        columna,
        width=anchos[columna],
        minwidth=50,
        anchor="center"
    )

#Barras de desplazamiento
barraVertical = ttk.Scrollbar(
    panelTabla,
    orient="vertical",
    command=tablaInventario.yview
)

barraHorizontal = ttk.Scrollbar(
    panelTabla,
    orient="horizontal",
    command=tablaInventario.xview
)

tablaInventario.configure(
    yscrollcommand=barraVertical.set,
    xscrollcommand=barraHorizontal.set
)

#Ubicación de la tabla y las barras
tablaInventario.grid(
    row=0,
    column=0,
    sticky="nsew"
)

barraVertical.grid(
    row=0,
    column=1,
    sticky="ns"
)

barraHorizontal.grid(
    row=1,
    column=0,
    sticky="ew"
)

panelTabla.grid_rowconfigure(0, weight=1)
panelTabla.grid_columnconfigure(0, weight=1)

#Función para actualizar la tabla de inventario
def actualizarInventario():
    #Eliminar las filas anteriores de la tabla
    for fila in tablaInventario.get_children():
        tablaInventario.delete(fila)

    #Agregar los productos registrados a la tabla
    for indice, producto in enumerate(productos):
        #Alternar el color según la posición de la fila
        if indice % 2 == 0:
            colorFila = "fila_clara"
        else:
            colorFila = "fila_otoñal"

        tablaInventario.insert(
            "",
            END,
            values=(
                producto["ID"],
                producto["Nombre"],
                producto["Marca"],
                f'{producto["Cantidad"]:g}',
                f'${producto["Precio"]:,.2f}',
                producto["Categoría"],
                producto["Unidad"]
            ),
            tags=(colorFila,)
        )

#Función para seleccionar un producto de la tabla
def seleccionarProducto(event):
    #Obtener la fila seleccionada
    seleccion = tablaInventario.selection()

    #Verificar que exista una fila seleccionada
    if not seleccion:
        return

    #Obtener los datos de la fila seleccionada
    valores = tablaInventario.item(
        seleccion[0],
        "values"
    )

    #Obtener el ID del producto seleccionado
    identificador = int(valores[0])

    #Buscar el producto original en la lista
    for producto in productos:
        if producto["ID"] == identificador:
            #Cargar el ID en su campo
            cuadroID.configure(state="normal")
            cuadroID.delete(0, END)
            cuadroID.insert(0, producto["ID"])
            cuadroID.configure(state="readonly")

            #Cargar el nombre
            cuadroNombre.delete(0, END)
            cuadroNombre.insert(0, producto["Nombre"])

            #Cargar la marca
            cuadroMarca.delete(0, END)
            cuadroMarca.insert(0, producto["Marca"])

            #Cargar la cantidad
            cuadroCantidad.delete(0, END)
            cuadroCantidad.insert(
                0,
                f'{producto["Cantidad"]:g}'
            )

            #Cargar el precio
            cuadroPrecio.delete(0, END)
            cuadroPrecio.insert(
                0,
                f'{producto["Precio"]:g}'
            )

            #Cargar la categoría
            cuadroCategoria.delete(0, END)
            cuadroCategoria.insert(
                0,
                producto["Categoría"]
            )

            #Cargar la unidad
            cuadroUnidad.delete(0, END)
            cuadroUnidad.insert(
                0,
                producto["Unidad"]
            )

            #Cambiar a la pestaña del formulario
            pestania.select(inicio)

            break

#Detectar cuando el usuario selecciona una fila
tablaInventario.bind(
    "<<TreeviewSelect>>",
    seleccionarProducto
)

#========================================
#REGISTRO DE PRODUCTOS
#========================================

#Función para registrar un producto
def registrarProducto():
    global siguienteID

    #Obtener los datos del formulario
    nombre = cuadroNombre.get().strip()
    marca = cuadroMarca.get().strip()
    cantidadTexto = cuadroCantidad.get().strip()
    precioTexto = cuadroPrecio.get().strip()
    categoria = cuadroCategoria.get().strip()
    unidad = cuadroUnidad.get().strip()

    #Validar los campos obligatorios
    if not nombre or not cantidadTexto or not precioTexto or not unidad:
        messagebox.showwarning(
            "Campos obligatorios",
            "Completa el nombre, la cantidad, el precio y la unidad."
        )
        return

    #Validar los datos numéricos
    try:
        cantidad = float(cantidadTexto.replace(",", "."))
        precio = float(precioTexto.replace(",", "."))
    except ValueError:
        messagebox.showerror(
            "Datos inválidos",
            "La cantidad y el precio deben ser números válidos."
        )
        return

    #Comprobar que la cantidad sea positiva
    if cantidad <= 0:
        messagebox.showwarning(
            "Cantidad inválida",
            "La cantidad debe ser mayor que cero."
        )
        return

    #Comprobar que el precio no sea negativo
    if precio < 0:
        messagebox.showwarning(
            "Precio inválido",
            "El precio no puede ser negativo."
        )
        return

    #Generar el ID del nuevo producto
    identificador = siguienteID

    #Crear el producto
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
    siguienteID += 1

    #Actualizar la tabla de inventario
    actualizarInventario()

    #Mostrar el ID asignado
    cuadroID.configure(state="normal")
    cuadroID.delete(0, END)
    cuadroID.insert(0, identificador)
    cuadroID.configure(state="readonly")

    #Mostrar mensaje de confirmación
    messagebox.showinfo(
        "Producto registrado",
        f"El producto '{nombre}' se registró correctamente.\nID: {identificador}"
    )

    #Limpiar el formulario
    limpiarCampos()

#Botón para registrar productos
botonRegistrar = Button(
    panelFormulario,
    text="Registrar producto",
    command=registrarProducto,
    font=("Arial", 10, "bold"),
    bg=CANELA,
    fg=BLANCO,
    activebackground=TERRACOTA,
    activeforeground=BLANCO,
    relief="flat",
    cursor="hand2"
)
botonRegistrar.pack(
    fill="x",
    padx=25,
    pady=(0, 5),
    ipady=5
)

#========================================
#PESTAÑA VENTAS
#========================================

tituloVentas = Label(
    ventas,
    text="Ventas",
    font=("Arial", 20, "bold"),
    bg=CREMA,
    fg=CANELA
)
tituloVentas.pack(pady=(40, 10))

mensajeVentas = Label(
    ventas,
    text="Aquí construiremos el módulo de ventas y tickets.",
    font=("Arial", 11),
    bg=CREMA,
    fg=TEXTO
)
mensajeVentas.pack(pady=5)

#========================================
#PESTAÑA CLIENTES
#========================================

tituloClientes = Label(
    clientes,
    text="Clientes",
    font=("Arial", 20, "bold"),
    bg=CREMA,
    fg=CANELA
)
tituloClientes.pack(pady=(40, 10))

mensajeClientes = Label(
    clientes,
    text="Aquí construiremos el registro y la gestión de clientes.",
    font=("Arial", 11),
    bg=CREMA,
    fg=TEXTO
)
mensajeClientes.pack(pady=5)

#Inicio del programa
raiz.mainloop()
