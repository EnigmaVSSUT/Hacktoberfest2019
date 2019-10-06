#include<bits/stdc++.h>
using namespace std;
#include<string.h>

int main() {
	//code
	//return 0;
	int t;
	cin>>t;
	while(t--)
	{
	    int c=0;
	   string s;
	   cin>>s;
	   stack<char> st;
	  int l=s.length();
	  for(int i=0;i<l;i++)
	  {
	      if(s[i]=='(')
	      st.push('(');
	      else if(s[i]==')' && st.top()=='(')
	      {
	      st.pop();
	      c=c+2;
	      }
	  }
	  cout<<c;
	} 
	return 0;
}
