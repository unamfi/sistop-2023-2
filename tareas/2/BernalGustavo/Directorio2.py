import os
import datetime

class ArchivoOrdenar:
    def __init__(self, nombre, modificacion, modo, tamano):
        self.nombre = nombre
        self.modificacion = modificacion
        self.modo = modo
        self.tamano = tamano

    @staticmethod
    def ordenar(lista):
        lista.sort(key=lambda archivo: archivo.nombre)  # Ordena la lista de archivos por nombre en orden alfabético ascendente
        return lista

def main():
    while True:
        print("//////////////////////////////////")
        directorio = input("Ingrese el directorio: ")
        try:
            numeroDias = int(input("Ingrese el número de días: "))
        except ValueError:
            print("El número de días debe ser un número entero válido.")
            return

        if not os.path.exists(directorio):
            print("El directorio especificado no existe.")
            return

        print("Nombre\t\t\tModificación\t\tModo\tTamaño")
        print("==============================================================")

        lista = []
        for archivo in os.listdir(directorio):
            ruta_archivo = os.path.join(directorio, archivo)
            if os.path.isfile(ruta_archivo):
                fecha_modificacion = os.path.getmtime(ruta_archivo)
                fecha_actual = datetime.datetime.now().timestamp()
                if fecha_modificacion >= fecha_actual - (numeroDias * 86400):
                    modificacion = datetime.datetime.fromtimestamp(fecha_modificacion).strftime('%Y-%m-%d %H:%M:%S')
                    modo = os.stat(ruta_archivo).st_mode
                    tamano = os.stat(ruta_archivo).st_size
                    lista.append(ArchivoOrdenar(archivo, modificacion, modo, tamano))

        lista_ordenada = ArchivoOrdenar.ordenar(lista)
        for archivo in lista_ordenada:
            print(f"{archivo.nombre}\t\t{archivo.modificacion}\t{archivo.modo}\t{archivo.tamano}")

        print(ord('T'), "T", ord('b'), "b\n")

if __name__ == "__main__":
    main()

