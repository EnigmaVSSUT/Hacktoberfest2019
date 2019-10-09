#include<bits/stdc++.h>
using namespace std;
main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin>>n;
	vector <int> arr(n);
	for(int i=0;i<n;i++)
		cin>>arr[i];
	
	int max_so_far=INT_MIN, max_ending_here=0,s=0,end=0,start=0;
    for(int i=0;i<n;i++)
    {
        max_ending_here=max_ending_here+arr[i];
        if(max_so_far<max_ending_here)
        {
        	max_so_far=max_ending_here;
        	start=s;
        	end=i;
		}
            
            
        if(max_ending_here<0)
        {
        	max_ending_here=0;
        	s=i+1;
		}
    }
    //cout<<max_so_far;
    for(int i=start;i<=end;i++)
    	cout<<arr[i]<<" ";
    cout<<"\n";
}
