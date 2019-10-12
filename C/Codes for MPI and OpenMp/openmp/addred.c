#include<stdio.h>
#define N 1000000000
int main()
{
 long int i,a[N],sum=0,local=0;
#pragma omp parallel for 
 for(i=0;i<N;i++)
 {
  a[i]=i+1;
 }
#pragma omp parallel 
{
	
	#pragma omp for reduction(+:sum)
 		for(i=0;i<N;i++)
 		{	
		sum+=a[i];
		}
}
  printf("Sum=%ld  \n",sum);

 return 0;
}


