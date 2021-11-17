#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main(int argc, char *argv[]) {
    int fd = open(argv[1], O_RDONLY);
    if(fd == -1)
    {
        printf("Le fichier n'est pas trouvable\n");
    }
    close(fd);
    return 0;
}
