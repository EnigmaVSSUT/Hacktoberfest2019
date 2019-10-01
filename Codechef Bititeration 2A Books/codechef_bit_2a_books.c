#include<iostream>
using namespace std;
int main()
{
	int t,size,i,j,c;
	cin>>t;
	while(t--)
	{
		cin>>size;
		int a[size],b[size];
		for(i=0;i<size;i++)
		cin>>a[i];
        for(i=0;i<size;i++)
		{
			c=0;
			for(j=i+1;j<size;j++)
			{
				if(a[i]<a[j])
				c++;
			}
			b[i]=c;
			cout<<b[i]<<" ";
			}
			cout<<"\n";
		
	}
	return 0;
}
