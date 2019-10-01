#include<bits/stdc++.h>
using namespace std;
int main(){
    long long t,n,p,q,m,i,j,k,sum,count,x,y;
    cin>>t;
    while(t--){
        cin>>n>>m;sum=0;
        long long b[n];b[0]=0;
        for(i=1;i<n;i++)
        cin>>b[i];
        while(m--){
            sum=0;
            count=0;
            cin>>p>>q;
            x=p<q?p:q;
            y=p>q?p:q;
            if((y-x)%2==0)
            cout<<"UNKNOWN"<<endl;
            else{
                for(i=x;i<y;i++)
                {
                    if((count%2)==0)
                    sum=sum+b[i];
                    else
                    sum=sum-b[i];
                    count++;
                }
                cout<<sum<<endl;
            }
        }
    }
    return(0);
}

