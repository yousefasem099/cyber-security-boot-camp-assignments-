#include <stdio.h>
#include <string.h>

int main() {
    char input[100];

    printf("Enter text to convert: ");
    fgets(input, sizeof(input), stdin);

    input[strcspn(input, "\n")] = 0;

    printf("Hexadecimal output:\n");

    for (int i = 0; input[i] != '\0'; i++) {
        printf("%02X ", (unsigned char)input[i]);
    }
    
    printf("\n");
    return 0;
}
