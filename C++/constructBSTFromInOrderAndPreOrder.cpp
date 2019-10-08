//A program to construct a binary tree, given the inorder and preorder traversals of the tree.
# include <iostream>
# include <vector>
# include <map>

using namespace std;

//Structure for binary tree
struct Node
{
    int Data;
    Node *Left, *Right;

    Node(int x)
    {
        Data = x;
        Left = Right = NULL;
    }
};

void inOrderTraversal(Node *Root)
{
    if(Root == NULL)
      return ;

    inOrderTraversal(Root -> Left);
    cout << Root -> Data << " ";
    inOrderTraversal(Root -> Right);
}

void preOrderTraversal(Node *Root)
{
    if(Root == NULL)
      return ;

    cout << Root -> Data << " ";
    preOrderTraversal(Root -> Left);
    preOrderTraversal(Root -> Right);
}

/*
The logic here is:
Say we have 2 arrays, PRE and IN.
Preorder traversing implies that PRE[0] is the root node.
Then we can find this PRE[0] in IN, say it's IN[5].
Now we know that IN[5] is root, so we know that IN[0] - IN[4] is on the left side, IN[6] to the end is on the right side.
Recursively doing this on subarrays, we can build a tree out of it.
*/
//Function to construct tree from the preOrder and inOrder traversals
//Note To Self : The preEnd parameter is not necessary here, but I am including it for uniformity.
Node *constructTree(int preStart, int preEnd, int inStart, int inEnd, vector <int> preOrder, vector <int> inOrder, map <int, int> inMap)
{
    if(preStart > preEnd || inStart > inEnd)
    {
        return NULL;
    }

    Node *Root = new Node(preOrder[preStart]); //The first node of the preOrder traversal will be the root node.
    int inRoot = inMap[preOrder[preStart]]; //Find where the root node exists in the inOrder traversal list.
    int numsLeft = inRoot - inStart; //The number of nodes on the left side of the root on the inorder traversal are the number of nodes in the left subtree.

    //The left subtree of the root will be all the nodes which are present before the root node in the inorder traversal.
    Root -> Left = constructTree(preStart + 1, preEnd, inStart, inRoot - 1, preOrder, inOrder, inMap);
    //The right subtree of the root will be all the nodes which are present after the root node in the inorder traversal.
    Root -> Right = constructTree(preStart + numsLeft + 1, preEnd, inRoot + 1, inEnd, preOrder, inOrder, inMap);
    return Root;
}

int main(void)
{
    vector <int> inOrder = {4, 2, 5, 1, 3, 6};
    vector <int> preOrder = {1, 2, 4, 5, 3, 6};

    if(inOrder.size() != preOrder.size())
    {
        cout << "\nCannot construct tree since both the tree since the number of elements in the both the lists is different.";
        return 1;
    }

    map <int, int> inMap;

    //Create a map to store the data as the key and the index as the value.
    for(int i = 0 ; i < inOrder.size() ; i++)
      inMap[inOrder[i]] = i;

    Node *Root = constructTree(0, preOrder.size() - 1, 0, inOrder.size() - 1, preOrder, inOrder, inMap);
    cout << "\nInorder and preorder traversals after constructing the tree : \n";
    inOrderTraversal(Root);
    cout << "\n";
    preOrderTraversal(Root);
    return 0;
}
//End of program
