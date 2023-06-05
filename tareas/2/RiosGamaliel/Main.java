import java.io.File;
import java.io.FileFilter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.attribute.PosixFilePermissions;
import java.time.Duration;
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.List;

public class Main {
  private static File directory = null;
  private static long dias;

  private static boolean getParams(String[] args) {
    File file = new File(args[0]);
    
    if (!file.exists() || !file.isDirectory()) {
      return false;
    }

    directory = file;
    Main.dias = Long.parseLong(args[1]);
    return true;
  }

  private static List<File> listDirectoryFiles() {
    var today = LocalDateTime.now(ZoneId.systemDefault());
    FileFilter filter = (f) -> {
      var date = LocalDateTime.ofInstant(
          Instant.ofEpochMilli(f.lastModified()),
          ZoneId.systemDefault());
      long days = Duration.between(date, today).toDays();
      return days <= Main.dias;
    };
    return List.of(directory.listFiles(filter));
  }

  private static String getOctalPermissions(File file) throws IOException {
    int[] modes = {0,0,0};
    var filePermission = Files.getPosixFilePermissions(file.toPath());
    String permissions = PosixFilePermissions.toString(filePermission);

    if (permissions.substring(0, 3).contains("r"))
      modes[0] += 4;
    if (permissions.substring(0, 3).contains("w"))
      modes[0] += 2;
    if (permissions.substring(0, 3).contains("x"))
      modes[0] += 1;
    if (permissions.substring(3, 6).contains("r"))
      modes[1] += 4;
    if (permissions.substring(3, 6).contains("w"))
      modes[1] += 2;
    if (permissions.substring(3, 6).contains("x"))
      modes[1] += 1;

    if (permissions.substring(6, 9).contains("r"))
      modes[2] += 4;
    if (permissions.substring(6, 9).contains("w"))
      modes[2] += 2;
    if (permissions.substring(6, 9).contains("x"))
      modes[2] += 1;

    String initialSequence = file.isFile() ? "100" : "040";

    return initialSequence + modes[0] + modes[1] + modes[2];

  }

  private static void showFilesInformation(List<File> files) {
    System.out.printf("%25s\t%18s\t%6s\t%10s\t\n",
      "Nombre", "Modificación", "Modo", "Tamaño");
    System.out.printf("%60s\n",
      "=====================================" + 
      "=====================================");
    files
      .forEach(f -> {
        String name = f.getName();
        name = name.length() > 25 ? name.substring(0, 22).concat("...") : name;
        String date = LocalDateTime
          .ofInstant(
            Instant.ofEpochMilli(f.lastModified()),
            ZoneId.systemDefault())
          .format(DateTimeFormatter.ofPattern("dd-MM-yyyy hh:ss"));
        String mode = "[]";
        try {
          mode = getOctalPermissions(f);
        } catch (IOException e) {
          e.printStackTrace();
        }
        String size = String.valueOf(f.length());
        System.out.printf("%25s\t%18s\t%6s\t%10s\n",
          name, date, mode, size);
      });
  }

  public static void main(String... args) {
    if (args.length == 2) {
      getParams(args);
      System.out.println(directory);
      var filteredFiles = listDirectoryFiles();
      showFilesInformation(filteredFiles);
    } else {
      System.err.append("Esto no es válido :(");
    }
  }
}
