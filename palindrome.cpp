/ by @chaupatt (https://github.com/chaupatt)                             
#include <iostream>
using namespace std;

int main(){
    int n;
    cout << "Enter a number: ";
    cin >> n;
    int pal = 0, temp = n;
    while(temp!=0){
        int add = temp % 10;
        pal = (pal*10)+add;
        temp = temp/10;
    }
    if(n == pal) cout << n << " is a palindrome.\n";
    else cout << n << " is not a palindrome.\n";
}
