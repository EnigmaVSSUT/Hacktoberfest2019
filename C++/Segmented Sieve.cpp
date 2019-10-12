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

vector<ll> prime;

void simpleSieve(ll n)
{
    bool mark[n+1];
    memset(mark,true,sizeof(mark));
    for(int i=2;i*i<n;i++)
    {
        if(mark[i])
        {
            for(int j=i*i;j<n;j+=i)
                mark[j]=false;
        }
    }
    for(int i=2;i<n;i++)
    {
        if(mark[i])
        {
            prime.pb(i);
            cout << i << " ";
        }
    }
}

void segmentedSieve(ll n)
{
    ll limit=floor(sqrt(n))+1;
    simpleSieve(limit);
    ll low=limit;
    ll high=2*limit;
    while(low<high)
    {
        if(high>n)
            high=n;
        bool mark[limit+1];
        memset(mark,true,sizeof(mark));
        for(int i=0;i<prime.size();i++)
        {
            ll loLim=floor(low/prime[i])*prime[i];
            if(loLim<low)
                loLim+=prime[i];
            for(int j=loLim;j<high;j+=prime[i])
                mark[j-low]=false;
        }
        for(int i=low;i<high;i++)
        {
            if(mark[i-low])
                cout << i << " ";
        }
        low+=limit;
        high+=limit;
    }
}

int main()
{
    ll n;
    cin >> n;
    segmentedSieve(n);
    return 0;
}
