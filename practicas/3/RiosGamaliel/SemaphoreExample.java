import java.util.concurrent.Semaphore;
import java.util.stream.IntStream;

public class SemaphoreExample {
  public static void main(String... args) {
    Semaphore s = new Semaphore(3);

    double x[] = IntStream.range(5, 25).mapToDouble(i -> 2.0 / i).toArray();

    ComplexOperation co = new ComplexOperation(s);

    for (int i = 0; i < x.length; i++) {
      final int index = i;
      Thread r = new Thread(() -> {
        try {
          co.packAndCalculateData(x[index]);
        } catch (InterruptedException e) {}
      });

      r.start();
    }
  }
}
