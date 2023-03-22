from tkinter import ttk # biblioteca para botones
from tkinter import * # todas las clases y variables de tkinter
from tkinter import messagebox # biblioteca para ventanas emergentes
from tkinter import scrolledtext # biblioteca para textos

import Base

def lecturaUsuariosBorrar(obj,texto):
    j = []
    valores = Base.OnlyRead()
    for i in valores:
        j.append(i)
    if texto == j[0][2]:
        obj.BorrarProd()
        obj.Volatil.destroy()
    else:
        print("\a")
        obj.Volatil.destroy()
        obj.Mensaje['fg'] = 'red'
        obj.Mensaje['text'] = 'Contraseña incorrecta'

def lecturaUsuariosBorrar(obj,texto):
    j = []
    valores = Base.OnlyRead()
    for i in valores:
        j.append(i)
    if texto == j[0][2]:
        obj.BorrarProd()
        obj.Volatil.destroy()
    else:
        print("\a")
        obj.Volatil.destroy()
        obj.Mensaje['fg'] = 'red'
        obj.Mensaje['text'] = 'Contraseña incorrecta'

def lecturaUsuariosEditar(obj,texto):
    j = []
    valores = Base.OnlyRead()
    for i in valores:
        j.append(i)
    if texto == j[0][2]:
        obj.EditarProd()
        obj.Volatil.destroy()
    else:
        print("\a")
        obj.Volatil.destroy()
        obj.Mensaje['fg'] = 'red'
        obj.Mensaje['text'] = 'Contraseña incorrecta'

def PermisoAdministrador(objeto):
    objeto.Volatil = Toplevel()
    objeto.Volatil.title = "Permisos Insuficientes"
    objeto.Volatil.resizable(0, 0)
    Label(objeto.Volatil, text = "Ingresa la contraseña de administrador: ").grid(row = 0, column = 0)
    objeto.permiso = Entry(objeto.Volatil)
    objeto.permiso.grid(row = 0, column = 1, columnspan = 2)
    objeto.permiso.config(show="·")
    Button(objeto.Volatil,  text = "Continuar",  command = lambda:lecturaUsuariosBorrar(objeto,objeto.permiso.get())).grid(row = 1, column = 0, columnspan = 3)

def PermisoAdministradorEdicion(objeto):
    objeto.Volatil = Toplevel()
    objeto.Volatil.title = "Permisos Insuficientes"
    objeto.Volatil.resizable(0, 0)
    Label(objeto.Volatil, text = "Ingresa la contraseña de administrador: ").grid(row = 0, column = 0)
    objeto.permiso = Entry(objeto.Volatil)
    objeto.permiso.grid(row = 0, column = 1, columnspan = 2)
    objeto.permiso.config(show="·")
    Button(objeto.Volatil,  text = "Continuar",  command = lambda:lecturaUsuariosEditar(objeto,objeto.permiso.get())).grid(row = 1, column = 0, columnspan = 3)

class Alpha:
    def copy(self):
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Selecciona un dato'
            return
        self.Mensaje['text'] = ''
        nombre = self.tabla.item(self.tabla.selection())['text']
        precio = self.tabla.item(self.tabla.selection())['values'][0]
        portapapeles = nombre + " " + str(precio)
        texto = scrolledtext.ScrolledText(self.wind) # creamos la variable de tkinter para mandar al portapapeles
        texto.clipboard_clear() # limpiamos el portapapeles
        texto.clipboard_append(portapapeles) # guardamos el texto en el portapapeles

    def cut(self):
        self.copy() # se copia al portapapeles el valor seleccionado
        self.BorrarProd() # se borra el valor seleccionado

    def hidalgo(self): # paste pegar
        self.Mensaje['text'] = '' # vaciamos los mensajes anteriores
        texto = scrolledtext.ScrolledText(self.wind) # creamos la variable de tkinter para mandar al portapapeles
        try:
            texto.clipboard_get() # guardamos el texto en el portapapeles
        except IndexError as e:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Copia un dato con el formato "precio valor"'
            return
        portapapeles = texto.clipboard_get()
        nombre = ""
        precio = ""
        for i in portapapeles:
            if i.isdigit():
                precio = precio + i
            elif(i == "."):
                precio = precio + i
            elif(i == " "):
                nombre = nombre
            else:
                nombre = nombre + i
        parametro = (nombre, precio)
        Base.add(parametro)
        self.LlenarArbol()

    def advice(self, texto): # funcion consejo
        if len(texto):
            texto = texto + '.txt'
            archive = open(texto, 'w')
            residual = Base.read()
            for i in residual:
                for j in i:
                    archive.writelines(str(j)+" ")
                archive.writelines("\n")
            archive.close()
            self.saving.destroy()
            self.Mensaje['text'] = ''
        else:
            print("\a")
            self.saving.destroy()
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Datos Faltantes'

    def save(self): # funcion guardar en otro archivo
        self.saving = Toplevel()
        self.saving.title = "Guardar en archivo externo"
        Label(self.saving, text = "Ingresa el nombre del archivo a crear: ").grid(row = 0, column = 0)
        self.guardar = Entry(self.saving)
        self.guardar.grid(row = 0, column = 1, columnspan = 2)
        Button(self.saving,  text = "Guardar",  command = lambda:self.advice(self.guardar.get())).grid(row = 1, column = 0, columnspan = 3)

    def info(self): # informacion del programa
        messagebox.showinfo('Gestor Universal', 'Proyecto Final de Estructuras de Datos y Algoritmos 1\n\nHecho por:\n\n\t Fernando Arciga Guzmán\n\tÁngel David Valenzuela Vigil\n\nAsesorados por: Marco Antonio Martínez Quintana')

    def guarninguser(self, todo, N): # advertencia de cambio de usuario (n = nombre anterior,  N = nombre nuevo)
        valor = messagebox.askokcancel('Gestor Universal', ('¿Realmente deseas cambiar el usuario {} por {}?').format(todo[1], N))
        if valor:
            self.nameedit.destroy()
            Base.Cambio_InicioSesion("user", (N, todo[1], todo[2])) # el primer valor es el tipo de cambio
            self.Mensaje['fg'] = 'green'
            self.Mensaje['text'] = 'Usuario cambiado con éxito'

    def guarningcontra(self, todo, N): # advertencia de cambio de contraseña (n = contraseña anterior,  N =  nueva contraseña)
        valor = messagebox.askokcancel('Gestor Universal', ('¿Realmente deseas cambiar la contraseña {} por {}?').format(todo[2], N))
        if valor:
            Base.Cambio_InicioSesion("con", (N, todo[1], todo[2])) # el primer valor es el tipo de cambio
            self.conedit.destroy()
            self.Mensaje['fg'] = 'green'
            self.Mensaje['text'] = 'Contraseña cambiada con éxito'

    def guarningGeneral(self,n,c,N,C):
        if n and c and N and C:
            j = []
            valores = Base.OnlyRead()
            for i in valores:
                j.append(i)
            for valores in j:
                if n == valores[1]:
                    if c == valores[2]:
                        Base.Cambio_InicioSesion("kami",[C,N,n,c])
                        self.nameedit.destroy()
                        self.Mensaje['fg'] = 'green'
                        self.Mensaje['text'] = ('Actualizado el usuario ' + n.title() + " correctamente")
                    else:
                        print("\a")
                        self.nameedit.destroy()
                        self.Mensaje['fg'] = 'red'
                        self.Mensaje['text'] = 'Datos Erroneos'
        else:
            print("\a")
            self.nameedit.destroy()
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Datos Faltantes'
        self.nameedit.destroy()

    def exit(self): # salir con el boton en casacada
        valor = messagebox.askquestion("Saliendo",  "¿Realmente deseas salir?")
        if valor == "yes":
            self.wind.destroy() # termina el programa

    def JoanSebastian(self):
        self.nameedit = Toplevel() # ventana encima de la anterior
        self.nameedit.title = "Edición de cuentas globales" # titulo de la ventana

        # nombre anterior
        Label(self.nameedit, text = "Nombre Actual").grid(row = 0, column = 1)
        NombreAnterior = Entry(self.nameedit)
        NombreAnterior.grid(row = 0, column = 2)
        NombreAnterior.config(show="·")

        # nuevo nombre
        Label(self.nameedit, text = 'Nuevo Nombre').grid(row = 1, column = 1)
        nuevoNombre = Entry(self.nameedit)
        nuevoNombre.grid(row = 1, column = 2)
        nuevoNombre.config(show="·")

        # nombre anterior
        Label(self.nameedit, text = "Contraseña Actual").grid(row = 2, column = 1)
        ContraseñaActual = Entry(self.nameedit)
        ContraseñaActual.grid(row = 2, column = 2)
        ContraseñaActual.config(show="·")

        # nuevo nombre
        Label(self.nameedit, text = 'Nueva Contraseña').grid(row = 3, column = 1)
        nuevaContra = Entry(self.nameedit)
        nuevaContra.grid(row = 3, column = 2)
        nuevaContra.config(show="·")

        Button(self.nameedit, text = 'Actualizar', command = lambda:self.guarningGeneral(NombreAnterior.get(), ContraseñaActual.get(), nuevoNombre.get(), nuevaContra.get())).grid(row = 4, column = 2, sticky = W)

    def Usrio(self): # cambiar usuario
        listaUsuarios = []
        compro = Base.OnlyRead()  # variable compro recibe dos valores (usuario,  contraseña)
        for i in compro:
            listaUsuarios.append(i)
        self.nameedit = Toplevel() # ventana encima de la anterior
        self.nameedit.title = "Edición de cuentas" # titulo de la ventana

        # nombre anterior
        Label(self.nameedit, text = "Nombre Actual").grid(row = 0, column = 1)
        Entry(self.nameedit, textvariable = StringVar(self.nameedit, value = listaUsuarios[0][1]), state = 'readonly').grid(row = 0, column = 2)

        # nuevo nombre
        Label(self.nameedit, text = 'Nuevo Nombre').grid(row = 1, column = 1)
        nuevoDatoN = Entry(self.nameedit)
        nuevoDatoN.grid(row = 1, column = 2)
        Button(self.nameedit, text = 'Actualizar', command = lambda:self.guarninguser(listaUsuarios[0], nuevoDatoN.get())).grid(row = 4, column = 2, sticky = W)

    def Consena(self): # cambiar contraseña
        listaUsuarios = []
        compro = Base.OnlyRead() # variable compro recibe dos valores (usuario,  contraseña)
        for i in compro:
            listaUsuarios.append(i)
        self.conedit = Toplevel() # ventana encima de la anterior
        self.conedit.title = "Edición de cuentas" # titulo de la ventana

        # nombre anterior
        Label(self.conedit, text = "Contraseña Actual").grid(row = 0, column = 1)
        Entry(self.conedit, textvariable = StringVar(self.conedit, value = listaUsuarios[0][2]), state = 'readonly').grid(row = 0, column = 2)

        # nuevo nombre
        Label(self.conedit, text = 'Nueva Contraseña').grid(row = 1, column = 1)
        nuevoDatoN = Entry(self.conedit)
        nuevoDatoN.grid(row = 1, column = 2)
        Button(self.conedit, text = 'Actualizar', command = lambda:self.guarningcontra(listaUsuarios[0] ,nuevoDatoN.get())).grid(row = 4, column = 2, sticky = W)

    def LlenarArbol(self): # funcion para actualizar la tabla
        # para limpiar el arbol
        residual = self.tabla.get_children() # recibimos los valores en el arbol
        for i in residual:
            self.tabla.delete(i)

        # conexión y consulta
        Llenar = Base.read() # tupla simple
        for datos in Llenar:
            self.tabla.insert("", 0, text = datos[1], values = datos[2]) # se mandan los datos a la interfaz

    def LlenarBase(self): # funcion para llenar la base
        if(len(self.Nombre.get()) != 0 and len(self.Precio.get()) != 0):
            Parametros = (self.Nombre.get(), self.Precio.get())
            Base.add(Parametros) # funcion para conectar y ejecutar
            self.Mensaje['fg'] = 'green'
            self.Mensaje['text'] = 'Producto {} añadido correctamente'.format((self.Nombre.get()).title())
            self.Nombre.delete(0, END) # vaciamos la entrada
            self.Precio.delete(0, END) # vaciamos la entrada
        else:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Datos Faltantes'
        self.LlenarArbol() # mandamos llamar la funcion par aactualizar la pantalla

    def BorrarProd(self): # borra el valor seleccionado del arbol
        self.Mensaje['text'] = ''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Selecciona un dato'
            return
        self.Mensaje['text'] = ''
        parametro = self.tabla.item(self.tabla.selection())['text']
        Base.remove(parametro)
        self.Mensaje['fg'] = 'green'
        self.Mensaje['text'] = 'Artículo {} eliminado correctamente'.format(parametro)
        self.LlenarArbol()

    def EditarProd(self):
        self.Mensaje['text'] = ''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Selecciona un dato'
            return
        self.Mensaje['text'] = ''
        n = self.tabla.item(self.tabla.selection())['text']
        p = self.tabla.item(self.tabla.selection())['values'][0]
        self.edicion = Toplevel() # ventana encima de la anterior
        self.edicion.title = "Edición de productos"

        # nombre anterior
        Label(self.edicion, text = 'Nombre Actual').grid(row = 0, column = 1)
        Entry(self.edicion, textvariable = StringVar(self.edicion, value = n), state = 'readonly').grid(row = 0, column = 2)
        # nuevo nombre
        Label(self.edicion, text = 'Nuevo Nombre').grid(row = 1, column = 1)
        nuevoDatoN = Entry(self.edicion)
        nuevoDatoN.grid(row = 1, column = 2)

        # precio anterior
        Label(self.edicion, text = 'Precio Anterior').grid(row = 2, column = 1)
        Entry(self.edicion, textvariable = StringVar(self.edicion, value = p), state = 'readonly').grid(row = 2, column = 2)
        # nuevo precio
        Label(self.edicion, text = 'Nuevo Precio').grid(row = 3, column = 1)
        nuevoDatoP = Entry(self.edicion)
        nuevoDatoP.grid(row = 3,  column = 2)

        Button(self.edicion, text = 'Actualizar',  command = lambda:Base.edit(self, nuevoDatoN.get(), nuevoDatoP.get(), n, p)).grid(row = 4, column = 2, sticky = W)

    def __init__(self, root):
        self.wind = root # se coloca la raiz dentro de un atributo de la clase
        self.wind.iconbitmap('./res/Logo.ico')
        BarraMenu = Menu(self.wind)
        self.wind.config(menu = BarraMenu)
        self.wind.resizable(width = False,  height = False)
        self.wind.title("Gestión de Productos")

        Archivo = Menu(BarraMenu,  tearoff = 0)
        Archivo.add_command(label = "Guardar como archivo de texto", command = lambda:self.save())
        Archivo.add_separator()
        Archivo.add_command(label = "Salir",  command = lambda:self.exit())

        Editar = Menu(BarraMenu, tearoff = 0)
        Editar.add_command(label = "Copiar", command = lambda:self.copy())
        Editar.add_command(label = "Pegar", command = lambda:self.hidalgo())
        Editar.add_command(label = "Cortar", command = lambda:self.cut())
        Editar.add_command(label = "Eliminar", command = lambda:self.BorrarProd())

        Herramientas = Menu(BarraMenu, tearoff = 0)
        Herramientas.add_command(label = "Cambiar Usuario (actual)", command = lambda:self.Usrio())
        Herramientas.add_command(label = "Cambiar Contraseña (actual)", command = lambda:self.Consena())
        Herramientas.add_command(label = "Cambiar Usuario y Contraseña (cualquier usuario)", command = lambda:self.JoanSebastian())

        Info = Menu(BarraMenu, tearoff = 0)
        Info.add_command(label = "Acerca de...", command = lambda:self.info())

        BarraMenu.add_cascade(label = "Archivo", menu = Archivo)
        BarraMenu.add_cascade(label = "Edición", menu = Editar)
        BarraMenu.add_cascade(label = "Herramientas", menu = Herramientas)
        BarraMenu.add_cascade(label = "Información", menu = Info)

        # contenedor principal
        frame = LabelFrame(self.wind, text = "Registrar nuevo producto")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # label del nombre
        Label(frame, text = 'Nombre').grid(row = 1, column = 0)
        self.Nombre = Entry(frame)
        self.Nombre.focus()
        self.Nombre.grid(row = 1, column = 1)

        # label precio
        Label(frame, text = 'Precio').grid(row = 2, column = 0)
        self.Precio = Entry(frame)
        self.Precio.focus()
        self.Precio.grid(row = 2, column = 1)

        # boton Guardar
        ttk.Button(frame, text = 'Guardar', command = lambda:self.LlenarBase()).grid(row = 3, columnspan = 2, sticky = W+E)

        # boton Borrar
        ttk.Button(text = 'Borrar', command = lambda:self.BorrarProd()).grid(row = 5, column = 0, sticky = W+E)# boton Editar
        ttk.Button(text = 'Editar', command = lambda:self.EditarProd()).grid(row = 5, column = 1, sticky = W+E)

        # notificación
        self.Mensaje = Label(text = '', fg = 'black')
        self.Mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W+E)

        # arbol de productos
        self.tabla = ttk.Treeview(height = 10, columns = 2)
        self.tabla.grid(row = 4, column = 0, columnspan = 2)
        self.tabla.heading('#0', text = 'NOMBRE', anchor = CENTER)
        self.tabla.heading('#1', text = 'PRECIO', anchor = CENTER)
        self.LlenarArbol() # llenar el arbol anterior

class Beta:
    def copy(self):
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Selecciona un dato'
            return
        self.Mensaje['text'] = ''
        nombre = self.tabla.item(self.tabla.selection())['text']
        precio = self.tabla.item(self.tabla.selection())['values'][0]
        portapapeles = nombre + " " + str(precio)
        texto = scrolledtext.ScrolledText(self.wind) # creamos la variable de tkinter para mandar al portapapeles
        texto.clipboard_clear() # limpiamos el portapapeles
        texto.clipboard_append(portapapeles) # guardamos el texto en el portapapeles

    def cut(self):
        self.copy() # se copia al portapapeles el valor seleccionado
        PermisoAdministrador(self) # se borra el valor seleccionado

    def hidalgo(self): # paste pegar
        self.Mensaje['text'] = '' # vaciamos los mensajes anteriores
        texto = scrolledtext.ScrolledText(self.wind) # creamos la variable de tkinter para mandar al portapapeles
        try:
            texto.clipboard_get() # guardamos el texto en el portapapeles
        except IndexError as e:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Copia un dato con el formato "precio valor"'
            return
        portapapeles = texto.clipboard_get()
        nombre = ""
        precio = ""
        for i in portapapeles:
            if i.isdigit():
                precio = precio + i
            elif(i == "."):
                precio = precio + i
            elif(i == " "):
                nombre = nombre
            else:
                nombre = nombre + i
        parametro = (nombre, precio)
        Base.add(parametro)
        self.LlenarArbol()

    def advice(self, texto): # funcion consejo
        if len(texto):
            texto = texto + '.txt'
            archive = open(texto, 'w')
            residual = Base.read()
            for i in residual:
                for j in i:
                    archive.writelines(str(j)+" ")
                archive.writelines("\n")
            archive.close()
            self.saving.destroy()
            self.Mensaje['text'] = ''
        else:
            print("\a")
            self.saving.destroy()
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Datos Faltantes'

    def save(self): # funcion guardar en otro archivo
        self.saving = Toplevel()
        self.saving.title = "Guardar en archivo externo"
        Label(self.saving, text = "Ingresa el nombre del archivo a crear: ").grid(row = 0, column = 0)
        self.guardar = Entry(self.saving)
        self.guardar.grid(row = 0, column = 1, columnspan = 2)
        Button(self.saving,  text = "Guardar",  command = lambda:self.advice(self.guardar.get())).grid(row = 1, column = 0, columnspan = 3)

    def info(self): # informacion del programa
        messagebox.showinfo('Gestor Universal', 'Proyecto Final de Estructuras de Datos y Algoritmos 1\n\nHecho por:\n\n\t Fernando Arciga Guzmán\n\tÁngel David Valenzuela Vigil\n\nAsesorados por: Marco Antonio Martínez Quintana')

    def exit(self): # salir con el boton en casacada
        valor = messagebox.askquestion("Saliendo",  "¿Realmente deseas salir?")
        if valor == "yes":
            self.wind.destroy() # termina el programa

    def LlenarArbol(self): # funcion para actualizar la tabla
        # para limpiar el arbol
        residual = self.tabla.get_children() # recibimos los valores en el arbol
        for i in residual:
            self.tabla.delete(i)

        # conexión y consulta
        Llenar = Base.read() # tupla simple
        for datos in Llenar:
            self.tabla.insert("", 0, text = datos[1], values = datos[2]) # se mandan los datos a la interfaz

    def LlenarBase(self): # funcion para llenar la base
        if(len(self.Nombre.get()) != 0 and len(self.Precio.get()) != 0):
            Parametros = (self.Nombre.get(), self.Precio.get())
            Base.add(Parametros) # funcion para conectar y ejecutar
            self.Mensaje['fg'] = 'green'
            self.Mensaje['text'] = 'Producto {} añadido correctamente'.format((self.Nombre.get()).title())
            self.Nombre.delete(0, END) # vaciamos la entrada
            self.Precio.delete(0, END) # vaciamos la entrada
        else:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Datos Faltantes'
        self.LlenarArbol() # mandamos llamar la funcion par aactualizar la pantalla

    def BorrarProd(self): # borra el valor seleccionado del arbol
        self.Mensaje['text'] = ''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Selecciona un dato'
            return
        self.Mensaje['text'] = ''
        parametro = self.tabla.item(self.tabla.selection())['text']
        Base.remove(parametro)
        self.Mensaje['fg'] = 'green'
        self.Mensaje['text'] = 'Artículo {} eliminado correctamente'.format(parametro)
        self.LlenarArbol()

    def EditarProd(self):
        self.Mensaje['text'] = ''
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Selecciona un dato'
            return
        self.Mensaje['text'] = ''
        n = self.tabla.item(self.tabla.selection())['text']
        p = self.tabla.item(self.tabla.selection())['values'][0]
        self.edicion = Toplevel() # ventana encima de la anterior
        self.edicion.title = "Edición de productos"

        # nombre anterior
        Label(self.edicion, text = 'Nombre Actual').grid(row = 0, column = 1)
        Entry(self.edicion, textvariable = StringVar(self.edicion, value = n), state = 'readonly').grid(row = 0, column = 2)
        # nuevo nombre
        Label(self.edicion, text = 'Nuevo Nombre').grid(row = 1, column = 1)
        nuevoDatoN = Entry(self.edicion)
        nuevoDatoN.grid(row = 1, column = 2)

        # precio anterior
        Label(self.edicion, text = 'Precio Anterior').grid(row = 2, column = 1)
        Entry(self.edicion, textvariable = StringVar(self.edicion, value = p), state = 'readonly').grid(row = 2, column = 2)
        # nuevo precio
        Label(self.edicion, text = 'Nuevo Precio').grid(row = 3, column = 1)
        nuevoDatoP = Entry(self.edicion)
        nuevoDatoP.grid(row = 3,  column = 2)

        Button(self.edicion, text = 'Actualizar',  command = lambda:Base.edit(self, nuevoDatoN.get(), nuevoDatoP.get(), n, p)).grid(row = 4, column = 2, sticky = W)

    def __init__(self, root):
        self.wind = root # se coloca la raiz dentro de un atributo de la clase
        self.wind.iconbitmap('./res/Logo.ico')
        BarraMenu = Menu(self.wind)
        self.wind.config(menu = BarraMenu)
        self.wind.resizable(width = False,  height = False)
        self.wind.title("Gestión de Productos")

        Archivo = Menu(BarraMenu,  tearoff = 0)
        Archivo.add_command(label = "Guardar como archivo de texto", command = lambda:self.save())
        Archivo.add_separator()
        Archivo.add_command(label = "Salir",  command = lambda:self.exit())

        Editar = Menu(BarraMenu, tearoff = 0)
        Editar.add_command(label = "Copiar", command = lambda:self.copy())
        Editar.add_command(label = "Pegar", command = lambda:self.hidalgo())
        Editar.add_command(label = "Cortar", command = lambda:self.cut())
        Editar.add_command(label = "Eliminar", command = lambda:PermisoAdministrador(self))

        Info = Menu(BarraMenu, tearoff = 0)
        Info.add_command(label = "Acerca de...", command = lambda:self.info())

        BarraMenu.add_cascade(label = "Archivo", menu = Archivo)
        BarraMenu.add_cascade(label = "Edición", menu = Editar)
        BarraMenu.add_cascade(label = "Información", menu = Info)

        # contenedor principal
        frame = LabelFrame(self.wind, text = "Registrar nuevo producto")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # label del nombre
        Label(frame, text = 'Nombre').grid(row = 1, column = 0)
        self.Nombre = Entry(frame)
        self.Nombre.focus()
        self.Nombre.grid(row = 1, column = 1)

        # label precio
        Label(frame, text = 'Precio').grid(row = 2, column = 0)
        self.Precio = Entry(frame)
        self.Precio.focus()
        self.Precio.grid(row = 2, column = 1)

        # boton Guardar
        ttk.Button(frame, text = 'Guardar', command = lambda:self.LlenarBase()).grid(row = 3, columnspan = 2, sticky = W+E)

        # boton Borrar
        ttk.Button(text = 'Borrar', command = lambda:PermisoAdministrador(self)).grid(row = 5, column = 0, sticky = W+E)# boton Editar
        ttk.Button(text = 'Editar', command = lambda:PermisoAdministradorEdicion(self)).grid(row = 5, column = 1, sticky = W+E)

        # notificación
        self.Mensaje = Label(text = '', fg = 'black')
        self.Mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W+E)

        # arbol de productos
        self.tabla = ttk.Treeview(height = 10, columns = 2)
        self.tabla.grid(row = 4, column = 0, columnspan = 2)
        self.tabla.heading('#0', text = 'NOMBRE', anchor = CENTER)
        self.tabla.heading('#1', text = 'PRECIO', anchor = CENTER)
        self.LlenarArbol() # llenar el arbol anterior

class Gamma:
    def copy(self):
        try:
            self.tabla.item(self.tabla.selection())['text'][0]
        except IndexError as e:
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Selecciona un dato'
            return
        self.Mensaje['text'] = ''
        nombre = self.tabla.item(self.tabla.selection())['text']
        precio = self.tabla.item(self.tabla.selection())['values'][0]
        portapapeles = nombre + " " + str(precio)
        texto = scrolledtext.ScrolledText(self.wind) # creamos la variable de tkinter para mandar al portapapeles
        texto.clipboard_clear() # limpiamos el portapapeles
        texto.clipboard_append(portapapeles) # guardamos el texto en el portapapeles

    def advice(self, texto): # funcion consejo
        if len(texto):
            texto = texto + '.txt'
            archive = open(texto, 'w')
            residual = Base.read()
            for i in residual:
                for j in i:
                    archive.writelines(str(j)+" ")
                archive.writelines("\n")
            archive.close()
            self.saving.destroy()
            self.Mensaje['text'] = ''
        else:
            print("\a")
            self.saving.destroy()
            self.Mensaje['fg'] = 'red'
            self.Mensaje['text'] = 'Datos Faltantes'

    def save(self): # funcion guardar en otro archivo
        self.saving = Toplevel()
        self.saving.resizable(width=False, height=False)
        self.saving.title = "Guardar en archivo externo"
        Label(self.saving, text = "Ingresa el nombre del archivo a crear: ").pack()
        self.guardar = Entry(self.saving)
        self.guardar.pack()
        Button(self.saving,  text = "Guardar",  command = lambda:self.advice(self.guardar.get())).pack()

    def info(self): # informacion del programa
        messagebox.showinfo('Gestor Universal', 'Proyecto Final de Estructuras de Datos y Algoritmos 1\n\nHecho por:\n\n\t Fernando Arciga Guzmán\n\tÁngel David Valenzuela Vigil\n\nAsesorados por: Marco Antonio Martínez Quintana')

    def exit(self): # salir con el boton en casacada
        valor = messagebox.askquestion("Saliendo",  "¿Realmente deseas salir?")
        if valor == "yes":
            self.wind.destroy() # termina el programa

    def LlenarArbol(self): # funcion para actualizar la tabla
        # para limpiar el arbol
        residual = self.tabla.get_children() # recibimos los valores en el arbol
        for i in residual:
            self.tabla.delete(i)
        # conexión y consulta
        Llenar = Base.read() # tupla simple
        for datos in Llenar:
            self.tabla.insert("", 0, text = datos[1], values = datos[2]) # se mandan los datos a la interfaz

    def __init__(self, root):

        self.wind = root # se coloca la raiz dentro de un atributo de la clase
        self.wind.iconbitmap('./res/Logo.ico')
        BarraMenu = Menu(self.wind)
        self.wind.config(menu = BarraMenu)
        self.wind.resizable(width = False,  height = False)
        self.wind.title("Gestión de Productos")

        Archivo = Menu(BarraMenu,  tearoff = 0)
        Archivo.add_command(label = "Guardar como archivo de texto", command = lambda:self.save())
        Archivo.add_separator()
        Archivo.add_command(label = "Salir",  command = lambda:self.exit())

        Editar = Menu(BarraMenu, tearoff = 0)
        Editar.add_command(label = "Copiar", command = lambda:self.copy())

        Info = Menu(BarraMenu, tearoff = 0)
        Info.add_command(label = "Acerca de...", command = lambda:self.info())

        BarraMenu.add_cascade(label = "Archivo", menu = Archivo)
        BarraMenu.add_cascade(label = "Edición", menu = Editar)
        BarraMenu.add_cascade(label = "Información", menu = Info)

        # contenedor principal
        frame = LabelFrame(self.wind, text = "Lectura de productos registrados")
        frame.grid(row = 0, column = 0, columnspan = 3, pady = 20)

        # label del nombre
        Label(frame, text = 'Nombre').grid(row = 1, column = 0)
        self.Nombre = Entry(frame)
        self.Nombre.config(state = 'readonly')
        self.Nombre.grid(row = 1, column = 1)

        # label precio
        Label(frame, text = 'Precio').grid(row = 2, column = 0)
        self.Precio = Entry(frame)
        self.Precio.config(state = 'readonly')
        self.Precio.grid(row = 2, column = 1)

        # notificación
        self.Mensaje = Label(text = 'MODO LECTURA', fg = 'black')
        self.Mensaje.grid(row = 3, column = 0, columnspan = 2, sticky = W+E)

        # arbol de productos
        self.tabla = ttk.Treeview(height = 10, columns = 2)
        self.tabla.grid(row = 4, column = 0, columnspan = 2)
        self.tabla.heading('#0', text = 'NOMBRE', anchor = CENTER)
        self.tabla.heading('#1', text = 'PRECIO', anchor = CENTER)
        self.LlenarArbol() # llenar el arbol anterior

def IniciarAlpha():
    root = Tk()
    Alpha(root) # se instancia la pantalla principal
    root.mainloop()

def IniciarBeta():
    root = Tk()
    Beta(root) # se instancia la pantalla principal
    root.mainloop()

def IniciarGamma():
    root = Tk()
    Gamma(root) # se instancia la pantalla principal
    root.mainloop()
