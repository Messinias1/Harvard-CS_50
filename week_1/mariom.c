#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int input;
    do
    {
        input = get_int("Height: ");
    }

    while (input > 8 || input < 1);

    char h1[] = "       #  #";
    char h2[] = "      ##  ##";
    char h3[] = "     ###  ###";
    char h4[] = "    ####  ####";
    char h5[] = "   #####  #####";
    char h6[] = "  ######  ######";
    char h7[] = " #######  #######";
    char h8[] = "########  ########";

    if (input == 8)
    {
        printf("%s\n%s\n%s\n%s\n%s\n%s\n%s\n%s\n", h1, h2, h3, h4, h5, h6, h7, h8);
    }
    else if (input == 7)
    {
        printf("%s\n%s\n%s\n%s\n%s\n%s\n%s\n", h1, h2, h3, h4, h5, h6, h7);
    }
    else if (input == 6)
    {
        printf("%s\n%s\n%s\n%s\n%s\n%s\n", h1, h2, h3, h4, h5, h6);
    }
    else if (input == 5)
    {
        printf("%s\n%s\n%s\n%s\n%s\n", h1, h2, h3, h4, h5);
    }
    else if (input == 4)
    {
        printf("%s\n%s\n%s\n%s\n", h1, h2, h3, h4);
    }
    else if (input == 3)
    {
        printf("%s\n%s\n%s\n", h1, h2, h3);
    }
    else if (input == 2)
    {
        printf(" #\n##  ##\n");
    }
    else if (input == 1)
    {
        printf("# #\n");
    }
}
