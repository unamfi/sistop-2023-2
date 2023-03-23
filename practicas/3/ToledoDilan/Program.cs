using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace p1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string hora = DateTime.Now.ToString("hh:mm:ss");
            string fecha = DateTime.Now.ToLongDateString();
            Console.WriteLine($"Buen dia, ahora son las {hora} de la fecha {fecha}\n");
        }
    }
}
