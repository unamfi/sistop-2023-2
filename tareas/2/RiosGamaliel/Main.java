import java.io.File;
import java.io.FileFilter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.attribute.PosixFilePermission;
import java.time.Duration;
import java.time.Instant;
import java.time.LocalDateTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.List;
import java.util.stream.Collectors;

public class Main {
  private static File directory = null;
  private static long maxDays;

  private static boolean getParams(String[] args) {
    File file = new File(args[0]);
    Main.maxDays = Long.parseLong(args[1]);
    
    if (Main.maxDays >= 0 && !file.exists() || !file.isDirectory()) {
      return false;
    }

    directory = file;
    return true;
  }

  private static List<File> listDirectoryFiles() {
    var today = LocalDateTime.now(ZoneId.systemDefault());
    FileFilter filter = (f) -> {
      var date = LocalDateTime.ofInstant(
          Instant.ofEpochMilli(f.lastModified()),
          ZoneId.systemDefault());
      long days = Duration.between(date, today).toDays();
      return days <= Main.maxDays;
    };
    return List.of(directory.listFiles(filter));
  }

  private static String getOctalPermissions(File file) throws IOException {
    int[] modes = {0,0,0};
    var filePermissions = Files.getPosixFilePermissions(file.toPath());

    if (filePermissions.contains(PosixFilePermission.OWNER_READ))
      modes[0] += 4;
    if (filePermissions.contains(PosixFilePermission.OWNER_WRITE))
      modes[0] += 2;
    if (filePermissions.contains(PosixFilePermission.OWNER_EXECUTE))
      modes[0] += 1;

    if (filePermissions.contains(PosixFilePermission.GROUP_READ))
      modes[1] += 4;
    if (filePermissions.contains(PosixFilePermission.GROUP_WRITE))
      modes[1] += 2;
    if (filePermissions.contains(PosixFilePermission.GROUP_EXECUTE))
      modes[1] += 1;

    if (filePermissions.contains(PosixFilePermission.OTHERS_READ))
      modes[2] += 4;
    if (filePermissions.contains(PosixFilePermission.OTHERS_WRITE))
      modes[2] += 2;
    if (filePermissions.contains(PosixFilePermission.OTHERS_EXECUTE))
      modes[2] += 1;

    String initialSequence = file.isFile() ? "100" : "040";

    return initialSequence + modes[0] + modes[1] + modes[2];

  }

  private static List<File> sortFiles(List<File> files) {
    return files
        .stream()
        .parallel()
        .sorted((a, b) -> {
          return a.getName().toLowerCase().compareTo(b.getName().toLowerCase());
        })
        .collect(Collectors.toList());
  }

  private static void showFilesInformation(List<File> files) {
    System.out.printf("%25s\t%18s\t%6s\t%10s\t\n",
      "Nombre", "Modificación", "Modo", "Tamaño");
    System.out.printf("%60s\n",
      "=====================================" + 
      "=====================================");
    files
      .forEach(f -> {
        String nameStr = f.getName();
        nameStr = nameStr.length() > 25 ? nameStr.substring(0, 22).concat("...") : nameStr;
        String dateStr = LocalDateTime
          .ofInstant(
            Instant.ofEpochMilli(f.lastModified()),
            ZoneId.systemDefault())
          .format(DateTimeFormatter.ofPattern("dd-MM-yyyy HH:ss"));
        String modeStr = "[]";
        try {
          modeStr = getOctalPermissions(f);
        } catch (IOException e) {
          e.printStackTrace();
        }
        String size = String.valueOf(f.length());
        System.out.printf("%25s\t%18s\t%6s\t%10s\n",
          nameStr, dateStr, modeStr, size);
      });
  }

  public static void main(String... args) {
    if (args.length == 2 && getParams(args)) {
        System.out.printf("Showing %s directory", directory);
        var filteredFiles = sortFiles(listDirectoryFiles());
        showFilesInformation(filteredFiles);
        return;
      }
    System.err.append("Perdón, esto no es válido :(");
  }
}
