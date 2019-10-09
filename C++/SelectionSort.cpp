#include<iostream>
using namespace std;

void SelectionSort(int arr[], int size)
{
    int i,j,min;
    for(i=0; i<size-1; i++)
    {
        min = i;
        for(j=i+1; j<size; j++)
        {
            if(arr[j]<arr[min])
                min =j;
        }
        int temp = arr[min];
        arr[min]= arr[i];
        arr[i]=temp;

    }
}

int main()
{
    int arr[20], size,i;
    cin>>size;
    for(i=0; i<size; i++)
        cin>>arr[i];
    SelectionSort(arr,size);
    cout<<"\n After Sorting the Array : ";
    for(i=0; i<size; i++)
        cout<<arr[i]<<" ";
}
