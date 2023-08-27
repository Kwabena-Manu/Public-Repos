#include <iostream>
using namespace std;
int main()
{
	int b;
	cout<<"Please enter the number of lines of the christmas tree: ";
	cin>> b;
	b=b+b-1;
	for (int a = 1; a <= b; a+=2)
		{
			for (int c = 1; c<=(b-a)/2; c++)
			 cout<<" ";
			for (int d = 1; d<= a; d++)
			{
				cout<<"*";
			}
			cout<<endl;
		}
		for (int d = 1; d<=b/2; d++)
		{
			cout<<" ";
		}
		cout<<"*"<<endl;
} 
