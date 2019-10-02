#include<stdio.h>
#include<string.h>
#include<mpi.h>
#define MASTER 0
void main()
{
	char s[]="Priyabrata";
	int MAX_STRING=100;
	int comm_sz,q,c=0,f;
	int my_rank,total_int=0;
	MPI_Init(NULL,NULL);
	MPI_Comm_size(MPI_COMM_WORLD,&comm_sz);
	MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
			MPI_Allreduce(&my_rank,&total_int,1,MPI_INT,MPI_SUM,MPI_COMM_WORLD);
				printf("%d",total_int);
				
MPI_Finalize();
}
