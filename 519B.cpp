#include <iostream>
using namespace std;

int main()
{
	int n,input,i,f=0,s=0,t=0;
	cin>>n;
	int x[n],y[n-1],z[n-2];
	for (i=0;i<n;i++)
	{
		cin>>x[i];
		f=f+x[i];
	}
	for (i=0;i<n-1;i++)
	{
		cin>>y[i];
		s=s+y[i];
	}
	for (i=0;i<n-2;i++)
	{
		cin>>z[i];
		t=t+z[i];
	}
	cout<<f-s<<endl;
	cout<<s-t<<endl;
	return 0;
}