#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
// Prompt user for input
{
    float total;
    do
    {
        total = get_float("Change: ");
    }

    while (total < 0);

    // Round to 100 and create change variables

    total = roundf(total * 100);
    printf("%.2f\n", total);

    float q = 25;
    float d = 10;
    float n = 5;
    float p = 1;

    int count = 0;

    // Increase coin count and subract total while true

    while (q <= total)
    {
        count++;
        total = total - q;
    }

    while (d <= total)
    {
        count++;
        total = total - d;
    }

    while (n <= total)
    {
        count++;
        total = total - n;
    }

    while (p <= total)
    {
        count++;
        total = total - p;
    }

    // Return count to user

    printf("You will have %i coins returned back\n", count);

    return 0;
}
