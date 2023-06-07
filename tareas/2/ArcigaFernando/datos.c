/*  siiiiiiiiiiiiiiiiiiiiiiiiiiiii
*   por fin logre hacer que funcione
*   código hecho por Fernando Arciga, para la clase de sistemas operativos 2023-2
*   para ejecutarlo se debe usar: informameD </carpeta/subcarpeta> <días_en_entero>
*/

#include <stdio.h>
#include <sys/stat.h>
#include <dirent.h>
#include <time.h>

typedef struct stat _stat;
typedef struct dirent _dirent;

void read(_stat file_info) {
    printf("\nTamaño del archivo: %ld bytes", file_info.st_size);
    printf("Último acceso: %s", ctime(&file_info.st_atime));
    printf("Última modificación: %s", ctime(&file_info.st_mtime));
    printf("Último cambio de estado: %s\n", ctime(&file_info.st_ctime));
}

int main(int argc, char *argv[]) {
    if (argc != 3) return 1;
    
    char *nombredir = argv[1];
    DIR *dir; dir = opendir(nombredir);
    if (dir == NULL) {
        printf("\nNo se pudo abrir el directorio '%s'.\n", nombredir);
        return 1;
    }

    long int dias;
    sscanf(argv[2], "%ld", &dias);
    time_t segundos = dias * 24 * 60 * 60;
    time_t eloy = time(NULL);

    _dirent *archivo;
    while ((archivo = readdir(dir)) != NULL) {
        char ruta[257];
        snprintf(ruta, sizeof(ruta), "%s/%s", nombredir, archivo->d_name);
        _stat file_info;
        if (stat(ruta, &file_info) == 0){ // no hay error al intentar abrir el archivo
            time_t edad = eloy - file_info.st_mtime;
            if((file_info.st_mode != S_IFDIR)){
                if (edad <= segundos){
                    printf("\nArchivo: %s", archivo->d_name);
                    read(file_info);
                }
            }
        }
    }

    closedir(dir);
}
