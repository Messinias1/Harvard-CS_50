#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    float f;
    do
    {
        f = get_float("Change: ");
    }

    while (f < 0.01 || f > 9999999);
    f = (int)(f * 100);
    //     printf("%.2f", f);
    //     printf("F is %.2f and int is %d\n", f, (int)(f* 100));

    return 0;
}

#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main()
{
    float f;
    do
    {
        f = get_float("Change: ");
    }

    while (f < 0.01 || f > 9999999);
    f = (int)(f * 100);
    //     printf("%.2f", f);
    float q = .25;
    float d = .1;
    float n = .05;
    float p = .01;

    int count = 0;

    while (q < f)
    {
        count++;
        f - q;
    }

    while (.1 < f)
    {
        count++;
        f - d;
    }

    while (n < f)
    {
        count++;
        f - n;
    }

    while (.01 < f)
    {
        count++;
        f - p;
    }

    printf("You will have %i coins returned back\n", count);

    //     printf("F is %.2f and int is %d\n", f, (int)(f* 100));

    return 0;
}
