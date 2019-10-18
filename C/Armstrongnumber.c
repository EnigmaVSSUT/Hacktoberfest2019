#include <stdio.h>
int main(void)
{
    int number, originalNumber, remainder, result = 0;
    printf("Enter a three digit integer: ");
    
 //take the input from user
    scanf("%d", &number);
    originalNumber = number;
    
 //test the number to be armstrong
    while (originalNumber != 0)
    {
        remainder = originalNumber%10;
        result += remainder*remainder*remainder;
        originalNumber /= 10;
    }
    
 //compare with the original number
    if(result == number)
        printf("%d is an Armstrong number.",number);
    else
        printf("%d is not an Armstrong number.",number);
        
    return 0;
}
