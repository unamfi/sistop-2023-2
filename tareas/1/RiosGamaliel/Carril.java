import java.util.List;
import java.util.concurrent.Semaphore;

public class Carril implements Runnable {
  
  private final String id;
  private final List<TipoAuto> autos;
  private final Semaphore mutex, con1, con2, izq;

  public Carril(String id, List<TipoAuto> autos, Semaphore con1, Semaphore  con2, Semaphore izq, Semaphore mutex) {
    this.id = id;
    this.autos = autos;
    this.con1 = con1;
    this.con2 = con2;
    this.izq = izq;
    this.mutex = mutex;
  }

  @Override
  public void run() {
    while (true) {
      try {
        Thread.sleep(500);
        mutex.acquire();

        TipoAuto auto;

        synchronized(autos) {
          auto = autos.remove(0);
        }

        System.out.printf("[%s] Llega auto (%s)\n", id, auto.toString());

        con1.acquire();
        System.out.printf("[%s] Avanzo una vez\n", id, auto.toString());
        con1.release();

        if (auto == TipoAuto.CONTINUAR || auto == TipoAuto.GIRO_IZQ) {
          con2.acquire();
          System.out.printf("[%s] Avanzo otra vez\n", id, auto.toString());
          con2.release();
        }

        if (auto == TipoAuto.GIRO_IZQ) {
          izq.acquire();
          System.out.printf("[%s] Giro izquierda y avanza\n", id, auto.toString());
          izq.release();
        }

        if (auto == TipoAuto.CONTINUAR || auto == TipoAuto.GIRO_IZQ)
          System.out.printf("[%s] Se va auto\n", id, auto.toString());

        if (auto == TipoAuto.GIRO_DER)
          System.out.printf("[%s] Se va auto\n", id, auto.toString());

      } catch (InterruptedException e) {
        System.exit(0);
      }
    }
  }
}
