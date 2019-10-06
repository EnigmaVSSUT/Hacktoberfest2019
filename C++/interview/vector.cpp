
#include<bits/stdc++.h>
using namespace std;
main(){
int n;
cin>>n;

	vector<int> v;
		for(int i=0;i<n;i++){
		v.push_back(i);
		}
		for(int i=0;i<n;i++){
		cout<<v[i]<<" ";
		}
		cout<<endl;
		vector<int>::iterator it;
	
		for(it=v.begin();it!=v.end();++it){
			it=v.erase(it);
      				if(it==v.end())
					break;
			}
				for(it=v.begin();it!=v.end();++it){
			cout<<v;
			}
 }
