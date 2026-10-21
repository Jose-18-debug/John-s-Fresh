
from tkinter import *

raiz = Tk()
raiz.title("John's Fresh")
raiz.iconbitmap("Logo_JF_pequenio.ico")
raiz.config(bg="Gold")
raiz.config(bd=20, relief="sunken", cursor="hand2")

miFrame = Frame(raiz, bg="red", bd=10)
miFrame.pack(fill="both", expand=True, padx=10, pady=10)

# Titulo de bienvenida
miLabel = Label(
    miFrame,
    text="¡Bienvenidos a la Abarrotería de John!",
    fg="red",
    font=("Comic Sans MS", 15),
    bg="red"
)
miLabel.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Cuadros de texto
cuadroNombre = Entry(miFrame)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)

cuadroPass = Entry(miFrame, show="*")
cuadroPass.grid(row=2, column=1, padx=10, pady=10)

cuadroApellido = Entry(miFrame)
cuadroApellido.grid(row=3, column=1, padx=10, pady=10)

cuadroDireccion = Entry(miFrame)
cuadroDireccion.grid(row=4, column=1, padx=10, pady=10)

# Etiquetas
nombreLabel = Label(miFrame, text="Nombre:", bg="red")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

passLabel = Label(miFrame, text="Contraseña:", bg="red")
passLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

apellidoLabel = Label(miFrame, text="Apellido:", bg="red")
apellidoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel = Label(miFrame, text="Dirección:", bg="red")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

raiz.mainloop()
