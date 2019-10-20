/*
 * C Program to Check whether a given Number is Armstrong
 */
#include <stdio.h>
#include <math.h>
 
void main()
{
    int number, sum = 0, rem = 0, cube = 0, temp;
 
    printf ("enter a number");
    scanf("%d", &number);
    temp = number;
    while (number != 0)
    {
        rem = number % 10;
        cube = pow(rem, 3);
        sum = sum + cube;
        number = number / 10;
    }
    if (sum == temp)
        printf ("The given no is armstrong no");
    else
        printf ("The given no is not a armstrong no");
}
