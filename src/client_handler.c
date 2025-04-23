#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <openssl/ssl.h>
#include "../include/client_handler.h"

void handle_client(SSL *ssl) {
    char buffer[1024];
    while (1) {
        int bytes_received = SSL_read(ssl, buffer, sizeof(buffer) - 1);
        if (bytes_received <= 0) {
            printf("Client disconnected or SSL error.\n");
            break;
        }

        buffer[bytes_received] = '\0';
        printf("Received: %s\n", buffer);
    }

    int fd = SSL_get_fd(ssl);
    close(fd);
}

