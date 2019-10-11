#include<iostream>
using namespace std;
int main()
{
	int i,j,n,bt[25],at[25],wt[25],tat[25],st[25];
	float awt=0,atat=0;
	cout<<"Enter the no. of process :";
	cin>>n;
	cout<<"Enter the burst time :";
	for (i=0;i<n;i++){
		cin>>bt[i];
	}
    cout<<"Enter the arival time of the processes :";
    for(i=0;i<n;i++){
    cin>>at[i];
    }
	temp[0]=0;
	for(i=0;i<n;i++){
		wt[i]=0;
		tat[i]=0;
		st[i+1]=st[i]+bt[i];
		wt[i]=st[i]-at[i];
		tat[i]=wt[i]+bt[i];
		awt=awt+wt[i];
		atat=atat+tat[i];
	cout<<"Process :"<<i+1<<endl<<"Burst Time :"<<bt[i]<<endl<<"Arrival Time :"<<at[i]<<endl<<"Waiting Time :"<<wt[i]<<endl<<"Turn around Time :"<<tat[i]<<endl;	
	cout<<endl<<"**********"<<endl;
	}
awt=awt/n;
atat=atat/n;
cout<<"AWT :"<<awt<<endl<<"ATAT :"<<atat;
return 0;	
}