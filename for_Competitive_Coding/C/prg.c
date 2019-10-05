// Problem statement : The Roots of a quadratic equation are to be calculated if the coefficients of the terms are given.

// Quadratic equation is of the form : A*X2+B*X+C=0
   where A , B and  C are the coefficients.


//Language used:C

#include<stdio.h>

#include<math.h>

int main(void)

{
   
   int a,b,c,d;
  
   double r1,r2;
    
   scanf("%d%d%d\n",&a,&b,&c);             //Accepting the coefficients.
 
   d=b*b-4*a*c;
  
   if(d<0)
 
   d=-1*d;
   
   r1=(double)(-b+sqrt(d))/(2*a);         //Calculating root 1
   
   r2=(double)(-b-sqrt(d))/(2*a);         //Calculating root 2
   
   printf("%lf\n%lf",r1,r2);
    
   return 0;

}