//Sieve of Eratosthenes O(n)
#include<bits/stdc++.h>
using namespace std;
int n;
vector<bool>prime;
main()
{
	ios::sync_with_stdio(0);
	cin.tie(0);
	cin>>n;
	prime.assign(n,true);
	for (int p=2; p*p<=n; p++) 
    { 
        if (prime[p] == true) 
        {  
            for (int i=p*p; i<=n; i += p) 
                prime[i] = false; 
        } 
    } 
    
    for (int p=2; p<=n; p++) 
       if (prime[p]) 
          cout << p << " "; 
}
