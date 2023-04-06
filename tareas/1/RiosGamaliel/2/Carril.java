import java.util.List;
import java.util.concurrent.Semaphore;

public class Carril implements Runnable {
  
  private final String id;
  private final TipoCarril tipoCarril;
  private final List<TipoAuto> autos;
  private final Semaphore mutex, con1, con2, izq;

  private static Semaphore s = new Semaphore(1), s1 = new Semaphore(2);
  private static int numSemVert = 0, numSemHor = 0;

  public Carril(String id, TipoCarril tipoCarril, List<TipoAuto> autos, Semaphore con1, Semaphore  con2, Semaphore izq, Semaphore mutex) {
    this.id = id;
    this.tipoCarril = tipoCarril;
    this.autos = autos;
    this.con1 = con1;
    this.con2 = con2;
    this.izq = izq;
    this.mutex = mutex;
  }

  private void girarDerecha() throws InterruptedException {
    this.con1.acquire();
    System.out.printf("[%s] Avanzo una vez\n", id);
    System.out.printf("[%s] Giro der\n", id);
    this.con1.release();
  }

  private void girarIzquierda() throws InterruptedException {
    con1.acquire();
    System.out.printf("[%s] Avanzo una vez\n", id);
    con2.acquire();
    con1.release();
    System.out.printf("[%s] Avanzo otra vez\n", id);
    izq.acquire();
    con2.release();
    System.out.printf("[%s] Giro izq y avanzo\n", id);
    izq.release();
  }

  private void continuarDerecho() throws InterruptedException {
    con1.acquire();
    System.out.printf("[%s] Avanzo una vez\n", id);
    con2.acquire();
    con1.release();
    System.out.printf("[%s] Avanzo otra vez\n", id);
    con2.release();
  }

  @Override
  public void run() {
    TipoAuto auto;

    try {
      while (true) {
        Thread.sleep(1000);
        mutex.acquire();

        if (this.tipoCarril == TipoCarril.VERTICAL)
          synchronized (TipoCarril.VERTICAL) {
            if (++numSemVert == 1)
              s.acquire();
            s1.acquire();
          }
        else
          synchronized (TipoCarril.HORIZONTAL) {
            if (++numSemHor == 1)
              s.acquire();
            s1.acquire();
          }

        synchronized (autos) {
          auto = autos.remove(0);
        }

        System.out.printf("[%s] Llega auto (%s)\n", id, auto.toString());

        if (auto == TipoAuto.CONTINUAR)
          continuarDerecho();
        else if (auto == TipoAuto.GIRO_DER)
          girarDerecha();
        else if (auto == TipoAuto.GIRO_IZQ)
          girarIzquierda();

        System.out.printf("[%s] Me voy\n", id, auto.toString());

        if (this.tipoCarril == TipoCarril.VERTICAL)
          synchronized (TipoCarril.VERTICAL) {
            s1.release();
            if (--numSemVert == 0)
              s.release();
          }
        else
          synchronized (TipoCarril.HORIZONTAL) {
            s1.release();
            if (--numSemHor == 0)
              s.release();
          }
      }
    } catch (InterruptedException e) {
      System.exit(1);
    }
  }
}
