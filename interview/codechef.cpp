#include<bits/stdc++.h>
using namespace std;

int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int n,i;
	    cin>>n;
	    int a[n],b[n],c[n]={0},j,ct=0;
	    for(i=1;i<=n;i++)
	    {
	    cin>>a[i];
	}
	    for(i=1;i<=n;i++)
	{
	    cin>>b[i];
	}
	    for(i=1;i<=n;i++)
	    {
			for(j=i-a[i];j<=i+a[i];j++)
			{
				if(j>=0)
				{
					c[j]=c[j]+1;
				}
			}
		}
	//	sort(c,c+(n+1));
	//	sort(b,b+(n+1));
		for(i=1;i<=n;i++)
		cout<<c[i];
		cout<<endl;
		for(i=1;i<=n;i++)
		cout<<b[i];
		int f=0;
		for(i=1;i<=n;i++)
		{
			if(b[i]!=c[i])
			f=1;
		}
		if(f==1)
		cout<<"NO";
		else
		cout<<"YES";
		cout<<endl;
}
	return 0;
	
	
	
}

