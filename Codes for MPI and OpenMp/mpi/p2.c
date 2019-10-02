#include<stdio.h>
#include<string.h>
#include<mpi.h>
#define MASTER 0
void main()
{
	int MAX_STRING=200;
	char greeting[MAX_STRING];
	int comm_sz,q;
	int my_rank,i;
	MPI_Init(NULL,NULL);
	MPI_Comm_size(MPI_COMM_WORLD,&comm_sz);
	MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
	printf("%d is executing\n",my_rank);
	printf("There are %d process out of %d process\n",my_rank,comm_sz);
	MPI_Finalize();
}
	
