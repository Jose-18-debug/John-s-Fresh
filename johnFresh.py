
from tkinter import *
from tkinter import ttk         #Importa componentes de Tkinter con estilos modernos
from tkinter import messagebox  #Importa ventanas emergentes para mostrar mensajes
from tkinter import filedialog  #Permite elegir dónde guardar los tickets
from datetime import datetime   #Permite obtener la fecha y hora de cada venta

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

#Listas temporales para los productos y la venta actual
productos = [
    {"ID": 1, "Nombre": "Arroz", "Marca": "Verde Valle", "Cantidad": 25, "Precio": 32.00, "Categoría": "Granos y Semillas", "Unidad": "Kilogramos"},
    {"ID": 2, "Nombre": "Frijol negro", "Marca": "Verde Valle", "Cantidad": 20, "Precio": 38.00, "Categoría": "Granos y Semillas", "Unidad": "Kilogramos"},
    {"ID": 3, "Nombre": "Azúcar", "Marca": "Zulka", "Cantidad": 15, "Precio": 30.00, "Categoría": "Abarrotes", "Unidad": "Kilogramos"},
    {"ID": 4, "Nombre": "Sal", "Marca": "La Fina", "Cantidad": 20, "Precio": 18.00, "Categoría": "Condimentos y Especias", "Unidad": "Kilogramos"},
    {"ID": 5, "Nombre": "Aceite vegetal", "Marca": "Nutrioli", "Cantidad": 18, "Precio": 42.00, "Categoría": "Abarrotes", "Unidad": "Botellas"},
    {"ID": 6, "Nombre": "Leche entera", "Marca": "Lala", "Cantidad": 24, "Precio": 29.00, "Categoría": "Lácteos", "Unidad": "Litros"},
    {"ID": 7, "Nombre": "Yogur", "Marca": "Danone", "Cantidad": 15, "Precio": 18.00, "Categoría": "Lácteos", "Unidad": "Piezas"},
    {"ID": 8, "Nombre": "Queso panela", "Marca": "Lala", "Cantidad": 10, "Precio": 45.00, "Categoría": "Lácteos", "Unidad": "Piezas"},
    {"ID": 9, "Nombre": "Huevo", "Marca": "Granja local", "Cantidad": 12, "Precio": 48.00, "Categoría": "Abarrotes", "Unidad": "Docenas"},
    {"ID": 10, "Nombre": "Manzana", "Marca": "A granel", "Cantidad": 15, "Precio": 42.00, "Categoría": "Frutas", "Unidad": "Kilogramos"},
    {"ID": 11, "Nombre": "Plátano", "Marca": "A granel", "Cantidad": 18, "Precio": 28.00, "Categoría": "Frutas", "Unidad": "Kilogramos"},
    {"ID": 12, "Nombre": "Naranja", "Marca": "A granel", "Cantidad": 20, "Precio": 25.00, "Categoría": "Frutas", "Unidad": "Kilogramos"},
    {"ID": 13, "Nombre": "Jitomate", "Marca": "A granel", "Cantidad": 15, "Precio": 32.00, "Categoría": "Verduras", "Unidad": "Kilogramos"},
    {"ID": 14, "Nombre": "Papa", "Marca": "A granel", "Cantidad": 20, "Precio": 28.00, "Categoría": "Verduras", "Unidad": "Kilogramos"},
    {"ID": 15, "Nombre": "Cebolla", "Marca": "A granel", "Cantidad": 12, "Precio": 30.00, "Categoría": "Verduras", "Unidad": "Kilogramos"},
    {"ID": 16, "Nombre": "Atún en lata", "Marca": "Dolores", "Cantidad": 30, "Precio": 22.00, "Categoría": "Enlatados", "Unidad": "Latas"},
    {"ID": 17, "Nombre": "Chiles enlatados", "Marca": "La Costeña", "Cantidad": 18, "Precio": 19.00, "Categoría": "Enlatados", "Unidad": "Latas"},
    {"ID": 18, "Nombre": "Refresco", "Marca": "Coca-Cola", "Cantidad": 24, "Precio": 20.00, "Categoría": "Bebidas", "Unidad": "Botellas"},
    {"ID": 19, "Nombre": "Agua natural", "Marca": "Bonafont", "Cantidad": 30, "Precio": 12.00, "Categoría": "Bebidas", "Unidad": "Botellas"},
    {"ID": 20, "Nombre": "Papas fritas", "Marca": "Sabritas", "Cantidad": 25, "Precio": 18.00, "Categoría": "Botanas y Dulces", "Unidad": "Piezas"},
    {"ID": 21, "Nombre": "Galletas", "Marca": "Gamesa", "Cantidad": 20, "Precio": 17.00, "Categoría": "Botanas y Dulces", "Unidad": "Paquetes"},
    {"ID": 22, "Nombre": "Detergente", "Marca": "Ariel", "Cantidad": 12, "Precio": 38.00, "Categoría": "Productos de Limpieza", "Unidad": "Paquetes"},
    {"ID": 23, "Nombre": "Jabón de baño", "Marca": "Zest", "Cantidad": 20, "Precio": 16.00, "Categoría": "Higiene Personal", "Unidad": "Piezas"},
    {"ID": 24, "Nombre": "Esponja para trastes", "Marca": "Scotch-Brite", "Cantidad": 15, "Precio": 15.00, "Categoría": "Productos de Cocina", "Unidad": "Piezas"}
]

siguienteID = len(productos) + 1
productoSeleccionadoID = None
carritoVentas = {}

#Control del folio de los tickets durante la sesión
siguienteFolio = 1

#Opciones para las listas desplegables
categorias = [
    "Verduras", "Frutas", "Granos y Semillas", "Lácteos",
    "Bebidas", "Botanas y Dulces", "Productos de Limpieza",
    "Productos de Cocina", "Carnes y Embutidos", "Abarrotes",
    "Enlatados", "Condimentos y Especias", "Higiene Personal",
    "Congelados", "Otros"
]

unidades = [
    "Piezas", "Kilogramos", "Gramos", "Litros",
    "Paquetes", "Cajas", "Botellas", "Latas",
    "Docenas", "Rollos"
]

#Configuración de la ventana principal
raiz = Tk()
raiz.title("John's Fresh - Sistema de punto de venta")
raiz.geometry("1100x800")
raiz.minsize(950, 700)
raiz.configure(bg=FONDO)

#Configuración del icono de la aplicación
try:
    raiz.iconbitmap("Logo_JF_pequenio.ico")
except TclError:
    pass

#Configuración de los estilos
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("TNotebook", background=FONDO, borderwidth=0)
estilo.configure("TNotebook.Tab", background=DURAZNO, foreground=TEXTO,
    padding=[18, 9], font=("Arial", 10, "bold"))
estilo.map("TNotebook.Tab", background=[("selected", CANELA)],
    foreground=[("selected", BLANCO)])
estilo.configure("Treeview", background=BLANCO, foreground=TEXTO,
    fieldbackground=BLANCO, rowheight=28, font=("Arial", 9))
estilo.configure("Treeview.Heading", background=CANELA, foreground=BLANCO,
    font=("Arial", 9, "bold"))
estilo.map("Treeview", background=[("selected", TERRACOTA)],
    foreground=[("selected", BLANCO)])

#Encabezado principal
titulo = Label(raiz, text="John's Fresh", font=("Arial", 24, "bold"),
    bg=FONDO, fg=CANELA)
titulo.pack(pady=(10, 0))

subtitulo = Label(raiz, text="Sistema de punto de venta e inventario",
    font=("Arial", 10), bg=FONDO, fg=TEXTO)
subtitulo.pack(pady=(0, 10))

#Creación de las pestañas principales
pestania = ttk.Notebook(raiz)
pestania.pack(fill="both", expand=True, padx=15, pady=(0, 10))

inicio = Frame(pestania, bg=FONDO)
inventario = Frame(pestania, bg=FONDO)
ventas = Frame(pestania, bg=FONDO)
clientes = Frame(pestania, bg=FONDO)

pestania.add(inicio, text="Inicio")
pestania.add(inventario, text="Inventario")
pestania.add(ventas, text="Ventas")
pestania.add(clientes, text="Clientes")

#PESTAÑA INICIO
#Panel del logo
panelLogo = Frame(inicio, bg=FONDO)
panelLogo.pack(side="left", fill="both", expand=True, padx=(15, 8), pady=10)

#Panel del formulario
panelFormulario = Frame(inicio, bg=BLANCO)
panelFormulario.pack(side="right", fill="both", expand=True, padx=(8, 15), pady=10)

#Carga del logo
try:
    logo = PhotoImage(file="Logo_JF_grande.png")
    logo = logo.subsample(3, 3)
    etiquetaLogo = Label(panelLogo, image=logo, bg=FONDO, bd=0)
    etiquetaLogo.pack(expand=True)
except (TclError, RuntimeError):
    etiquetaLogo = Label(panelLogo, text="John's Fresh",
        font=("Arial", 27, "bold"), bg=FONDO, fg=CANELA)
    etiquetaLogo.pack(expand=True)

#Título del formulario
tituloFormulario = Label(panelFormulario, text="Registro de productos",
    font=("Arial", 17, "bold"), bg=BLANCO, fg=CANELA)
tituloFormulario.pack(pady=(12, 8))

#Función para crear etiquetas del formulario
def crearEtiqueta(texto):
    etiqueta = Label(panelFormulario, text=texto, font=("Arial", 10, "bold"),
        bg=BLANCO, fg=TEXTO, anchor="w")
    etiqueta.pack(fill="x", padx=25, pady=(3, 1))
    return etiqueta

#Función para crear campos de texto
def crearCampo():
    return Entry(panelFormulario, font=("Arial", 10), bg=BLANCO, fg=TEXTO,
        relief="solid", bd=1, highlightbackground=BORDE)

#Campos del producto
crearEtiqueta("ID del producto")
cuadroID = crearCampo()
cuadroID.pack(fill="x", padx=25, ipady=3)
cuadroID.configure(state="readonly")

crearEtiqueta("Nombre del producto")
cuadroNombre = crearCampo()
cuadroNombre.pack(fill="x", padx=25, ipady=3)

crearEtiqueta("Marca")
cuadroMarca = crearCampo()
cuadroMarca.pack(fill="x", padx=25, ipady=3)

crearEtiqueta("Cantidad")
cuadroCantidad = crearCampo()
cuadroCantidad.pack(fill="x", padx=25, ipady=3)

crearEtiqueta("Precio")
cuadroPrecio = crearCampo()
cuadroPrecio.pack(fill="x", padx=25, ipady=3)

#Lista desplegable de categorías
crearEtiqueta("Categoría")
cuadroCategoria = ttk.Combobox(panelFormulario, values=categorias,
    state="readonly", font=("Arial", 10))
cuadroCategoria.pack(fill="x", padx=25, ipady=3)

#Lista desplegable de unidades de medida
crearEtiqueta("Unidad de medida")
cuadroUnidad = ttk.Combobox(panelFormulario, values=unidades,
    state="readonly", font=("Arial", 10))
cuadroUnidad.pack(fill="x", padx=25, ipady=3)

#PESTAÑA INVENTARIO
tituloInventario = Label(inventario, text="Inventario de productos",
    font=("Arial", 18, "bold"), bg=FONDO, fg=CANELA)
tituloInventario.pack(pady=(15, 4))

mensajeInventario = Label(inventario,
    text="Selecciona un producto para consultarlo, editarlo o eliminarlo",
    font=("Arial", 10), bg=FONDO, fg=TEXTO)
mensajeInventario.pack(pady=(0, 8))

#Panel de la tabla
panelTabla = Frame(inventario, bg=FONDO)
panelTabla.pack(fill="both", expand=True, padx=15, pady=(0, 6))

columnas = ("ID", "Nombre", "Marca", "Cantidad", "Precio", "Categoría", "Unidad")
tablaInventario = ttk.Treeview(panelTabla, columns=columnas,
    show="headings", selectmode="browse")

tablaInventario.tag_configure("fila_clara", background=BLANCO, foreground=TEXTO)
tablaInventario.tag_configure("fila_otoñal", background=DURAZNO_CLARO, foreground=TEXTO)

anchos = {"ID": 55, "Nombre": 150, "Marca": 110, "Cantidad": 85,
    "Precio": 90, "Categoría": 150, "Unidad": 100}

for columna in columnas:
    tablaInventario.heading(columna, text=columna)
    tablaInventario.column(columna, width=anchos[columna],
        minwidth=50, anchor="center")

barraVertical = ttk.Scrollbar(panelTabla, orient="vertical",
    command=tablaInventario.yview)
barraHorizontal = ttk.Scrollbar(panelTabla, orient="horizontal",
    command=tablaInventario.xview)

tablaInventario.configure(
    yscrollcommand=barraVertical.set,
    xscrollcommand=barraHorizontal.set
)

tablaInventario.grid(row=0, column=0, sticky="nsew")
barraVertical.grid(row=0, column=1, sticky="ns")
barraHorizontal.grid(row=1, column=0, sticky="ew")
panelTabla.grid_rowconfigure(0, weight=1)
panelTabla.grid_columnconfigure(0, weight=1)

#PESTAÑA VENTAS
tituloVentas = Label(ventas, text="Punto de venta",
    font=("Arial", 18, "bold"), bg=FONDO, fg=CANELA)
tituloVentas.pack(pady=(8, 2))

mensajeVentas = Label(ventas,
    text="Selecciona un producto, indica la cantidad y agrégalo a la venta.",
    font=("Arial", 9), bg=FONDO, fg=TEXTO)
mensajeVentas.pack(pady=(0, 6))

#Panel para seleccionar productos
panelSeleccionVenta = Frame(ventas, bg=BLANCO)
panelSeleccionVenta.pack(fill="x", padx=12, pady=(0, 5))

Label(panelSeleccionVenta, text="Producto disponible",
    font=("Arial", 9, "bold"), bg=BLANCO, fg=TEXTO).grid(
    row=0, column=0, padx=10, pady=(5, 2), sticky="w")

comboProducto = ttk.Combobox(panelSeleccionVenta, state="readonly",
    width=65, font=("Arial", 9))
comboProducto.grid(row=1, column=0, padx=10, pady=(0, 5), sticky="ew")

Label(panelSeleccionVenta, text="Cantidad",
    font=("Arial", 9, "bold"), bg=BLANCO, fg=TEXTO).grid(
    row=0, column=1, padx=8, pady=(5, 2), sticky="w")

cuadroCantidadVenta = Entry(panelSeleccionVenta, font=("Arial", 9),
    width=9, bg=BLANCO, fg=TEXTO, relief="solid", bd=1)
cuadroCantidadVenta.grid(row=1, column=1, padx=8, pady=(0, 5), ipady=2)

panelSeleccionVenta.grid_columnconfigure(0, weight=1)

#Panel de productos de la venta
tituloCarrito = Label(ventas, text="Productos de la venta actual",
    font=("Arial", 12, "bold"), bg=FONDO, fg=CANELA)
tituloCarrito.pack(pady=(0, 3))

panelCarrito = Frame(ventas, bg=FONDO)
panelCarrito.pack(fill="both", expand=True, padx=12, pady=(0, 3))

columnasVenta = ("ID", "Nombre", "Cantidad", "Precio unitario", "Importe")
tablaVenta = ttk.Treeview(panelCarrito, columns=columnasVenta,
    show="headings", selectmode="browse", height=4)

anchosVenta = {
    "ID": 45, "Nombre": 200, "Cantidad": 75,
    "Precio unitario": 110, "Importe": 105
}

for columna in columnasVenta:
    tablaVenta.heading(columna, text=columna)
    tablaVenta.column(columna, width=anchosVenta[columna],
        minwidth=45, anchor="center")

barraVenta = ttk.Scrollbar(panelCarrito, orient="vertical",
    command=tablaVenta.yview)
tablaVenta.configure(yscrollcommand=barraVenta.set)
tablaVenta.grid(row=0, column=0, sticky="nsew")
barraVenta.grid(row=0, column=1, sticky="ns")
panelCarrito.grid_rowconfigure(0, weight=1)
panelCarrito.grid_columnconfigure(0, weight=1)

#Panel de botones de venta
panelBotonesVenta = Frame(ventas, bg=FONDO)
panelBotonesVenta.pack(fill="x", padx=12, pady=(0, 4))

#Panel de totales
panelTotales = Frame(ventas, bg=BLANCO)
panelTotales.pack(fill="x", padx=12, pady=(0, 5))

etiquetaSubtotal = Label(panelTotales, text="Subtotal: $0.00",
    font=("Arial", 10, "bold"), bg=BLANCO, fg=TEXTO)
etiquetaSubtotal.pack(anchor="e", padx=12, pady=(4, 1))

etiquetaIVA = Label(panelTotales, text="IVA (16 %): $0.00",
    font=("Arial", 10), bg=BLANCO, fg=TEXTO)
etiquetaIVA.pack(anchor="e", padx=12, pady=1)

etiquetaTotal = Label(panelTotales, text="Total: $0.00",
    font=("Arial", 12, "bold"), bg=BLANCO, fg=CANELA)
etiquetaTotal.pack(anchor="e", padx=12, pady=(1, 3))

#Panel para el pago en efectivo
panelPago = Frame(panelTotales, bg=BLANCO)
panelPago.pack(fill="x", padx=12, pady=(0, 5))

Label(panelPago, text="Efectivo recibido: $",
    font=("Arial", 9, "bold"), bg=BLANCO, fg=TEXTO).pack(side="left")

cuadroEfectivo = Entry(panelPago, font=("Arial", 9),
    width=12, bg=BLANCO, fg=TEXTO, relief="solid", bd=1)
cuadroEfectivo.pack(side="left", padx=(4, 8), ipady=2)

etiquetaCambio = Label(panelPago, text="Cambio: $0.00",
    font=("Arial", 10, "bold"), bg=BLANCO, fg=CANELA)
etiquetaCambio.pack(side="left", padx=4)

#FUNCIONES DEL INVENTARIO Y LAS VENTAS

#Actualizar las opciones de productos disponibles
def actualizarSelectorVentas():
    opciones = []

    for producto in productos:
        if producto["Cantidad"] > 0:
            opciones.append(
                f'{producto["ID"]} - {producto["Nombre"]} | '
                f'Unidad: {producto["Unidad"]} | '
                f'Existencia: {producto["Cantidad"]:g} | '
                f'${producto["Precio"]:,.2f}'
            )

    comboProducto["values"] = opciones

    if comboProducto.get() not in opciones:
        comboProducto.set("")

#Actualizar la tabla de inventario
def actualizarInventario():
    for fila in tablaInventario.get_children():
        tablaInventario.delete(fila)

    for indice, producto in enumerate(productos):
        colorFila = "fila_clara" if indice % 2 == 0 else "fila_otoñal"

        tablaInventario.insert("", END, values=(
            producto["ID"], producto["Nombre"], producto["Marca"],
            f'{producto["Cantidad"]:g}', f'${producto["Precio"]:,.2f}',
            producto["Categoría"], producto["Unidad"]
        ), tags=(colorFila,))

    actualizarSelectorVentas()

#Seleccionar un producto de la tabla del inventario
def seleccionarProducto(event=None):
    global productoSeleccionadoID

    seleccion = tablaInventario.selection()
    if not seleccion:
        return

    valores = tablaInventario.item(seleccion[0], "values")
    if not valores:
        return

    identificador = int(valores[0])

    for producto in productos:
        if producto["ID"] == identificador:
            productoSeleccionadoID = identificador

            cuadroID.configure(state="normal")
            cuadroID.delete(0, END)
            cuadroID.insert(0, producto["ID"])
            cuadroID.configure(state="readonly")

            cuadroNombre.delete(0, END)
            cuadroNombre.insert(0, producto["Nombre"])

            cuadroMarca.delete(0, END)
            cuadroMarca.insert(0, producto["Marca"])

            cuadroCantidad.delete(0, END)
            cuadroCantidad.insert(0, f'{producto["Cantidad"]:g}')

            cuadroPrecio.delete(0, END)
            cuadroPrecio.insert(0, f'{producto["Precio"]:g}')

            cuadroCategoria.set(producto["Categoría"])
            cuadroUnidad.set(producto["Unidad"])
            break

tablaInventario.bind("<<TreeviewSelect>>", seleccionarProducto)

#Limpiar el formulario
def limpiarCampos():
    global productoSeleccionadoID

    productoSeleccionadoID = None

    cuadroID.configure(state="normal")
    cuadroID.delete(0, END)
    cuadroID.configure(state="readonly")

    for campo in (cuadroNombre, cuadroMarca, cuadroCantidad, cuadroPrecio):
        campo.delete(0, END)

    cuadroCategoria.set("")
    cuadroUnidad.set("")

    seleccion = tablaInventario.selection()
    if seleccion:
        tablaInventario.selection_remove(*seleccion)

#Validar y obtener los datos del formulario
def obtenerDatosFormulario():
    nombre = cuadroNombre.get().strip()
    marca = cuadroMarca.get().strip()
    cantidadTexto = cuadroCantidad.get().strip()
    precioTexto = cuadroPrecio.get().strip()
    categoria = cuadroCategoria.get().strip()
    unidad = cuadroUnidad.get().strip()

    if not nombre or not cantidadTexto or not precioTexto or not categoria or not unidad:
        messagebox.showwarning(
            "Campos obligatorios",
            "Completa el nombre, la cantidad, el precio, la categoría y la unidad."
        )
        return None

    try:
        cantidad = float(cantidadTexto.replace(",", "."))
        precio = float(precioTexto.replace(",", "."))
    except ValueError:
        messagebox.showerror(
            "Datos inválidos",
            "La cantidad y el precio deben ser números válidos."
        )
        return None

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

    return {
        "Nombre": nombre,
        "Marca": marca,
        "Cantidad": cantidad,
        "Precio": precio,
        "Categoría": categoria,
        "Unidad": unidad
    }

#Registrar un producto nuevo
def registrarProducto():
    global siguienteID

    if productoSeleccionadoID is not None:
        messagebox.showwarning(
            "Producto seleccionado",
            "Estás editando un producto existente. Pulsa Guardar cambios o Limpiar campos antes de registrar otro."
        )
        return

    datos = obtenerDatosFormulario()
    if datos is None:
        return

    producto = {"ID": siguienteID, **datos}
    productos.append(producto)
    identificador = siguienteID
    siguienteID += 1

    actualizarInventario()

    messagebox.showinfo(
        "Producto registrado",
        f'El producto "{producto["Nombre"]}" se registró correctamente.\nID: {identificador}'
    )

    limpiarCampos()

#Guardar cambios de un producto existente
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

    for producto in productos:
        if producto["ID"] == productoSeleccionadoID:
            producto.update(datos)
            break
    else:
        messagebox.showerror(
            "Producto no encontrado",
            "No se encontró el producto que deseas modificar."
        )
        return

    actualizarInventario()
    limpiarCampos()

    messagebox.showinfo(
        "Cambios guardados",
        "El producto se actualizó correctamente."
    )

#Abrir Inicio para editar un producto
def irAEditar():
    if productoSeleccionadoID is None:
        messagebox.showwarning(
            "Selecciona un producto",
            "Primero selecciona un producto de la tabla."
        )
        return

    pestania.select(inicio)

#Eliminar un producto del inventario y reasignar los IDs
def eliminarProducto():
    global productoSeleccionadoID, siguienteID

    if productoSeleccionadoID is None:
        messagebox.showwarning(
            "Selecciona un producto",
            "Selecciona en la tabla el producto que deseas eliminar."
        )
        return

    productoEliminar = next(
        (p for p in productos if p["ID"] == productoSeleccionadoID),
        None
    )

    if productoEliminar is None:
        messagebox.showerror(
            "Producto no encontrado",
            "No se encontró el producto seleccionado."
        )
        return

    if productoEliminar["ID"] in carritoVentas:
        messagebox.showwarning(
            "Producto en venta",
            "No puedes eliminar un producto que está agregado a la venta actual."
        )
        return

    confirmar = messagebox.askyesno(
        "Confirmar eliminación",
        f'¿Seguro que deseas eliminar "{productoEliminar["Nombre"]}"?\n\n'
        "Los IDs restantes se reorganizarán automáticamente."
    )

    if not confirmar:
        return

    productos.remove(productoEliminar)

    nuevosIDs = {}

    for nuevoID, producto in enumerate(productos, start=1):
        IDanterior = producto["ID"]
        nuevosIDs[IDanterior] = nuevoID
        producto["ID"] = nuevoID

    carritoActualizado = {}

    for IDanterior, item in carritoVentas.items():
        nuevoID = nuevosIDs[IDanterior]
        item["ID"] = nuevoID
        carritoActualizado[nuevoID] = item

    carritoVentas.clear()
    carritoVentas.update(carritoActualizado)

    siguienteID = len(productos) + 1

    actualizarInventario()
    actualizarTablaVenta()
    limpiarCampos()

    messagebox.showinfo(
        "Producto eliminado",
        "El producto se eliminó correctamente y los IDs se reorganizaron."
    )

#Agregar un producto a la venta actual
def agregarProductoVenta():
    seleccion = comboProducto.get()

    if not seleccion:
        messagebox.showwarning(
            "Selecciona un producto",
            "Selecciona un producto disponible."
        )
        return

    try:
        identificador = int(seleccion.split(" - ", 1)[0])
        cantidad = float(cuadroCantidadVenta.get().strip().replace(",", "."))
    except ValueError:
        messagebox.showerror(
            "Datos inválidos",
            "Ingresa una cantidad numérica válida."
        )
        return

    if cantidad <= 0:
        messagebox.showwarning(
            "Cantidad inválida",
            "La cantidad debe ser mayor que cero."
        )
        return

    producto = next(
        (p for p in productos if p["ID"] == identificador),
        None
    )

    if producto is None:
        messagebox.showerror(
            "Producto no encontrado",
            "El producto ya no está disponible en el inventario."
        )
        actualizarSelectorVentas()
        return

    cantidadActual = carritoVentas.get(
        identificador, {}
    ).get("Cantidad", 0)

    if cantidadActual + cantidad > producto["Cantidad"]:
        messagebox.showwarning(
            "Existencias insuficientes",
            f'Hay {producto["Cantidad"]:g} unidades disponibles y ya agregaste {cantidadActual:g} a la venta.'
        )
        return

    if identificador in carritoVentas:
        carritoVentas[identificador]["Cantidad"] += cantidad
    else:
        carritoVentas[identificador] = {
            "ID": identificador,
            "Nombre": producto["Nombre"],
            "Cantidad": cantidad,
            "Precio": producto["Precio"],
            "Unidad": producto["Unidad"]
        }

    actualizarTablaVenta()
    cuadroCantidadVenta.delete(0, END)
    comboProducto.set("")

    cuadroEfectivo.delete(0, END)
    etiquetaCambio.config(text="Cambio: $0.00")

#Actualizar la tabla de la venta actual
def actualizarTablaVenta():
    for fila in tablaVenta.get_children():
        tablaVenta.delete(fila)

    subtotal = 0

    for identificador, item in carritoVentas.items():
        importe = item["Cantidad"] * item["Precio"]
        subtotal += importe

        tablaVenta.insert("", END, values=(
            item["ID"], item["Nombre"], f'{item["Cantidad"]:g}',
            f'${item["Precio"]:,.2f}', f'${importe:,.2f}'
        ))

    iva = subtotal * 0.16
    total = subtotal + iva

    etiquetaSubtotal.config(text=f"Subtotal: ${subtotal:,.2f}")
    etiquetaIVA.config(text=f"IVA (16 %): ${iva:,.2f}")
    etiquetaTotal.config(text=f"Total: ${total:,.2f}")

#Quitar un producto de la venta actual
def quitarProductoVenta():
    seleccion = tablaVenta.selection()

    if not seleccion:
        messagebox.showwarning(
            "Selecciona un producto",
            "Selecciona en la tabla el producto que deseas quitar."
        )
        return

    valores = tablaVenta.item(seleccion[0], "values")
    identificador = int(valores[0])

    if identificador in carritoVentas:
        del carritoVentas[identificador]

    actualizarTablaVenta()

    cuadroEfectivo.delete(0, END)
    etiquetaCambio.config(text="Cambio: $0.00")

#Crear el contenido de un ticket de venta
def generarTextoTicket(folio, fecha, articulos, subtotal, iva,
                       total, efectivo, cambio):
    ancho = 46
    lineas = []

    lineas.append("=" * ancho)
    lineas.append("JOHN'S FRESH".center(ancho))
    lineas.append("TICKET DE VENTA".center(ancho))
    lineas.append("=" * ancho)
    lineas.append(f"Folio: {folio:04d}")
    lineas.append(f"Fecha: {fecha}")
    lineas.append("-" * ancho)
    lineas.append("PRODUCTOS")
    lineas.append("-" * ancho)

    for item in articulos:
        nombre = item["Nombre"]
        cantidad = item["Cantidad"]
        precio = item["Precio"]
        importe = cantidad * precio
        unidad = item.get("Unidad", "Unidades")

        lineas.append(nombre[:ancho])
        lineas.append(
            f"  {cantidad:g} {unidad} x ${precio:,.2f}"
        )
        lineas.append(f"  Importe: ${importe:,.2f}")

    lineas.append("-" * ancho)
    lineas.append(f"{'Subtotal:':<28}${subtotal:>15,.2f}")
    lineas.append(f"{'IVA (16 %):':<28}${iva:>15,.2f}")
    lineas.append("=" * ancho)
    lineas.append(f"{'TOTAL:':<28}${total:>15,.2f}")
    lineas.append("=" * ancho)
    lineas.append(f"{'Efectivo recibido:':<28}${efectivo:>15,.2f}")
    lineas.append(f"{'Cambio:':<28}${cambio:>15,.2f}")
    lineas.append("=" * ancho)
    lineas.append("¡Gracias por comprar en".center(ancho))
    lineas.append("John's Fresh!".center(ancho))
    lineas.append("=" * ancho)

    return "\n".join(lineas)

#Guardar el ticket como archivo de texto
def guardarTicket(textoTicket, folio):
    ruta = filedialog.asksaveasfilename(
        parent=ventanaTicket,
        title="Guardar ticket de venta",
        initialfile=f"Ticket_JohnsFresh_{folio:04d}.txt",
        defaultextension=".txt",
        filetypes=[("Archivo de texto", "*.txt")]
    )

    if not ruta:
        return

    try:
        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write(textoTicket)

        messagebox.showinfo(
            "Ticket guardado",
            f"El ticket se guardó correctamente en:\n{ruta}",
            parent=ventanaTicket
        )
    except OSError as error:
        messagebox.showerror(
            "Error al guardar",
            f"No fue posible guardar el ticket.\n\n{error}",
            parent=ventanaTicket
        )

#Mostrar el ticket en una ventana independiente
def mostrarTicket(textoTicket, folio):
    global ventanaTicket

    ventanaTicket = Toplevel(raiz)
    ventanaTicket.title(f"Ticket de venta - Folio {folio:04d}")
    ventanaTicket.geometry("460x650")
    ventanaTicket.minsize(400, 500)
    ventanaTicket.configure(bg=FONDO)
    ventanaTicket.transient(raiz)

    try:
        ventanaTicket.iconbitmap("Logo_JF_pequenio.ico")
    except TclError:
        pass

    tituloTicket = Label(
        ventanaTicket,
        text="Venta finalizada correctamente",
        font=("Arial", 14, "bold"),
        bg=FONDO,
        fg=CANELA
    )
    tituloTicket.pack(pady=(12, 6))

    mensajeTicket = Label(
        ventanaTicket,
        text="Puedes revisar el ticket y guardarlo como archivo de texto.",
        font=("Arial", 9),
        bg=FONDO,
        fg=TEXTO,
        wraplength=420
    )
    mensajeTicket.pack(pady=(0, 8))

    panelTextoTicket = Frame(ventanaTicket, bg=BLANCO)
    panelTextoTicket.pack(fill="both", expand=True, padx=15, pady=5)

    barraTicket = ttk.Scrollbar(panelTextoTicket, orient="vertical")
    textoTicketUI = Text(
        panelTextoTicket,
        wrap="none",
        font=("Courier New", 10),
        bg=BLANCO,
        fg=TEXTO,
        relief="flat",
        padx=10,
        pady=10,
        width=46,
        height=25
    )

    barraTicket.config(command=textoTicketUI.yview)
    textoTicketUI.configure(yscrollcommand=barraTicket.set)

    textoTicketUI.pack(side="left", fill="both", expand=True)
    barraTicket.pack(side="right", fill="y")

    textoTicketUI.insert("1.0", textoTicket)
    textoTicketUI.configure(state="disabled")

    panelBotonesTicket = Frame(ventanaTicket, bg=FONDO)
    panelBotonesTicket.pack(fill="x", padx=15, pady=(6, 12))

    botonGuardarTicket = Button(
        panelBotonesTicket,
        text="Guardar ticket",
        command=lambda: guardarTicket(textoTicket, folio),
        font=("Arial", 10, "bold"),
        bg=CANELA,
        fg=BLANCO,
        activebackground=TERRACOTA,
        activeforeground=BLANCO,
        relief="flat",
        cursor="hand2"
    )
    botonGuardarTicket.pack(side="left", expand=True, fill="x",
                            padx=(0, 5), ipady=5)

    botonCerrarTicket = Button(
        panelBotonesTicket,
        text="Cerrar",
        command=ventanaTicket.destroy,
        font=("Arial", 10, "bold"),
        bg=DURAZNO,
        fg=TEXTO,
        activebackground=DURAZNO_CLARO,
        relief="flat",
        cursor="hand2"
    )
    botonCerrarTicket.pack(side="left", expand=True, fill="x",
                           padx=(5, 0), ipady=5)

    ventanaTicket.grab_set()

#Finalizar la venta, generar el ticket y descontar existencias
def finalizarVenta():
    global siguienteFolio

    if not carritoVentas:
        messagebox.showwarning(
            "Venta vacía",
            "Agrega al menos un producto antes de finalizar la venta."
        )
        return

    #Verificar todas las existencias antes de descontar cualquier cantidad
    for identificador, item in carritoVentas.items():
        producto = next(
            (p for p in productos if p["ID"] == identificador),
            None
        )

        if producto is None:
            messagebox.showerror(
                "Producto no encontrado",
                f'El producto "{item["Nombre"]}" ya no existe en el inventario.'
            )
            return

        if item["Cantidad"] > producto["Cantidad"]:
            messagebox.showwarning(
                "Existencias insuficientes",
                f'Ya no hay suficientes unidades de "{producto["Nombre"]}". Actualiza la venta antes de continuar.'
            )
            return

    #Calcular subtotal, IVA y total
    subtotal = sum(
        item["Cantidad"] * item["Precio"]
        for item in carritoVentas.values()
    )

    iva = subtotal * 0.16
    total = subtotal + iva

    #Validar el dinero recibido en efectivo
    efectivoTexto = cuadroEfectivo.get().strip().replace(",", ".")

    if not efectivoTexto:
        messagebox.showwarning(
            "Falta el pago",
            "Ingresa el efectivo recibido del cliente."
        )
        cuadroEfectivo.focus_set()
        return

    try:
        efectivo = float(efectivoTexto)
    except ValueError:
        messagebox.showerror(
            "Pago inválido",
            "Ingresa una cantidad de efectivo válida."
        )
        cuadroEfectivo.focus_set()
        return

    if efectivo < 0:
        messagebox.showwarning(
            "Pago inválido",
            "El efectivo recibido no puede ser negativo."
        )
        return

    if efectivo < total:
        messagebox.showwarning(
            "Efectivo insuficiente",
            f'El total es ${total:,.2f} y el cliente entregó ${efectivo:,.2f}.\n'
            f'Faltan ${total - efectivo:,.2f}.'
        )
        return

    cambio = efectivo - total
    etiquetaCambio.config(text=f"Cambio: ${cambio:,.2f}")

    #Confirmar la venta antes de descontar existencias
    confirmar = messagebox.askyesno(
        "Finalizar venta",
        f"Subtotal: ${subtotal:,.2f}\n"
        f"IVA (16 %): ${iva:,.2f}\n"
        f"Total: ${total:,.2f}\n\n"
        f"Efectivo recibido: ${efectivo:,.2f}\n"
        f"Cambio: ${cambio:,.2f}\n\n"
        "¿Deseas confirmar la venta?"
    )

    if not confirmar:
        return

    #Conservar una copia de los artículos antes de limpiar el carrito
    articulosTicket = [
        {
            "ID": item["ID"],
            "Nombre": item["Nombre"],
            "Cantidad": item["Cantidad"],
            "Precio": item["Precio"],
            "Unidad": item.get(
                "Unidad",
                next(
                    (p["Unidad"] for p in productos
                     if p["ID"] == identificador),
                    "Unidades"
                )
            )
        }
        for identificador, item in carritoVentas.items()
    ]

    folio = siguienteFolio
    fecha = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    textoTicket = generarTextoTicket(
        folio,
        fecha,
        articulosTicket,
        subtotal,
        iva,
        total,
        efectivo,
        cambio
    )

    #Descontar existencias solamente al confirmar
    for identificador, item in carritoVentas.items():
        producto = next(
            p for p in productos if p["ID"] == identificador
        )
        producto["Cantidad"] -= item["Cantidad"]

    #Preparar la siguiente venta
    carritoVentas.clear()
    actualizarTablaVenta()
    actualizarInventario()

    cuadroCantidadVenta.delete(0, END)
    comboProducto.set("")
    cuadroEfectivo.delete(0, END)
    etiquetaCambio.config(text="Cambio: $0.00")

    siguienteFolio += 1

    #Mostrar el ticket generado
    mostrarTicket(textoTicket, folio)

#BOTONES DE INICIO
botonRegistrar = Button(panelFormulario, text="Registrar producto",
    command=registrarProducto, font=("Arial", 10, "bold"),
    bg=CANELA, fg=BLANCO, activebackground=TERRACOTA,
    activeforeground=BLANCO, relief="flat", cursor="hand2")
botonRegistrar.pack(fill="x", padx=25, pady=(8, 3), ipady=4)

botonGuardar = Button(panelFormulario, text="Guardar cambios",
    command=guardarCambios, font=("Arial", 10, "bold"),
    bg=TERRACOTA, fg=BLANCO, activebackground=CANELA,
    activeforeground=BLANCO, relief="flat", cursor="hand2")
botonGuardar.pack(fill="x", padx=25, pady=3, ipady=4)

botonLimpiar = Button(panelFormulario, text="Limpiar campos",
    command=limpiarCampos, font=("Arial", 10, "bold"),
    bg=DURAZNO, fg=TEXTO, activebackground=DURAZNO_CLARO,
    activeforeground=TEXTO, relief="flat", cursor="hand2")
botonLimpiar.pack(fill="x", padx=25, pady=(3, 10), ipady=4)

#BOTONES DEL INVENTARIO
panelBotonesInventario = Frame(inventario, bg=FONDO)
panelBotonesInventario.pack(fill="x", padx=15, pady=(0, 10))

botonEditar = Button(panelBotonesInventario, text="Editar en Inicio",
    command=irAEditar, font=("Arial", 10, "bold"),
    bg=CANELA, fg=BLANCO, activebackground=TERRACOTA,
    activeforeground=BLANCO, relief="flat", cursor="hand2")
botonEditar.pack(side="left", padx=(0, 8), ipady=5, ipadx=8)

botonEliminar = Button(panelBotonesInventario, text="Eliminar producto",
    command=eliminarProducto, font=("Arial", 10, "bold"),
    bg=ROJO, fg=BLANCO, activebackground="#82332B",
    activeforeground=BLANCO, relief="flat", cursor="hand2")
botonEliminar.pack(side="left", padx=8, ipady=5, ipadx=8)

#BOTONES DE VENTAS
botonAgregarVenta = Button(panelSeleccionVenta, text="Agregar a venta",
    command=agregarProductoVenta, font=("Arial", 9, "bold"),
    bg=CANELA, fg=BLANCO, activebackground=TERRACOTA,
    activeforeground=BLANCO, relief="flat", cursor="hand2")
botonAgregarVenta.grid(row=1, column=2, padx=8, pady=(0, 5), ipady=3)

botonQuitarVenta = Button(panelBotonesVenta, text="Quitar producto",
    command=quitarProductoVenta, font=("Arial", 9, "bold"),
    bg=DURAZNO, fg=TEXTO, activebackground=DURAZNO_CLARO,
    relief="flat", cursor="hand2")
botonQuitarVenta.pack(side="left", padx=(0, 8), ipady=4, ipadx=8)

botonFinalizarVenta = Button(panelBotonesVenta, text="Finalizar venta",
    command=finalizarVenta, font=("Arial", 9, "bold"),
    bg=CANELA, fg=BLANCO, activebackground=TERRACOTA,
    activeforeground=BLANCO, relief="flat", cursor="hand2")
botonFinalizarVenta.pack(side="right", padx=8, ipady=4, ipadx=8)

#PESTAÑA CLIENTES
tituloClientes = Label(clientes, text="Clientes",
    font=("Arial", 20, "bold"), bg=FONDO, fg=CANELA)
tituloClientes.pack(pady=(35, 8))

mensajeClientes = Label(clientes,
    text="Aquí construiremos el registro y la gestión de clientes.",
    font=("Arial", 10), bg=FONDO, fg=TEXTO)
mensajeClientes.pack(pady=5)

#Cargar los productos iniciales en el inventario y en el selector de ventas
actualizarInventario()
actualizarTablaVenta()

#Inicio del programa
raiz.mainloop()
