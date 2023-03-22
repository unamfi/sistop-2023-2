import sqlite3
import Main

# funciones para la base de productos
f1 = "CREATE TABLE products (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,NOMBRE_ARTICULO VARCHAR(50) NOT NULL,PRECIO REAL NOT NULL)"
f2 = "SELECT * FROM products ORDER BY NOMBRE_ARTICULO DESC"
f3 = "INSERT INTO products VALUES(NULL, ?, ?)"
f4 = "DELETE FROM products WHERE NOMBRE_ARTICULO = ?"
f5 = "UPDATE products SET NOMBRE_ARTICULO = ?, PRECIO = ? WHERE NOMBRE_ARTICULO = ? AND PRECIO = ?"

# funciones para la base de usuarios
fy = "CREATE TABLE users (ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, Usuario VARCHAR(8), Contrasena VARCHAR(10))"
fx = "SELECT * FROM users"
fz = "INSERT INTO users VALUES(NULL, ?, ?)"
fc = "UPDATE users SET Usuario = ? WHERE Usuario = ? AND Contrasena = ?"
fu = "UPDATE users SET Contrasena = ? WHERE Usuario = ? AND Contrasena = ?"

def createOnce(): # creación única de la tabla usuarios
    Conexión = sqlite3.connect("users")
    Cursor = Conexión.cursor()
    Cursor.execute(fy)
    Conexión.commit()
    Cursor.execute(fz,('root','root'))
    Conexión.commit()
    Cursor.execute(fz,('beta','beta'))
    Conexión.commit()
    Cursor.execute(fz,('gamma','gamma'))
    Conexión.commit()
    Conexión.close()

def OnlyRead(): # lectura única de la tabla
    Conexión = sqlite3.connect("users")
    Cursor = Conexión.cursor()
    comprobante = Cursor.execute(fx)
    return comprobante
    Conexión.commit()
    Conexión.close()

def Cambio_InicioSesion(tipo,cambios): # cambiar usuario/contraseña
    if tipo == "user":
        Conexión = sqlite3.connect("users")
        Cursor = Conexión.cursor()
        Cursor.execute(fc,cambios)
        Conexión.commit()
        Conexión.close()
    elif tipo == "kami":
        user = []
        user.append(cambios[1])
        user.append(cambios[2])
        user.append(cambios[3])
        contra = []
        contra.append(cambios[0])
        contra.append(cambios[2])
        contra.append(cambios[3])
        Conexión = sqlite3.connect("users")
        Cursor = Conexión.cursor()
        Cursor.execute(fc,user)
        Conexión.commit()
        Cursor.execute(fu,contra)
        Conexión.commit()
        Conexión.close()
    else:
        Conexión = sqlite3.connect("users")
        Cursor = Conexión.cursor()
        Cursor.execute(fu,cambios)
        Conexión.commit()
        Conexión.close()

def create(): # creación única de la tabla productos
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(f1)
    Conexión.close()

def remove(param): # borrar productos
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(f4,(param,))
    Conexión.commit()
    Conexión.close()

def read(): # lectura de productos
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Datos = Cursor.execute(f2)
    Conexión.commit()
    return Datos
    Conexión.close()

def add(param): # añadir producto
    Conexión = sqlite3.connect("DataCenter")
    Cursor = Conexión.cursor()
    Cursor.execute(f3,param)
    Conexión.commit()
    Conexión.close()

def edit(Raiz,N,P,n,p): # editar un producto
    if (N and P):
        param = (N,P,n,p)
        Conexión = sqlite3.connect("DataCenter") # nos conectamos
        Cursor = Conexión.cursor() # se crea el cursor para modificar la base
        Cursor.execute(f5,param) # se ejecuta un comando en la base y se mandan los parametros para complementar
        Conexión.commit() # se guardan los cambios en la base
        Conexión.close() # se cierra la conexión a la base de datos
        Raiz.edicion.destroy() # se destruye la ventana
        Raiz.Mensaje['fg'] = 'green'
        Raiz.Mensaje['text'] = 'Artículo {} actualizado correctamente'.format(n)
        Raiz.LlenarArbol()
    else:
        Raiz.edicion.destroy() # se destruye la ventana
        Raiz.Mensaje['fg'] = 'red'
        Raiz.Mensaje['text'] = 'Artículo {} actualizado incorrectamente\nFALTAN DATOS'.format(n)
