#include<iostream>
using namespace std;

void InsertionSort(int arr[], int size)
{
    int i,j,v;
    for(i=1; i<=size; i++)
    {
        v = arr[i];
        j=i;
        while(arr[j-1]>v && j>=1)
        {
            arr[j] = arr[j-1];
            j--;
        }
        arr[j]= v;
    }
}

int main()
{
    int arr[20], size,i;
    cin>>size;
    for(i=0; i<size; i++)
        cin>>arr[i];
    InsertionSort(arr,size);
    cout<<"\n After Sorting the Array : ";
    for(i=0; i<size; i++)
        cout<<arr[i]<<" ";
}
