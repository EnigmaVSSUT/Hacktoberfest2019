/*
 * Program to output two random matrices
 * Compile Using: "g++ dataSetGen.cpp "
 *
 * Created By Yashasvi Goel
 * Date:05/06/18
 * Input the size of first array
 * Repeat for second array
 * Take the output in a file
 * Use the file as input for any program in this repository
 * (the size of the arrays will be included)
 *
 */
#include<bits/stdc++.h>
int main()
{
	int n,m;
	scanf("%d %d",&n,&m);
	int p,q;
	srand(time(0));
	scanf("%d %d",&p,&q);
	printf("%d %d\n",n,m);
	for(int i=0;i<(n);i++)
	{
		for(int j=0;j<m;j++)
			printf("%d ",rand());
		printf("\n");
	}
	printf("%d %d\n",p,q);
	for(int i=0;i<p;i++)
	{
		for(int j=0;j<q;j++)
			printf("%d ",rand());
		printf("\n");
	}
	return 0;
}
