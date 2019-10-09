#include<bits/stdc++.h>
#include<string.h>
using namespace std;

main()
{
	string s;
	cin>>s;
	int l=s.length();
	int i=0,b=0,w=0;
	while(s[i]!='\0' && l>=3)
	{
		if(s[i]=='w'&&s[i+1]=='w'&&s[i+2]=='w')
		{
			w++;
			i=i+3;
			l=l-3;
		}
		else if(s[i]=='b'&&s[i+1]=='b'&&s[i+2]=='b'&& l>=3)
		{
			b++;
			i=i+3;
			l=l-3;
		}
		else
		i++;
	}
	if(w>b)
	cout<<"wendy";
	else
	cout<<"bob";
}
