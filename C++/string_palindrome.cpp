#include<bits/stdc++.h>

using namespace std;

//A string is said to be palindromic if it is same when read from both sides(left to right OR right to left)
//'check' is a function that checks whether the input string is a palindrome or not.

bool check(string s)
{
	int l = 0;
	int r = s.length()-1;

	while(l<=r)
	{
		if(s[l]!=s[r])
			return false;
		l++;
		r--;
	}
	return true;
}

int main()
{
	int t;   //number of testcases
	cin>>t;

	while(t--)
	{
		string s;   //input string
		 cin>>s;

		bool ans = check(s);
		cout<<ans<<endl;
	}

	return 0;
}
