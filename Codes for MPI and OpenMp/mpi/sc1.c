#include<stdio.h>
#include<mpi.h>
#define size 25
#define master 0
void main()
{
	int i,c[10],a[size],b[size/5]={0},comm_sz,s1=0,my_rank,k=0,sum=0;
	for(i=0;i<=size;i++)
		a[i]=i+1;
	MPI_Init(NULL,NULL);
	MPI_Comm_size(MPI_COMM_WORLD,&comm_sz);
	MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
	MPI_Scatter(a,5,MPI_INT,b,5,MPI_INT,0,MPI_COMM_WORLD);
	
		for(i=0;i<(size/5);i++)
			printf("%d ",b[i]);
		for(i=0;i<5;i++)
		{
		sum+=b[i];
		c[k]=sum;
		k++;
		}
		printf("sum=%d",sum);
	printf("\n");
	MPI_Reduce(&c,&s1,1,MPI_INT,MPI_SUM,0,MPI_COMM_WORLD);
	if(my_rank==0)
	{
	printf("\n%d",s1);
	}
	MPI_Finalize();
}
