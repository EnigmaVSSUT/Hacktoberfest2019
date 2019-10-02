#include<stdio.h>
#include<stdlib.h>
#include<mpi.h>
#define size 25
#define master 0
void main()
{
	int i,a[size],b[size/5]={0},comm_sz,my_rank,s=0,sum=0;
	MPI_Init(NULL,NULL);
	for(i=0;i<=size;i++)
		a[i]=i+1;
	MPI_Comm_size(MPI_COMM_WORLD,&comm_sz);
	MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
	MPI_Scatter(a,5,MPI_INT,b,5,MPI_INT,0,MPI_COMM_WORLD);
	
		for(i=0;i<(size/5);i++){
			printf("%d ",b[i]);
			s=s+b[i];
		}
			
	printf("%d",s);
	printf("\n");
	MPI_Reduce(&s,&sum,1,MPI_INT,MPI_SUM,0,MPI_COMM_WORLD);
	if(my_rank==master)
		printf("%d",sum);
	MPI_Finalize();
}
