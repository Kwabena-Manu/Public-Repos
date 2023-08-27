#include <iostream>
#include <cmath>
using namespace std;

double sinx2(double q);
double fact(int y);
int main()
{
	double x,b;
	
	
	do
	{
	    cout <<"Please enter x"<<endl;
		cin>>x;
		cout<<endl;
	} while (abs(x) >= 22/14);
	
	b = sinx2(x);
	cout<<"sin sqaured of x is "<<b;

}

double sinx2(double q)
{
	double sinx=0,i=1;
	double prev;
	do
	{
		prev = sinx;
		sinx = sinx + (pow(-1,i+1)*pow(2,2*i-1)* pow(q,2*i)/fact(2*i));
		
		i++;	
	}while (fabs(prev-sinx) >pow(10,-6));
	cout <<i<<endl;
	
	return sinx;
	
}

double fact (int y)
{
	int g=1;
	for (int b=1; b<=y; b++)
	{
		g = g*b;
		
	}
	return g;
}
