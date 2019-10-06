#include<bits/stdc++.h>
using namespace std;
main()
{
	int a[]={1,6,2,3,7,8},i,j,k;
	map<int,int> m;
	int sum=8,c=0;
	for(int i=0;i<6;i++)
	
	{
		m[a[i]]=1;
	}
	sort(a,a+6);
	for(int i=0;i<6;i++)
	{
		if(m.find(sum-a[i])!=m.end())
		{
		c++;
		cout<<a[i]<<" "<<sum-a[i]<<endl;
		}
	}
	cout<<c;
}
