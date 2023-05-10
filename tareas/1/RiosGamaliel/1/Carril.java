import java.util.List;
import java.util.concurrent.Semaphore;

/**
 * Lógica de cada uno de los carriles
 */
public class Carril implements Runnable {
  
  /**
   * El nombre con el cual se identifica al hilo
   */
  private final String id;

  /**
   * La lista de autos asignada al carril
   */
  private final List<TipoAuto> autos;

  /**
   * La señalización que usa el PRODUCTOR para 
   * notificar la creación de un nuevo auto
   */
  private final Semaphore producerSignal;
  
  /**
   * Secciones a utilizar para los movimientos. 
   * Se toman de forma relativa al carril en cuestión.
   */
  private final Semaphore frente1, frente2, izquierda;

  /**
   * Multiplex para evitar que más de tres carriles 
   * procesen autos al mismo tiempo.
   */
  private static Semaphore multiplex = new Semaphore(3);

  public Carril(String id, List<TipoAuto> autos, Semaphore frente1, Semaphore  frente2, Semaphore izquierda, Semaphore producerSignal) {
    this.id = id;
    this.autos = autos;
    this.frente1 = frente1;
    this.frente2 = frente2;
    this.izquierda = izquierda;
    this.producerSignal = producerSignal;
  }

  private void girarDerecha() throws InterruptedException {
    this.frente1.acquire();
    System.out.printf("[%s] Avanzo una vez\n", id);
    Thread.sleep(15);
    System.out.printf("[%s] Giro der\n", id);
    this.frente1.release();
  }

  private void girarIzquierda() throws InterruptedException {
    frente1.acquire();
    System.out.printf("[%s] Avanzo una vez\n", id);
    Thread.sleep(15);
    frente2.acquire();
    frente1.release();
    System.out.printf("[%s] Avanzo otra vez\n", id);
    Thread.sleep(15);
    izquierda.acquire();
    frente2.release();
    System.out.printf("[%s] Giro izq y avanzo\n", id);
    Thread.sleep(15);
    izquierda.release();
  }

  private void continuarDerecho() throws InterruptedException {
    frente1.acquire();
    System.out.printf("[%s] Avanzo una vez\n", id);
    Thread.sleep(15);
    frente2.acquire();
    frente1.release();
    System.out.printf("[%s] Avanzo otra vez\n", id);
    Thread.sleep(15);
    frente2.release();
  }


  @Override
  public void run() {
    TipoAuto auto;

    try {
      while (true) {
        Thread.sleep(1000);
        
        // Se espera la señalización de PRODUCTOR
        producerSignal.acquire();
        multiplex.acquire();

        // Se consume el primer auto de la lista
        synchronized (autos) {
          auto = autos.remove(0);
        }

        // Se procesa el auto
        System.out.printf("[%s] Llega auto (%s)\n", id, auto.toString());

        if (auto == TipoAuto.CONTINUAR)
          continuarDerecho();
        else if (auto == TipoAuto.GIRO_DER)
          girarDerecha();
        else if (auto == TipoAuto.GIRO_IZQ)
          girarIzquierda();

        System.out.printf("[%s] Me voy\n", id, auto.toString());

        // Se libera un espacio del multiplex
        multiplex.release();
      }
    } catch (InterruptedException e) {
      System.exit(0);
    }
  }
}
