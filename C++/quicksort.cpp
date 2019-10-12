#include<iostream>
using namespace std;

void swap(int *a,int *b){
  int tmp;
  tmp=*a;
  *a=*b;
  *b=tmp;
}

int partition(int A[],int low,int high){
  int pivot;
  pivot=A[high];
  int i=low-1;
  for(int j=low;j<high;j++){
    if(A[j]<=pivot){
      i++;
      swap(&A[i],&A[j]);
    }
  }
  swap(&A[i+1],&A[high]);
  return(i+1);
}

void quickSort(int A[],int low,int high){
  if(low<high){
    int pt=partition(A,low,high);
    quickSort(A,low,pt-1);
    quickSort(A,pt+1,high);
  }
}

int main(){
  int n;
  cout<<"Enter the number of array elements \n";
  cin>>n;
  int a[n];
  cout<<"Enter the array elements \n";
  for(int i=0;i<n;i++){
    cin>>a[i];
  }
  quickSort(a,0,n-1);
  cout<<"The elements in sorted order are \n";
  for(int i=0;i<n;i++){
    cout<<a[i]<<" ";
  }
  return 0;
}
