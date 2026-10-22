from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Configuración de los colores para el sistema
CANELA = "#713F35"
TERRACOTA = "#A65D45"
DURAZNO = "#E8B99A"
CREMA = "#F8EBDD"
BLANCO = "#FFF9F2"
TEXTO = "#49312B"
BORDE = "#D3A18A"
DURAZNO_CLARO = "#F0D9C5"
FONDO = "#DCE4D5"
ROJO = "#A64035"

#Lista temporal para guardar los productos
productos = []
siguienteID = 1
productoSeleccionadoID = None

#Configuración de la ventana principal
raiz = Tk()
raiz.title("John's Fresh - Sistema de punto de venta")
raiz.geometry("1050x750")
raiz.minsize(900, 650)
raiz.configure(bg=FONDO)

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
    background=FONDO,
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
    bg=FONDO,
    fg=CANELA
)
titulo.pack(pady=(15, 0))

subtitulo = Label(
    raiz,
    text="Sistema de punto de venta e inventario",
    font=("Arial", 11),
    bg=FONDO,
    fg=TEXTO
)
subtitulo.pack(pady=(0, 15))

#Creación de las pestañas principales
pestania = ttk.Notebook(raiz)
pestania.pack(fill="both", expand=True, padx=20, pady=(0, 15))

inicio = Frame(pestania, bg=FONDO)
inventario = Frame(pestania, bg=FONDO)
ventas = Frame(pestania, bg=FONDO)
clientes = Frame(pestania, bg=FONDO)

pestania.add(inicio, text="Inicio")
pestania.add(inventario, text="Inventario")
pestania.add(ventas, text="Ventas")
pestania.add(clientes, text="Clientes")

#========================================
#PESTAÑA INICIO
#========================================

#Panel del logo
panelLogo = Frame(inicio, bg=FONDO)
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
        bg=FONDO,
        bd=0
    )
    etiquetaLogo.pack(expand=True)

except (TclError, RuntimeError):
    etiquetaLogo = Label(
        panelLogo,
        text="John's Fresh",
        font=("Arial", 27, "bold"),
        bg=FONDO,
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
tituloFormulario.pack(pady=(15, 10))

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
    etiqueta.pack(fill="x", padx=25, pady=(4, 2))
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
cuadroID.pack(fill="x", padx=25, ipady=3)
cuadroID.configure(state="readonly")

#Campo nombre
crearEtiqueta("Nombre del producto")
cuadroNombre = crearCampo()
cuadroNombre.pack(fill="x", padx=25, ipady=3)

#Campo marca
crearEtiqueta("Marca")
cuadroMarca = crearCampo()
cuadroMarca.pack(fill="x", padx=25, ipady=3)

#Campo cantidad
crearEtiqueta("Cantidad")
cuadroCantidad = crearCampo()
cuadroCantidad.pack(fill="x", padx=25, ipady=3)

#Campo precio
crearEtiqueta("Precio")
cuadroPrecio = crearCampo()
cuadroPrecio.pack(fill="x", padx=25, ipady=3)

#Campo categoría
crearEtiqueta("Categoría")
cuadroCategoria = crearCampo()
cuadroCategoria.pack(fill="x", padx=25, ipady=3)

#Campo unidad
crearEtiqueta("Unidad de medida")
cuadroUnidad = crearCampo()
cuadroUnidad.pack(fill="x", padx=25, ipady=3)

#Función para limpiar el formulario
def limpiarCampos():
    global productoSeleccionadoID

    productoSeleccionadoID = None

    cuadroID.configure(state="normal")
    cuadroID.delete(0, END)
    cuadroID.configure(state="readonly")

    cuadroNombre.delete(0, END)
    cuadroMarca.delete(0, END)
    cuadroCantidad.delete(0, END)
    cuadroPrecio.delete(0, END)
    cuadroCategoria.delete(0, END)
    cuadroUnidad.delete(0, END)

    #Quitar la selección de la tabla si existe
    seleccion = tablaInventario.selection()
    if seleccion:
        tablaInventario.selection_remove(*seleccion)

#========================================
#PESTAÑA INVENTARIO
#========================================

#Título del inventario
tituloInventario = Label(
    inventario,
    text="Inventario de productos",
    font=("Arial", 18, "bold"),
    bg=FONDO,
    fg=CANELA
)
tituloInventario.pack(pady=(20, 5))

mensajeInventario = Label(
    inventario,
    text="Selecciona un producto para consultarlo, editarlo o eliminarlo",
    font=("Arial", 11),
    bg=FONDO,
    fg=TEXTO
)
mensajeInventario.pack(pady=(0, 12))

#Panel que contiene la tabla
panelTabla = Frame(inventario, bg=FONDO)
panelTabla.pack(
    fill="both",
    expand=True,
    padx=15,
    pady=(0, 8)
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

#Colores alternados para las filas
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
    tablaInventario.heading(columna, text=columna)
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
tablaInventario.grid(row=0, column=0, sticky="nsew")
barraVertical.grid(row=0, column=1, sticky="ns")
barraHorizontal.grid(row=1, column=0, sticky="ew")

panelTabla.grid_rowconfigure(0, weight=1)
panelTabla.grid_columnconfigure(0, weight=1)

#Función para actualizar la tabla de inventario
def actualizarInventario():
    for fila in tablaInventario.get_children():
        tablaInventario.delete(fila)

    for indice, producto in enumerate(productos):
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
def seleccionarProducto(event=None):
    global productoSeleccionadoID

    seleccion = tablaInventario.selection()

    if not seleccion:
        return

    valores = tablaInventario.item(
        seleccion[0],
        "values"
    )

    if not valores:
        return

    identificador = int(valores[0])

    #Buscar el producto seleccionado
    for producto in productos:
        if producto["ID"] == identificador:
            productoSeleccionadoID = identificador

            #Cargar el ID
            cuadroID.configure(state="normal")
            cuadroID.delete(0, END)
            cuadroID.insert(0, producto["ID"])
            cuadroID.configure(state="readonly")

            #Cargar el resto de los datos
            cuadroNombre.delete(0, END)
            cuadroNombre.insert(0, producto["Nombre"])

            cuadroMarca.delete(0, END)
            cuadroMarca.insert(0, producto["Marca"])

            cuadroCantidad.delete(0, END)
            cuadroCantidad.insert(0, f'{producto["Cantidad"]:g}')

            cuadroPrecio.delete(0, END)
            cuadroPrecio.insert(0, f'{producto["Precio"]:g}')

            cuadroCategoria.delete(0, END)
            cuadroCategoria.insert(0, producto["Categoría"])

            cuadroUnidad.delete(0, END)
            cuadroUnidad.insert(0, producto["Unidad"])

            break

#Detectar la selección de una fila
tablaInventario.bind(
    "<<TreeviewSelect>>",
    seleccionarProducto
)

#Botones del inventario
panelBotonesInventario = Frame(inventario, bg=FONDO)
panelBotonesInventario.pack(
    fill="x",
    padx=15,
    pady=(0, 15)
)

#Función para abrir Inicio y editar el producto
def irAEditar():
    if productoSeleccionadoID is None:
        messagebox.showwarning(
            "Selecciona un producto",
            "Primero selecciona un producto de la tabla."
        )
        return

    pestania.select(inicio)

#Botón para editar
botonEditar = Button(
    panelBotonesInventario,
    text="Editar en Inicio",
    command=irAEditar,
    font=("Arial", 10, "bold"),
    bg=CANELA,
    fg=BLANCO,
    activebackground=TERRACOTA,
    activeforeground=BLANCO,
    relief="flat",
    cursor="hand2"
)
botonEditar.pack(side="left", padx=(0, 8), ipady=5, ipadx=8)

#Función para eliminar un producto
def eliminarProducto():
    global productoSeleccionadoID

    #Verificar que haya un producto seleccionado
    if productoSeleccionadoID is None:
        messagebox.showwarning(
            "Selecciona un producto",
            "Selecciona en la tabla el producto que deseas eliminar."
        )
        return

    #Buscar el producto por su ID
    productoEliminar = None

    for producto in productos:
        if producto["ID"] == productoSeleccionadoID:
            productoEliminar = producto
            break

    if productoEliminar is None:
        messagebox.showerror(
            "Producto no encontrado",
            "No se encontró el producto seleccionado."
        )
        return

    #Solicitar confirmación antes de eliminar
    confirmar = messagebox.askyesno(
        "Confirmar eliminación",
        f"¿Seguro que deseas eliminar '{productoEliminar['Nombre']}'?\n\n"
        "Esta acción no se puede deshacer."
    )

    if not confirmar:
        return

    #Eliminar el producto de la lista
    productos.remove(productoEliminar)

    #Actualizar la tabla
    actualizarInventario()

    #Limpiar el formulario y la selección
    limpiarCampos()

    messagebox.showinfo(
        "Producto eliminado",
        "El producto se eliminó correctamente."
    )

#Botón para eliminar en Inventario
botonEliminar = Button(
    panelBotonesInventario,
    text="Eliminar producto",
    command=eliminarProducto,
    font=("Arial", 10, "bold"),
    bg=ROJO,
    fg=BLANCO,
    activebackground="#82332B",
    activeforeground=BLANCO,
    relief="flat",
    cursor="hand2"
)
botonEliminar.pack(side="left", padx=8, ipady=5, ipadx=8)

#========================================
#FUNCIONES DE REGISTRO Y EDICIÓN
#========================================

#Función para obtener y validar los datos del formulario
def obtenerDatosFormulario():
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
        return None

    #Validar los datos numéricos
    try:
        cantidad = float(cantidadTexto.replace(",", "."))
        precio = float(precioTexto.replace(",", "."))
    except ValueError:
        messagebox.showerror(
            "Datos inválidos",
            "La cantidad y el precio deben ser números válidos."
        )
        return None

    #Validar que los valores sean razonables
    if cantidad <= 0:
        messagebox.showwarning(
            "Cantidad inválida",
            "La cantidad debe ser mayor que cero."
        )
        return None

    if precio < 0:
        messagebox.showwarning(
            "Precio inválido",
            "El precio no puede ser negativo."
        )
        return None

    #Regresar los datos validados
    return {
        "Nombre": nombre,
        "Marca": marca,
        "Cantidad": cantidad,
        "Precio": precio,
        "Categoría": categoria,
        "Unidad": unidad
    }

#Función para registrar un producto nuevo
def registrarProducto():
    global siguienteID

    #No registrar uno nuevo si se está editando otro
    if productoSeleccionadoID is not None:
        messagebox.showwarning(
            "Producto seleccionado",
            "Estás editando un producto existente.\n"
            "Pulsa Guardar cambios o Limpiar campos antes de registrar otro."
        )
        return

    datos = obtenerDatosFormulario()

    if datos is None:
        return

    #Crear el producto con un ID nuevo
    producto = {
        "ID": siguienteID,
        **datos
    }

    productos.append(producto)
    identificador = siguienteID
    siguienteID += 1

    #Actualizar la tabla
    actualizarInventario()

    messagebox.showinfo(
        "Producto registrado",
        f"El producto '{producto['Nombre']}' se registró correctamente.\n"
        f"ID: {identificador}"
    )

    limpiarCampos()

#Función para guardar los cambios de un producto
def guardarCambios():
    if productoSeleccionadoID is None:
        messagebox.showwarning(
            "Selecciona un producto",
            "Selecciona un producto del inventario antes de guardar cambios."
        )
        return

    datos = obtenerDatosFormulario()

    if datos is None:
        return

    #Buscar el producto que se va a actualizar
    for producto in productos:
        if producto["ID"] == productoSeleccionadoID:
            producto.update(datos)
            break
    else:
        messagebox.showerror(
            "Producto no encontrado",
            "No se pudo encontrar el producto que deseas modificar."
        )
        return

    #Actualizar la tabla
    actualizarInventario()

    #Limpiar el formulario
    limpiarCampos()

    messagebox.showinfo(
        "Cambios guardados",
        "El producto se actualizó correctamente."
    )

#========================================
#BOTONES DEL FORMULARIO
#========================================

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
    pady=(10, 4),
    ipady=4
)

#Botón para guardar cambios
botonGuardar = Button(
    panelFormulario,
    text="Guardar cambios",
    command=guardarCambios,
    font=("Arial", 10, "bold"),
    bg=TERRACOTA,
    fg=BLANCO,
    activebackground=CANELA,
    activeforeground=BLANCO,
    relief="flat",
    cursor="hand2"
)
botonGuardar.pack(
    fill="x",
    padx=25,
    pady=4,
    ipady=4
)

#Botón para limpiar el formulario
botonLimpiar = Button(
    panelFormulario,
    text="Limpiar campos",
    command=limpiarCampos,
    font=("Arial", 10, "bold"),
    bg=DURAZNO,
    fg=TEXTO,
    activebackground=DURAZNO_CLARO,
    activeforeground=TEXTO,
    relief="flat",
    cursor="hand2"
)
botonLimpiar.pack(
    fill="x",
    padx=25,
    pady=(4, 12),
    ipady=4
)

#========================================
#PESTAÑA VENTAS
#========================================

tituloVentas = Label(
    ventas,
    text="Ventas",
    font=("Arial", 20, "bold"),
    bg=FONDO,
    fg=CANELA
)
tituloVentas.pack(pady=(40, 10))

mensajeVentas = Label(
    ventas,
    text="Aquí construiremos el módulo de ventas y tickets.",
    font=("Arial", 11),
    bg=FONDO,
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
    bg=FONDO,
    fg=CANELA
)
tituloClientes.pack(pady=(40, 10))

mensajeClientes = Label(
    clientes,
    text="Aquí construiremos el registro y la gestión de clientes.",
    font=("Arial", 11),
    bg=FONDO,
    fg=TEXTO
)
mensajeClientes.pack(pady=5)

#Inicio del programa
raiz.mainloop()
