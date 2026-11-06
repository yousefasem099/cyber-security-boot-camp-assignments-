//   اولا يجب ادخال اسم الملف المراد البحث داخله مع المسار او وضع الملف بجانب مسار الكود
//   ثانيا ادخال الكلمة المراد البحث عنها بداخل الملف 
#include <stdio.h>
#include <string.h>

int main() {
    char filename[100];
    char word[50];
    char line[256];
    int found = 0;

    printf("Enter file name: ");
    scanf("%s", filename);

    printf("Enter word to find: ");
    scanf("%s", word);

    FILE *f = fopen(filename, "r");
    if (f == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    while (fgets(line, sizeof(line), f) != NULL) {
        if (strstr(line, word) != NULL) {
            found = 1;
            break;
        }
    }

    fclose(f);

    if (found == 1) {
        printf("Found!\n");
    } else {
        printf("Not found.\n");
    }

    return 0;
}
