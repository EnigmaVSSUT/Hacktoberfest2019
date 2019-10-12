#include <iostream>
#include <bits/stdc++.h>
using namespace std;
#define mod 1000000007
#define pb(x) push_back(x);
#define mp(x,y) make_pair(x,y)
#define X first
#define Y second
typedef long long int ll;
typedef pair<ll,ll> pp;

#define debug(x) cout << #x << " :: "<< x <<"\n";
#define debug2(x,y) cout << #x << " :: "<< x << "\t" << #y << " :: " << y << "\n";
#define debug3(x,y,z) cout << #x << " :: "<< x << "\t" << #y << " :: " << y << "\t" << #z << " :: " << z << "\n";
#define boost ios_base::sync_with_stdio(false);cin.tie(0);cout.tie(0);
#include <ext/pb_ds/assoc_container.hpp>
#include <ext/pb_ds/tree_policy.hpp>
using namespace __gnu_pbds;
#define ordered_set tree< pair<ll,ll> , null_type,less< pair<ll,ll> >, rb_tree_tag,tree_order_statistics_node_update>

int main()
{
    boost
    ll n;
    cin >> n;
    bool isPrime[n+1];
    ll primes[n+1];
    memset(primes,0,sizeof(primes));
    memset(isPrime,true,sizeof(isPrime));
    isPrime[0]=false;
    isPrime[1]=false;
    for(int i=2;i*i<=n;i++)
    {
        if(isPrime[i])
        {
            //primes[i]=primes[i-1]+1;
            for(int j=i*i;j<=n;j+=i)
                isPrime[j]=false;
        }
    }
    for(int i=2;i<=n;i++)
    {
        if(isPrime[i])
            primes[i]=primes[i-1]+1;
        else
            primes[i]=primes[i-1];
    }
    ll q;
    cin >> q;
    while(q--)
    {
        ll a,b;
        cin >> a >> b;
        if(primes[a]==primes[b])
            cout << primes[b]-primes[a] << endl;
        else
            cout << primes[b]-primes[a]+1 << endl;
    }
    return 0;
}
