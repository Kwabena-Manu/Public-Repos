#include <iostream>
#include <cmath>
using namespace std;
int tobn(int y, int z);
int main()
{
	int baseans;
	cout<<"Please enter the number x in base 10"<<endl;
	int x;
	cin>>x;
	
	int m;
	cout<<endl<<"Please enter the base to convert x to"<<endl;
	cin>>m;
	while (m<2 && m>9 && m!=16)
	{
		cout<<endl<<"Please m should be from(2-9) or (16)"<<endl;
		cin>>m;
		
		cout<<endl;
	}
	baseans= tobn(x,m);
	cout<<x<<" in base "<<m<<" is "<<baseans;
}

int tobn(int y, int z)
{
	int ans= 0,a=0;
	int baseb;
	while (y>0)
	{
		
		baseb = y%z;
		y = y/z;
	
		ans = ans + (baseb*pow (10,a));
		a++;
	}
	return ans;
}

