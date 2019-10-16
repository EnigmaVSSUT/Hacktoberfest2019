#include<iostream>
using namespace std;

template <typename T>

class Node {
    public :
    T data;
    Node<T> *next;

    Node(T data) {
        this -> data = data;
        next = NULL;
    }
};

template <typename T>

class Stack {
    Node<T> *head;
    int size;
    public :

    Stack() {
        head = NULL;
		size = 0;
    }

    int getSize() {
        return size;
    }

    bool isEmpty() {
        return size==0;
    }

    void push(T element) {
        Node<T> *newNode = new Node<T>(element);
		newNode -> next = head;
		head = newNode;
		size++;
    }

    T pop() {
        if(isEmpty()) {
			return 0;
		}
		T ans = head -> data;
		Node<T> *temp = head;
		head = head -> next;
		delete temp;
		size--;
		return ans;
    }

    T top() {
        		if(isEmpty()) {
			return 0;
		}
		return head -> data;
    }

    void display(){
    if(isEmpty()){
        cout << "Stack is empty" << endl;
    }
    Node<T> *temp = head;
    while(temp != NULL){
        cout << temp -> data << " ";
        temp = temp -> next;
    }
    cout << endl;
    }
};

    int main() {

        Stack<int> st;
            cout << "MENU" << endl;
    cout << "1.push" << endl;
    cout << "2.top" << endl;
    cout << "3.display" << endl;
    cout << "4.pop" << endl;
    cout << "5.current size of stack" << endl;
    cout << "6.exit" << endl;
    int n;
    do{
        cout << "enter the choice" << endl;
    cin >> n;
        switch(n){
            case 1:{
                int t;
                cout << "enter the value" << endl;
                cin >> t;
                st.push(t);
                break;
            }

            case 2:{
                int ans = st.top();
                if(ans != 0) {
                    cout << ans << endl;
                }
                else {
                    cout << "Stack is empty" << endl;
                }
                break;
            }

            case 3:{
                st.display();
                break;
            }

            case 4:{
                int ans = st.pop();
                if(ans != 0) {
                    cout << ans << endl;
                }
                else {
                    cout << "Stack is empty" << endl;
                }
                break;
            }

            case 5:{
            cout << st.getSize() << endl;
            break;
            }
            case 6:{
                break;
            }
        }
    }while(n != 6);
    }
