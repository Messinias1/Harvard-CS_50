#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int shift(char c);

int main(int argc, string argv[])
{
    char c;
    printf("Enter a character: ");
    scanf("%c", &c);
    if (isalpha(c) == 0)
        printf("Usage: ./vigenere keyword");
    else
        printf("Success");
    return 0;
}

int shift(char c)
{
    int key = shift(argv[1][0]);
    printf("%i\n", key);
}
