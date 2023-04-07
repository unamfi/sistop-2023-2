import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Semaphore;

/**
 * Implementación del problema:
 * - "Intersección de caminos"
 * Versión: 1
 */
public class InterseccionCaminos {
  
  /**
   * Arreglo de mutex para controlar el acceso a la lista de autos por hilo.
   */
  private static Semaphore[] autosMutex = {
    new Semaphore(1), new Semaphore(1), new Semaphore(1), new Semaphore(1)
  };

  /**
   * Arreglo de señalizaciones para notificar cuando el productor ha creado autos.
   */
  private static Semaphore[] producerSignal = {
    new Semaphore(0), new Semaphore(0), new Semaphore(0), new Semaphore(0)
  };

  /**
   * Lista donde se almacenan las colas de autos para cada uno de los hilos.
   */
  private static List<List<TipoAuto>> autos = List.of(
    new ArrayList<>(), new ArrayList<>(), new ArrayList<>(), new ArrayList<>()
  );

  public static void main(String... args) {

    // Lógica del PRODUCTOR
    Runnable autoProducer = () -> {
      Random randGen = new Random();
      randGen.setSeed(LocalDateTime.now().getNano());
      try {
        while (true) {
          Thread.sleep(100);
          
          // Selección del carril
          int carril = randGen.nextInt(4);

          synchronized (autos.get(carril)) {
            // Selección del tipo de auto
            int tipoAuto = randGen.nextInt(3);
            autos.get(carril).add(TipoAuto.values()[tipoAuto]);
          }

          // Señalización al CONSUMIDOR
          producerSignal[carril].release();
        }
      } catch (InterruptedException e) {
        System.exit(0);
      }
    };

    // Creación del productor de autos
    new Thread(autoProducer).start();

    // Carril izquierda (←)
    new Thread(
      new Carril("IZQ", autos.get(0), autosMutex[1], autosMutex[0], autosMutex[2], producerSignal[0])
    ).start();

    // Carril abajo (↓)
    new Thread(
      new Carril("ABJ", autos.get(1), autosMutex[0], autosMutex[2], autosMutex[3], producerSignal[1])
    ).start();

    // Carril derecha (→)
    new Thread(
      new Carril("DER", autos.get(2), autosMutex[2], autosMutex[3], autosMutex[1], producerSignal[2])
    ).start();

    // Carril arriba (↑)
    new Thread(
      new Carril("ARR", autos.get(3), autosMutex[3], autosMutex[1], autosMutex[0], producerSignal[3])
    ).start();
  }
}
