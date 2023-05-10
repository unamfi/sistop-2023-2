import java.util.List;
import java.util.concurrent.Semaphore;

public class Carril implements Runnable {
  
  /**
   * El nombre con el cual se identifica al hilo
   */
  private final String id;

  /**
   * Tipo de carril (HORIZONTAL o VERTICAL) para la exclusión mutua
   */
  private final TipoCarril tipoCarril;

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
   * Semáforo a través del cual se construye la implementación 
   * del apagador.
   */
  private static Semaphore apagador = new Semaphore(1);

  /**
   * Cantidad de carriles que hay de cada tipo procesando 
   * un auto al mismo tiempo.
   */
  private static int numCarrilesVert = 0, numCarrilesHor = 0;

  public Carril(String id, TipoCarril tipoCarril, List<TipoAuto> autos, Semaphore frente1, Semaphore  frente2, Semaphore izquierda, Semaphore producerSignal) {
    this.id = id;
    this.tipoCarril = tipoCarril;
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

        // Lógica del apagador (entrada)
        if (this.tipoCarril == TipoCarril.VERTICAL)
          synchronized (TipoCarril.VERTICAL) {
            if (++numCarrilesVert == 1)
              apagador.acquire();
          }
        else
          synchronized (TipoCarril.HORIZONTAL) {
            if (++numCarrilesHor == 1)
              apagador.acquire();
          }

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

        // Lógica del apagador (salida)
        if (this.tipoCarril == TipoCarril.VERTICAL)
          synchronized (TipoCarril.VERTICAL) {
            if (--numCarrilesVert == 0)
              apagador.release();
          }
        else
          synchronized (TipoCarril.HORIZONTAL) {
            if (--numCarrilesHor == 0)
              apagador.release();
          }
      }
    } catch (InterruptedException e) {
      System.exit(1);
    }
  }
}
