#include <iostream>
using namespace std;

int main()
{
	int n,m,count=0,net=1;
	cin>>n>>m;
	while(net>=1)
	{
		net=(n-1)*(m-1);
		n--;
		m--;
		count++;
	}
	if (count%2!=0)
	{
		cout<<"Akshat"<<endl;
	}
	else
	{
		cout<<"Malvika"<<endl;
	}
	return 0;
}