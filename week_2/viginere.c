#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

int main(int argc, string argv[])
{
    // Declare if argc isnt equal to 2 end program
    if (argc != 2)
    {
        printf("Usage: ./viginere <keyword>\n");
        return 1;
    }

    // Make argv[1] a string loop in array and see if key is alphabetical
    string key = argv[1];
    int lenk = strlen(key);

    for (int i = 0; i < lenk; i++)
    {
        if (!isalpha(key[i]))
        {
            printf("keyword must be letters only\n");
            return 1;
        }
    }

    // Get user plaintext iterate through plaintext repeat j for lenk of key, print ciphertext
    string plaintext = get_string("plaintext: ");
    int len = strlen(plaintext);

    printf("ciphertext: ");

    for (int i = 0, j = 0; i < len; i++)
    {
        if (isalpha(plaintext[i]))
        {
            if (islower(plaintext[i]))
            {
                printf("%c", (plaintext[i] - 'a' + toupper(key[j]) - 'A') % 26 + 'a');
            }
            else if (isupper(plaintext[i]))
            {
                printf("%c", (plaintext[i] - 'A' + toupper(key[j]) - 'A') % 26 + 'A');
            }
            j = (j + 1) % lenk;
        }
        else
        {
            printf("%c", plaintext[i]);
        }
    }
    printf("\n");
}
