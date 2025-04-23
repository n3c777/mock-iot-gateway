#include <stdio.h>
#include <time.h>
#include "../include/utils.h"

void log_to_file(const char *filename, const char *message) {
    FILE *f = fopen(filename, "a");
    if (f == NULL) return;

    time_t now = time(NULL);
    fprintf(f, "[%s] %s\n", ctime(&now), message);
    fclose(f);
}
