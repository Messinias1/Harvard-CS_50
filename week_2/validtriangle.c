#include <stdio.h>
#include <stdlib.h>
#include <cs50.h>

bool validtriangle(double a, double b, double c);

bool validtriangle(double a, double b, double c)
{
    if (a <= 0 || b <= 0 || c <= 0)
    {
        return false;
    }

    if ((a + b <= c) || (a + c <= b) || (b + c <= a))
    {
        return false;
    }
    return true;
}
