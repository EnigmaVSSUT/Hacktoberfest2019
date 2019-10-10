#include <bits/stdc++.h>
using namespace std;

#define MAXN 10000

struct node{
	// whatever attributes you want for the node
	node* next[26]; 	// one for each 26 lowercase alphabet	
	bool isWord;		// see if it is a word
}

node nodePool[MAXN];	// global pool for nodes; prevents constant 'heavy' dynamic allocation
node* root;
int nextFree;

node* getNode(){
	node* result = &nodePool[nextFree++];
	for(int i=0;i<26;i++)
		result->next[i] = 0;
	result->isLeaf = false;
	return result;
}

void addToTrie(char* str){
	int c;
	node* crawl = root;
	for(i=0;str[i]!='\0';i++){
		c = str[i] - 'a';
		if(!crawl->next[c])
			crawl->next[c] = getNode();
		crawl = crawl->next[c];
	}
	crawl->isWord = true;
}

bool searchTrie(char* str){
	int c,i;
	node* crawl = root;
	for(i=0;str[i]!='\0';i++){
		c = str[i] - 'a';
		if(!crawl->next[c])
			return false;
		crawl = crawl->next[c];
	}
	return true;
}

void init(){
	nextFree=0;
	root=getNode();	
}

int main() {
	// no need to dynamically allocate memory to node for each testcase; already done statically- nodePool
	int t,i;
	cin>>t;
	while(t--){
		init();
		// your code here
	}
	return 0;
}