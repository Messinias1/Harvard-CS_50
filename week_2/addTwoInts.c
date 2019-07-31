#include <cs50.h>
#include <stdio.h>

int add_two_ints(int a, int b);

int main(void)
{
    int x = get_int("Enter a number: ");
    int y = get_int("Enter another number ");

    int z = add_two_ints(x, y);

    printf("The sum of %i and %i is %i\n", x, y, z);
}

int add_two_ints(int a, int b)
{
    int sum = a + b;
    return sum;
}
