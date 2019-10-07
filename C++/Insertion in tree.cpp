#include <iostream>
#include <bits/stdc++.h>
#include <cmath>
#include <stack>
#include <queue>

using namespace std;

struct node 
{
	int key;
	struct node *left;
	struct node *right;
};

struct node *new_node(int data)
{
	struct node *temp=(struct node *)malloc(sizeof(struct node));
	temp->key=data;
	temp->left=NULL;
	temp->right=NULL;
	return temp;
}

struct node *create_tree(int *arr,int i,int n)
{
	if(i>=n)
		return NULL;
	struct node *temp=new_node(arr[i]);
	temp->left=create_tree(arr,(2*i)+1,n);
	temp->right=create_tree(arr,(2*i)+2,n);
	return temp;
}

void insert(struct node *root,int data)
{
	queue <struct node *> q1;
	q1.push(root);
	while(!q1.empty())
	{
		struct node *temp=q1.front();
		if(!temp)
		{
			temp=new_node(data);
			break;
		}
		if(temp->left)
			q1.push(temp->left);
		else
		{
			temp->left=new_node(data);
			break;
		}
		if(temp->right)
			q1.push(temp->right);
		else
		{
			temp->right=new_node(data);
			break;
		}
		q1.pop();	
	}
}

void inorder(struct node *root)
{
	if(root)
	{
		cout << root->key << " " ;
		inorder(root->left);
		inorder(root->right);
	}
}

int main()
{
	int n,num;
	cin >> n;
	int arr[n];
	for(int i=0;i<n;i++)
		cin >> arr[i];
	struct node *tree=create_tree(arr,0,n);
	cin >> num;
	insert(tree,num);
	inorder(tree);
}
