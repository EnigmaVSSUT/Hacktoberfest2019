/******************************************************************************

                              Online C++ Compiler.
               Code, Compile, Run and Debug C++ program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <iostream>

using namespace std;

int main()
{
    int m = 10;
    int x[] = {1, 4, 5, 7, 2, 5, 3, 8 , 9, 10, 6};
    int y[] = {1000, 2000, 5000, 6700, 1500, 2200, 7800, 8400, 9040, 5900};
    double theta0 = 1.1, theta1 = 2.2, a = 0.01;
    int count = 0;
    
    while(count <= 5000)
    {
        cout<<"theta0: "<<theta0 << " theta1:" <<theta1 <<endl;
        double sum = 0, sum1 = 0;
        for(int i = 0; i< m; i++)
        {
            sum += (theta0 + (theta1*x[i])) - y[i];
            sum1 += ((theta0 + (theta1*x[i])) - y[i])*x[i];
        }
        
        
        
        theta0 = theta0 - (a*sum/m);
        theta1 = theta1 - (a*sum1/m);
        
        count ++;
    }
    
    int z;
    cin>>z;
    
    int pred = theta0 + theta1*z;
    cout<< "Predicted Salary: " << pred <<endl;

    return 0;
}
