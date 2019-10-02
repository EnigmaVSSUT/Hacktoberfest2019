#include <omp.h>
#include <stdio.h>
#include <stdlib.h>

#define N 3000                 /* number of rows in matrix A */

int main (int argc, char *argv[]) 
{
int	i, j, k, chunk;
double	a[N][N],           /* matrix A to be multiplied */
	b[N][N],           /* matrix B to be multiplied */
	c[N][N];           /* result matrix C */

chunk=10;
#pragma omp parallel for private(i,j,k) schedule(static,chunk)
  for (i=0; i<N; i++)
    for (j=0; j<N; j++){
      a[i][j]= i+j;
      b[i][j]= i*j;
      c[i][j]= 0;
      }

  /*** Do matrix multiply sharing iterations on outer loop ***/
#pragma omp parallel for  private(i,j,k) schedule(static,chunk)
  for (i=0; i<N; i++)    
    for(k=0; k<N; k++)       
      for (j=0; j<N; j++)
        c[i][j] += a[i][k] * b[k][j];

/****Print the last element of the loop****/
printf("%lf\n",c[N-1][N-1]);

  } 

