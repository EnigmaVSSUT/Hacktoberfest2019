#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
void hanoi(int n, char A, char B, char C)
{
	if(n>0)
	{
		hanoi(n-1, A, C, B);
		cout<<A<<" to "<<C<<"\n";
		hanoi(n-1, B, A, C);
	}
	
}
main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	int n;
	cin>>n;
	hanoi(n, 'A', 'B', 'C');
}

