#include<stdio.h>
#include<string.h>
#include<mpi.h>
#define MASTER 0
void main()
{
	char s[]="Priyabrata";
	int MAX_STRING=100;
	int comm_sz,i,a[25],b[5];
	int my_rank,total_int=0;
	MPI_Init(NULL,NULL);
	MPI_Comm_size(MPI_COMM_WORLD,&comm_sz);
	MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
	if(my_rank==MASTER)
	{		
	for(i=0;i<5;i++)
	{
	MPI_Scatter(&a,2,MPI_INT,&b,5,MPI_INT,0,MPI_COMM_WORLD);		
	}
	for(i=0;i<5;i++)
	{
	printf("%d",b[i]);	
	}
}		
MPI_Finalize();
}
