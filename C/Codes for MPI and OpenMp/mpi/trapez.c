#include<stdio.h>
#include<mpi.h>
 
void Get_data(int p,int my_rank,double* a_p,double* b_p,int* n_p);

double Trap(double local_a,double local_b,int local_n,double h);

double f(double x);

int main()
{
int my_rank,p,n,local_n,source,dest=0,tag=0;
double a,b,h,local_a,local_b,my_area,total;
MPI_Status status;

MPI_Init(&argc,&argv);
MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
MPI_Comm_size(MPI_COMM_WORLD,&p);

Get_data(p,my_rank,&a,&b,&n);

h=(b-a)/n;
local_n=n/p;

local_a=a+my_rank*local_n*h;
local_b=local_a+local_n*h;
my_area=Trap(local_a,local_b,local_n,h);

if(my_rank==0)
{
	total=my_area;
	for(source=1;source<p;source++)
	{
		MPI_Recv(&my_area,1,MPI_DOUBLE,source,tag,MPI_COMM_WORLD,&status);
		total=total+my_area;
	}
}else
{
	MPI_Send(&my_area,1,MPI_DOUBLE,dest,tag,MPI_COMM_WORLD);
}
if(my_rank==0)
{
printf("with n=%d trapezoids, our estimate\n",n);
printf("of the area from %f to %f=%.15f\n",a,b,total);
}
MPI_Finalize();
return 0;
void Get_data(int p,int my_rank,double* a_p,double* b_p,int* n_p)
{
	int q;
	MPI_Status status;
	if(my_rank==0)
	{
		printf("enter a,b,n\n");
		scanf("%lf,%lf,%d",&a,&b,&n);
		for(q=1;q<p;q++)
		{
		MPI_Send(a_p,1,MPI_DOUBLE,q,0,MPI_COMM_WORLD);
		MPI_Send(b_p,p,1,MPI_DOUBLE,q,0,MPI_COMM_WORLD);
		MPI_Send(n_p,1,MPI_INT,q,0,MPI_COMM_WORLD);
		}
	}
	else{
	MPI_Recv(a_p,1,MPI_DOUBLE,0,0,MPI_COMM_WORLD,&status);
	MPI_Recv(b_p,1,MPI_DOUBLE,0,0,MPI_COMM_WORLD,&status);
	MPI_Recv(n_p,1,MPI_INT,0,0,MPI_COMM_WORLD,&status);
	}
}

double Trap(double local_a,double local_b,int local_n,double h)
{
	double my_area,x;
	int i;
	my_area=(f(local_a)+f(local_b))/2.0;
	x=local_a;
	for(i=1;i<=local_n-1;i++)
	{
		x=local_a+i*h;
		my_area=my_area+f(x);
	}
my_area*=h;
return my_area;
double f(double x)
{
	double return_val;
	return_val=x*x+1;
	return return_val;
	}












































