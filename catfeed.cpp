#include <iostream>
using namespace std;

int main() {
	int t;
	cin >> t;
	while(t--){
	    int n,m;
	    cin >> n>>m;
	    int arr[m],fr[n],c = 0 ;
	   
	    for(int i= 0;i<n;i++)
	        fr[i] = 0;
        
        for(int i=0;i<m;i++){
            cin>>arr[i];
        }
	        
	    for(int i=0;i<m/n;i++){
	       for(int j = 0;j<n;j++){
	           fr[arr[ (n*i)+j ] -1]++;
	           
	           if(fr[arr[ (n*i)+j ] - 1 ] != 1){
	               c = 1;
	               break;
	           }
	       }
	       
	       for(int i= 0;i<n;i++)
	        fr[i] = 0;
	    }
	    
	    for(int i= 0;i<n;i++)
	        fr[i] = 0;
	        
	   
	    if(c == 1){
	        cout << "NO" << std::endl;
	    }
	    else
	        for(int i = 0;i<m%n;i++){
	            fr[arr[i + (m/n)*n]]++;
	            if(fr[arr[i+(m/n)]-1]>1){
	                cout << "NO" << std::endl;
	                c = 1;
	                break;
	            }
	        }
	        if(c == 0){
	            cout << "YES" << std::endl;
	        }
	}
	return 0;
}
