from tkinter import *
import Main
import Base
import os

# comprobar la existencia de bases de datos
if os.path.isfile("./DataCenter"):
    # print("file_found") no es visible sin consola
    pass
else:
    Base.create()

if os.path.isfile("./users"):
    # print("file_found") no es visible sin consola
    pass
else:
    Base.createOnce()



# clase iniciando
class root:
    # función de los botones
    def codigoBoton(self):
        datos = []
        DatosEnBase = Base.OnlyRead()
        for i in DatosEnBase:
            datos.append(i)
        if ((self.User.get() == datos[0][1]) and (self.Pass.get() == datos[0][2])):
            self.destroy()
            Main.IniciarAlpha()
        elif ((self.User.get() == datos[1][1]) and (self.Pass.get() == datos[1][2])):
            self.destroy()
            Main.IniciarBeta()
        elif ((self.User.get() == datos[2][1]) and (self.Pass.get() == datos[2][2])):
            self.destroy()
            Main.IniciarGamma()
        else:
            print("\a") # sonido del sistema
            self.User.delete(0, END) # vaciamos la entrada
            self.Pass.delete(0, END) # vaciamos la entrada

    def exit(self):
        self.destroy()


    def __init__(self, base):
        # raiz
        self = base
        self.eval('tk::PlaceWindow . center') # centrar la ventana
        self.iconbitmap("./res/Logo.ico") # cambiar icono
        self.overrideredirect(True) # ocultar los bordes
        self.attributes('-alpha', 0.9) # transparencia
        #self.wm_attributes('-transparentcolor','white')

        # Frame Principal
        MainFrame = Frame(self)
        MainFrame.grid(row=0,column=0)

        # Clase Imagen
        self.imagen = PhotoImage(file="./res/images.png")

        # Cuadro de Texto del Titulo
        Titulo = Label(MainFrame, text="Iniciar Sesión", font=("Arial",36))
        Titulo.grid(row=0,column=1,columnspan=2)

        # Apartado del Logo
        self.Logo = Label(MainFrame, image=self.imagen)
        self.Logo.grid(row=0,column=0,rowspan=3)

        # Cuadro de Texto Para el Usuario
        Label(MainFrame, text="Usuario: ").grid(row=1,column=1)
        self.User = Entry(MainFrame)
        self.User.grid(row=1,column=2)

        # Cuadro de Texto Para la Contraseña
        Label(MainFrame, text="Contraseña: ").grid(row=2,column=1)
        self.Pass = Entry(MainFrame)
        self.Pass.grid(row=2,column=2)
        self.Pass.config(show="·")

        ContinuarBoton = Button(MainFrame, text="Iniciar", command=lambda:root.codigoBoton(self))
        ContinuarBoton.grid(row=3,column=1, columnspan = 3)

        SalirBoton = Button(MainFrame, text="Salir", command=lambda:root.exit(self))
        SalirBoton.grid(row=3,column=2, columnspan = 3)

# comprobar la clase para ejecutar el programa
if __name__ == '__main__':
    base = Tk()
    root(base) # instanciamos la clase root
    base.mainloop()
