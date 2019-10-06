#include <bits/stdc++.h>
using namespace std;

int main() {
	
	string s1,s2;
	cin>>s1>>s2;
	int f=0,i;
	map<char,int> m1,m2;
	for(i=0;i<s1.length();i++)
	{
	    m1[s1[i]]++;
	    
	}
	for(i=0;i<s2.length();i++)
	{
	    m2[s2[i]]++;
	    
	}
	
for(i=0;i<26;i++)
{
    if(m1[char(97+i)]!=m2[char(97+i)])
    f=1;
}
	if(f==0)
	cout<<"match";
	else
	cout<<"not";
}
	
	
	
	
	
	return 0;
}
