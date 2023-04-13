import java.util.Arrays;
import java.util.concurrent.Semaphore;
import java.util.stream.IntStream;

public class ComplexOperation {
  private Semaphore s;
  private double[] coefficiets = IntStream.range(1, 500).mapToDouble(i -> 1.0 / i).toArray();

  public ComplexOperation(Semaphore s) {
    this.s = s;
  }

  public double calculateData(double x) {
    System.out.printf("Computing p(%6.4f)...\t\t(Thread: %d)\n", x, Thread.currentThread().getId());

    return Arrays.stream(this.coefficiets)
      .reduce((acc, num) -> x * acc + num)
      .getAsDouble();
  }

  public void sendData(double x, double data) {
    System.out.printf("- Sending p(%6.4f)=%6.4f\t(Thread: %d)\n", x, data, Thread.currentThread().getId());
  }

  public void packAndCalculateData(double x) throws InterruptedException {
    s.acquire();
    var result = calculateData(x);
    s.release();
    sendData(x, result);
  }
}
