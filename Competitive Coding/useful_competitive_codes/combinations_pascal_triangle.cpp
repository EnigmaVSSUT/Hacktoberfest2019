// combinations using pascal triangle
#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;
#define MAXN 51 // maximum value of n
    
main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	ll dp[MAXN+1][MAXN+1];
	ll n,r;
    for(ll i = 0;i<=MAXN;i++)
    {
    	dp[i][0]=1;
		dp[0][i]=1;
	}
    for(ll i = 1;i<=MAXN;i++)
    {
    	for(ll j = 1;j<=MAXN;j++)
    		dp[i][j] = dp[i-1][j]+dp[i][j-1];
	}
	cin>>n>>r;
	cout<<dp[r][n-r];
}

