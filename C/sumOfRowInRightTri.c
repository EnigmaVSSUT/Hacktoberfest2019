//C Program to find the sum of rows in a right-angled triangle
#include<stdio.h>
void main()
{
    int i, j,rows,sum;
    printf("Enter the number of rows\n");
    scanf("%d",&rows);
    for(i=1;i<=rows;i++)
    {
        sum=0;
        for(j=1;j<=i;j++)
        {
            sum+=j;
            if(j!=i)
            {
                printf("%d +",j);
            }
            else
            {
                printf("%d",j);
            }
            
        }
        printf("%d",sum);
        printf("\n");
    }
    }