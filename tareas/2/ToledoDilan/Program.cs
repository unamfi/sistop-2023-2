using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Analizador_deArchivos
{
    internal class Program
    {
        class archivoOrdenar
        {
            public string nombre, modificacion, tamano, modo;
            public archivoOrdenar(string nombre, string modificacion, string modo, string tamano)
            {
                this.nombre = nombre;
                this.modificacion = modificacion;
                this.tamano = tamano;
                this.modo = modo;
            }
            static public List<archivoOrdenar> ordenar(List<archivoOrdenar> a)
            {
                List<archivoOrdenar> lista = new List<archivoOrdenar>();
                for (int i = 0; i < a.Count - 1; i++)
                {
                    for (int j = 0; j < a.Count - 1; j++)
                    {
                        archivoOrdenar archivo = null;bool flag = true;
                        char[] p1 = a[j].nombre.ToCharArray(); char[] p2 = a[j + 1].nombre.ToCharArray();
                        for (int k = 0; k < Math.Min(p1.Length, p2.Length); k++)
                            if ((int)p1[k] < (int)p2[k]) { flag = false; break; }
                            else if ((int)p1[k] > (int)p2[k])
                            {
                                archivo = a[j];
                                a[j] = a[j + 1];
                                a[j + 1] = archivo;
                                flag = false;
                                break;
                            }
                        if (archivo == null && a[j + 1].nombre.Length == Math.Min(p1.Length, p2.Length)&&flag)
                        {
                            archivo = a[j];
                            a[j] = a[j + 1];
                            a[j+1] = archivo;          
                        }flag = true;
                    }

                }
                return a;

            }

        }

        static void Main(string[] args)
        {
            string directorio;
            int numeroDias;
            while (true) { //durará hasta que le ingreses mal un directorio o día
                Console.WriteLine("/////////////////Nueva consulta/////////////////");
            Console.Write("Ingrese el directorio : ");
            directorio = Console.ReadLine();

            Console.Write("Ingrese el número de días: ");
            if (!Int32.TryParse(Console.ReadLine(), out numeroDias))
            {
                Console.WriteLine("El número de días debe ser un número entero válido.");
                return;
            }

            if (!Directory.Exists(directorio))
            {
                Console.WriteLine("El directorio especificado no existe.");
                return;
            }
            DirectoryInfo dirInfo = new DirectoryInfo(directorio);
            Console.WriteLine("Nombre\t\t\tModificación\t\tModo\tTamaño");
            Console.WriteLine("==============================================================");
                List<archivoOrdenar> lista = new List<archivoOrdenar> { };
                
                foreach (var archivo in dirInfo.GetFiles())
                {
                    if (archivo.LastWriteTime >= DateTime.Now.AddDays(-numeroDias))
                    {
                        lista.Add(new archivoOrdenar(archivo.Name, archivo.LastWriteTime.ToString(),
                        archivo.Attributes.ToString(), archivo.Length.ToString()));
                    }
                }
                lista = archivoOrdenar.ordenar(lista);
                foreach (var archivo in lista)
                {
                   
                        Console.WriteLine($"{archivo.nombre}\t\t{archivo.modificacion}\t{archivo.modo}\t{archivo.tamano}");
                    
                }
                Console.WriteLine(((int)'T')+" T "+ ((int)'b')+"b");
                Console.WriteLine("\n");
            }

            
        }
       
    }
}
