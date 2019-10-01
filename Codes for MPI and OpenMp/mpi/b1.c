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
/*	if(my_rank!=MASTER)
	{		
			total_int+=my_rank;
			printf("%d",total_int);
		//	MPI_Reduce(&my_rank, &total_int, 1, MPI_INT, MPI_SUM,0,MPI_COMM_WORLD) ;
	}
	else
	{
		//	total_int+=my_rank;*/
			MPI_Reduce(&my_rank,&total_int,1,MPI_INT,MPI_PROD,0,MPI_COMM_WORLD);
		//	MPI_Recv(my_rank,MAX_STRING,MPI_CHAR,f,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			if(my_rank==MASTER)
			{	
				total_int=total_int+my_rank;
				printf("%d",total_int);
			}	
MPI_Finalize();
}
