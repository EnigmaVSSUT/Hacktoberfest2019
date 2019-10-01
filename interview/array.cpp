#include<bits/stdc++.h>
using namespace std;
main()
{
	int n,k,c[1000],t=0,d=0;
	cin>>n;
	int a[n];
	for(int i=0;i<n;i++)
	cin>>a[i];
	for(int i=0;i<n;i++)
	{
		for(int j=i+1;j<n;j++)
		{
			c[k]=a[i]+a[j];
			k++;
		}
	}
	for(int i=0;i<k;i++)
	cout<<c[i]<<" ";
	cout<<endl;
	int e[k-1]={0};
	//sort(c,c+k);
//	cout<<c[k-1];
	for(int i=0;i<k;i++)
	{
		for(int j=i+1;j<k;j++)
		{
			if((c[i]==c[j]) && (e[j]==0))
			{
			d++;
			e[j]=1;
		}
	}
		if(d>t)
		{
			cout<<d<<" ";
			t=d;
			d=0;
		}
}
cout<<t+1;
}
