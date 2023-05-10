import java.util.Scanner;

public class SumaComplejos {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        // Pedir al usuario los valores de los números complejos a sumar
        System.out.println("Introduce el primer número complejo:");
        double real1 = sc.nextDouble();
        double imag1 = sc.nextDouble();
        
        System.out.println("Introduce el segundo número complejo:");
        double real2 = sc.nextDouble();
        double imag2 = sc.nextDouble();
        
        // Realizar la suma de los números complejos
        double realResultado = real1 + real2;
        double imagResultado = imag1 + imag2;
        
        // Mostrar el resultado al usuario
        System.out.println("La suma de los números complejos es:");
        System.out.println(realResultado + " + " + imagResultado + "i");

        System.out.println("Fin del programa.\n");
    }
}
