#include<stdio.h>
#include<string.h>
#include<mpi.h>
#define MASTER 0
void main()
{
	int MAX_STRING=200;
	char greeting[MAX_STRING];
	int comm_sz,q;
	int my_rank;
	MPI_Init(NULL,NULL);
	MPI_Comm_size(MPI_COMM_WORLD,&comm_sz);
	MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
	if(my_rank!=MASTER)
	{
		sprintf(greeting,"Welcome to the world of Parallel Computing. I am process no %d out of %d",my_rank,comm_sz);
		MPI_Send(greeting,strlen(greeting)+1,MPI_CHAR,0,0,MPI_COMM_WORLD);
	}
	else
	{
		printf("Welcome to the world of parallel computing. I am process no %d out of %d",my_rank,comm_sz);
	for(q=1;q<comm_sz;q++)
	{
		MPI_Recv(greeting,MAX_STRING,MPI_CHAR,q,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
		printf("%s\n",greeting);
	}
	}
	MPI_Finalize();
}
	
