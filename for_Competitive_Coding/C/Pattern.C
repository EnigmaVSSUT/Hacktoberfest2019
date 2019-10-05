/*  *                                                    
   ***                                                      
  *****                                                     
  @   @                                                     
  @   @                                                     
  @   @
  @ * @                                                     
  @***@                                                     
  *****
Sample pattern for input n=5
Number of rows of '@' should be 'n' as well as the number of columns. '*' Should be adjusted accordingly.*/

#include<stdio.h>
void main()
{
    int i,j,k,l,n,space;
    printf("\nEnter size: ");
    scanf("%d",&n); //Input should be odd number for proper pattern
    space=(n-1)/2+1;
    for (i=0;i<=((n/2)+1);i++)
    {
        for (k=0;k<space;k++)
        {
            printf(" ");
        }
        for (j=0;j<2*i-1;j++)
        {
            printf("*");
        }

        space--;
        printf("\n");
    }
    space=((n-1)/2)-1;
    for(i=1;i<=n;i++)
    {
        if(i<=((n/2)+1))
        {
            for(j=1;j<=n;j++)
            {
                if(j==1 || j==n)
                    printf("@");
                else
                    printf(" ");
            }
            printf("\n");
        }
        else
        {

            printf("@");
            for (k=0;k<space;k++)
            {
                printf(" ");
            }
            for (l=0;l<2*i-1-2*(n/2+1);l++)
            {
                printf("*");
            }
            for (k=0;k<space;k++)
            {
                printf(" ");
            }
            printf("@");
            space--;
            printf("\n");
        }


    }
    for(i=1;i<=n;i++)
        printf("*");
}
