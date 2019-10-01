#include <bits/stdc++.h>
using namespace std;
 
#define MOD 1000000007
#define MAX 1000000
  
typedef long long int lli;
 
lli fact[MAX], invFact[MAX];
 
lli nCr(lli n, lli r)
{
	return (((fact[n]*invFact[r])%MOD)*invFact[n-r])%MOD;
} 
 
main()
{
	lli i,n,r;
	fact[0] = invFact[0] = invFact[1] = 1;
	for(i=1;i<MAX;i++) fact[i] = (fact[i-1]*i)%MOD;
	for(i=2;i<MAX;i++) invFact[i] = (MOD - MOD/i) * invFact[MOD % i] % MOD;
	for(i=1;i<MAX;i++) invFact[i] = (invFact[i-1] * invFact[i])%MOD;
	
	cin>>n>>r;
	cout<<nCr(n,r);
}
