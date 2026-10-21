
from tkinter import *
from tkinter import ttk  #Importa componentes de Tkinter con estilos modernos
#Importa ventanas emergentes para mostrar mensajes, advertencias y errores
from tkinter import messagebox

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
siguienteID = 1

#Configuración de la ventana principal
raiz = Tk()
raiz.title("John's Fresh - Sistema de punto de venta")
raiz.geometry("1050x750")
raiz.minsize(900, 650)
raiz.configure(bg=CREMA)

try:
    raiz.iconbitmap("Logo_JF_pequenio.ico")
except TclError:
    pass

#Configuración del estilo de las pestañas
estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure("TNotebook", background=CREMA, borderwidth=0)
estilo.configure("TNotebook.Tab", background=DURAZNO, foreground=TEXTO, padding=[18, 10], font=("Arial", 10, "bold"))
estilo.map("TNotebook.Tab", background=[("selected", CANELA)], foreground=[("selected", BLANCO)])

#Título principal
titulo = Label(raiz, text="JOHN'S FRESH", font=("Arial", 24, "bold"), bg=CREMA, fg=CANELA)
titulo.pack(pady=(12, 3))

subtitulo = Label(raiz, text="Sistema de punto de venta e inventario", font=("Arial", 11), bg=CREMA, fg=TEXTO)
subtitulo.pack(pady=(0, 10))

#Creación del contenedor de pestañas
pestania = ttk.Notebook(raiz)
pestania.pack(fill="both", expand=True, padx=20, pady=(0, 15))

#Creación de las pestañas
inicio = Frame(pestania, bg=CREMA)
inventario = Frame(pestania, bg=CREMA)
ventas = Frame(pestania, bg=CREMA)
clientes = Frame(pestania, bg=CREMA)

pestania.add(inicio, text="Inicio")
pestania.add(inventario, text="Inventario")
pestania.add(ventas, text="Ventas")
pestania.add(clientes, text="Clientes")

#Diseño de la pestaña Inicio
panelLogo = Frame(inicio, bg=CREMA)
panelLogo.pack(side="left", fill="both", expand=True, padx=(15, 8), pady=10)

panelFormulario = Frame(inicio, bg=BLANCO)
panelFormulario.pack(side="right", fill="both", expand=True, padx=(8, 15), pady=10)

#Carga del logo
try:
    logo = PhotoImage(file="Logo_JF_grande.png").subsample(3, 3)
    etiquetaLogo = Label(panelLogo, image=logo, bg=CREMA, bd=0)
    etiquetaLogo.image = logo
    etiquetaLogo.pack(expand=True)
except TclError:
    etiquetaLogo = Label(panelLogo, text="JOHN'S FRESH", font=("Arial", 26, "bold"), bg=CREMA, fg=CANELA)
    etiquetaLogo.pack(expand=True)

#Título del formulario
tituloFormulario = Label(panelFormulario, text="Registro de productos", font=("Arial", 17, "bold"), bg=BLANCO, fg=CANELA)
tituloFormulario.pack(pady=(12, 8))

#Función para crear las etiquetas del formulario
def crearEtiqueta(texto):
    return Label(panelFormulario, text=texto, font=("Arial", 10, "bold"), bg=BLANCO, fg=TEXTO)

#Función para crear los campos del formulario
def crearCampo():
    return Entry(panelFormulario, font=("Arial", 10), bg=BLANCO, fg=TEXTO, relief="solid", bd=1, highlightbackground=BORDE)

#Campo de ID
crearEtiqueta("ID del producto").pack(anchor="w", padx=30, pady=(3, 2))
cuadroID = crearCampo()
cuadroID.pack(fill="x", padx=30, ipady=4)
cuadroID.config(state="readonly")

#Campo de nombre
crearEtiqueta("Nombre del producto *").pack(anchor="w", padx=30, pady=(6, 2))
cuadroNombre = crearCampo()
cuadroNombre.pack(fill="x", padx=30, ipady=4)

#Campo de marca
crearEtiqueta("Marca").pack(anchor="w", padx=30, pady=(6, 2))
cuadroMarca = crearCampo()
cuadroMarca.pack(fill="x", padx=30, ipady=4)

#Campo de cantidad
crearEtiqueta("Cantidad *").pack(anchor="w", padx=30, pady=(6, 2))
cuadroCantidad = crearCampo()
cuadroCantidad.pack(fill="x", padx=30, ipady=4)

#Campo de precio
crearEtiqueta("Precio unitario *").pack(anchor="w", padx=30, pady=(6, 2))
cuadroPrecio = crearCampo()
cuadroPrecio.pack(fill="x", padx=30, ipady=4)

#Campo de categoría
crearEtiqueta("Categoría").pack(anchor="w", padx=30, pady=(6, 2))
cuadroCategoria = crearCampo()
cuadroCategoria.pack(fill="x", padx=30, ipady=4)

#Campo de unidad
crearEtiqueta("Unidad de medida *").pack(anchor="w", padx=30, pady=(6, 2))
cuadroUnidad = crearCampo()
cuadroUnidad.pack(fill="x", padx=30, ipady=4)

#Función para limpiar los campos
def limpiarCampos():
    cuadroID.config(state="normal")
    cuadroID.delete(0, END)
    cuadroID.config(state="readonly")

    for cuadro in [cuadroNombre, cuadroMarca, cuadroCantidad, cuadroPrecio, cuadroCategoria, cuadroUnidad]:
        cuadro.delete(0, END)

#Función para registrar un producto
def registrarProducto():
    global siguienteID

    nombre = cuadroNombre.get().strip()
    marca = cuadroMarca.get().strip()
    cantidadTexto = cuadroCantidad.get().strip().replace(",", ".")
    precioTexto = cuadroPrecio.get().strip().replace(",", ".")
    categoria = cuadroCategoria.get().strip()
    unidad = cuadroUnidad.get().strip()

    #Validar campos obligatorios
    if not nombre or not cantidadTexto or not precioTexto or not unidad:
        messagebox.showwarning("Campos incompletos", "Completa el nombre, la cantidad, el precio y la unidad de medida.")
        return

    #Validar que cantidad y precio sean números
    try:
        cantidad = float(cantidadTexto)
        precio = float(precioTexto)
    except ValueError:
        messagebox.showerror("Datos incorrectos", "La cantidad y el precio deben ser valores numéricos.")
        return

    #Validar valores permitidos
    if cantidad <= 0:
        messagebox.showwarning("Cantidad incorrecta", "La cantidad debe ser mayor que cero.")
        return

    if precio < 0:
        messagebox.showwarning("Precio incorrecto", "El precio no puede ser negativo.")
        return

    #Asignar ID y crear el producto
    identificador = siguienteID

    producto = {
        "ID": identificador,
        "Nombre": nombre,
        "Marca": marca,
        "Cantidad": cantidad,
        "Precio": precio,
        "Categoría": categoria,
        "Unidad": unidad
    }

    #Guardar el producto en la lista temporal
    productos.append(producto)

    #Actualizar el siguiente ID disponible
    siguienteID += 1

    #Mostrar el ID asignado
    cuadroID.config(state="normal")
    cuadroID.delete(0, END)
    cuadroID.insert(0, identificador)
    cuadroID.config(state="readonly")

    messagebox.showinfo("Registro exitoso", f"El producto '{nombre}' se registró correctamente.\nID asignado: {identificador}")

    limpiarCampos()

#Botones del formulario
panelBotones = Frame(panelFormulario, bg=BLANCO)
panelBotones.pack(pady=12)

botonRegistrar = Button(panelBotones, text="Registrar producto", command=registrarProducto, bg=CANELA, fg=BLANCO, activebackground=TERRACOTA, activeforeground=BLANCO, font=("Arial", 10, "bold"), relief="flat", cursor="hand2", padx=12, pady=8)
botonRegistrar.pack(side="left", padx=5)

botonLimpiar = Button(panelBotones, text="Limpiar campos", command=limpiarCampos, bg=DURAZNO, fg=TEXTO, activebackground=TERRACOTA, activeforeground=BLANCO, font=("Arial", 10, "bold"), relief="flat", cursor="hand2", padx=12, pady=8)
botonLimpiar.pack(side="left", padx=5)

#Diseño de la pestaña Inventario
tituloInventario = Label(inventario, text="Inventario de productos", font=("Arial", 18, "bold"), bg=CREMA, fg=CANELA)
tituloInventario.pack(pady=30)

mensajeInventario = Label(inventario, text="Aquí se mostrará la tabla de productos registrados.", font=("Arial", 11), bg=CREMA, fg=TEXTO)
mensajeInventario.pack(pady=10)

#Diseño de la pestaña Ventas
tituloVentas = Label(ventas, text="Registro de ventas", font=("Arial", 18, "bold"), bg=CREMA, fg=CANELA)
tituloVentas.pack(pady=30)

mensajeVentas = Label(ventas, text="Aquí se realizará la selección de productos y el cálculo de las ventas.", font=("Arial", 11), bg=CREMA, fg=TEXTO)
mensajeVentas.pack(pady=10)

#Diseño de la pestaña Clientes
tituloClientes = Label(clientes, text="Registro de clientes", font=("Arial", 18, "bold"), bg=CREMA, fg=CANELA)
tituloClientes.pack(pady=30)

mensajeClientes = Label(clientes, text="Aquí se registrará la información de los clientes.", font=("Arial", 11), bg=CREMA, fg=TEXTO)
mensajeClientes.pack(pady=10)

#Iniciar la aplicación
raiz.mainloop()
