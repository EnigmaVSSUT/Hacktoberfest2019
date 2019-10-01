#include<stdio.h>
#include<string.h>
#include<mpi.h>
#define MASTER 0
void main()
{
	int MAX_STRING=100;
	char s[100];
	//printf("Enter your name");
//	scanf("%s",&s);
	int comm_sz,q;
	int my_rank;
	MPI_Init(NULL,NULL);
	MPI_Comm_size(MPI_COMM_WORLD,&comm_sz);
	MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
	if(my_rank==MASTER)
	{		
			
			sprintf(s,"Priyabrata");
		//	MPI_Send(&k,1,MPI_INT,0,0,MPI_COMM_WORLD);
	}
			MPI_Bcast(s,100,MPI_CHAR,0,MPI_COMM_WORLD);
							
				
			//MPI_Recv(&k,MAX_STRING,MPI_INT,q,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			//printf("%d,%d",k,my_rank);
		//	MPI_Recv(s,MAX_STRING,MPI_CHAR,q,0,MPI_COMM_WORLD,MPI_STATUS_IGNORE);
			printf("%s\n",s);		
MPI_Finalize();
}
