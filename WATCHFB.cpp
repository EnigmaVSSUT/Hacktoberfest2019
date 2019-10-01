#include <iostream>
#include<bits/stdc++.h>
#define ll long long int
using namespace std;

int main()
{
    ll t;
    cin>>t;
    while(t--)
    {
        ll n;
        cin>>n;
        ll a = 0, b =0;
        while(n--)
        {
            ll q,a1,b1;
            cin>>q>>a1>>b1;
            if(q==1)
            {
                a = a1;b = b1;
                cout<<"YES"<<endl;
            }
            else
            {
                ll max12 = max(a1,b1),min12 = min(a1,b1),max11 = max(a,b),min11 = min(a,b);
                if(max12==min12)
                {
                    a = max12,b =min12;
                    cout<<"YES"<<endl;
                }
                else if (min12>=max11)
                {
                    cout<<"NO"<<endl;
                }
                else if ((min12>=min11&&min12<=max11)&&(max12>=max11))
                {
                    if(a==min11)
                    {
                        a = min12;b=max12;
                    }
                    else if (b==min11)
                    {
                        b = min12;a = max12;
                    }
                    cout<<"YES"<<endl;
                }
            }
        }
    }


    return 0;
}

