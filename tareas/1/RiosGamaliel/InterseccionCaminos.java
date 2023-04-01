import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;
import java.util.Random;
import java.util.concurrent.Semaphore;

/**
 * Implementación del problema:
 * - "Intersección de caminos"
 */
public class InterseccionCaminos {
  private static Semaphore[] s = {
    new Semaphore(1), new Semaphore(1), new Semaphore(1), new Semaphore(1)
  };

  private static Semaphore[] producerMutex = {
    new Semaphore(0), new Semaphore(0), new Semaphore(0), new Semaphore(0)
  };

  private static List<List<TipoAuto>> autos = List.of(
    new ArrayList<>(), new ArrayList<>(), new ArrayList<>(), new ArrayList<>()
  );

  public static void main(String... args) {

    Runnable autoProducer = () -> {
      Random randGen = new Random();
      randGen.setSeed(LocalDateTime.now().getNano());
      try {
        while (true) {
          Thread.sleep(250);
          int index = randGen.nextInt(4);

          synchronized (autos.get(index)) {
            int tipoAuto = randGen.nextInt(3);
            autos.get(index).add(TipoAuto.values()[tipoAuto]);
          }
          producerMutex[index].release();
        }
      } catch (InterruptedException e) {
        System.exit(0);
      }
    };

    // Creación del productor de autos
    new Thread(autoProducer).start();

    // Carril izquierda (←)
    new Thread(
      new Carril("IZQ", autos.get(0), s[1], s[0], s[3], producerMutex[0])
    ).start();

    // Carril abajo (↓)
    new Thread(
      new Carril("ABJ", autos.get(1), s[0], s[2], s[1], producerMutex[1])
    ).start();

    // Carril derecha (→)
    new Thread(
      new Carril("DER", autos.get(2), s[2], s[3], s[0], producerMutex[2])
    ).start();

    // Carril arriba (↑)
    new Thread(
      new Carril("ARR", autos.get(3), s[3], s[1], s[2], producerMutex[3])
    ).start();
  }
}
