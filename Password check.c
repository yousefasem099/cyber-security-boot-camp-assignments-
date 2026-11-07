
#include <stdio.h>
#include <string.h>

int main() {
    char pass[100];
    int i, up=0, low=0, num=0, sym=0;

    printf("Enter password: ");
    scanf("%99s", pass);

    for(i=0; pass[i]!='\0'; i++) {
        if(pass[i]>='A' && pass[i]<='Z') up=1;
        else if(pass[i]>='a' && pass[i]<='z') low=1;
        else if(pass[i]>='0' && pass[i]<='9') num=1;
        else sym=1;
    }

    if(strlen(pass)>=8 && up && low && num && sym)
        printf("Strong Password");
    else
        printf("Weak Password");

    return 0;
}
