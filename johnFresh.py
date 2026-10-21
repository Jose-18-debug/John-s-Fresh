from tkinter import *

raiz = Tk()
raiz.title("John's Fresh")
# raiz.resizable(True, False)
raiz.iconbitmap("Logo_JF_pequenio.ico")
# raiz.geometry("650x350")
raiz.config(bg = "Gold")
raiz.config(bd = 20, relief = "sunken", cursor = "hand2")

miFrame = Frame()
miFrame.pack(fill = "x")
miFrame.config(bg = "red")
miFrame.config(width = "650", height = "350", bd = 35,
               relief = "sunken", cursor = "pirate")

raiz.mainloop()