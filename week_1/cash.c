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
