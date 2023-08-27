#include <iostream>
#include <cmath>
using namespace std;
int x[1000],y[1000];
int main()
{
	int n;
	double sumx =0,sumy=0,sum1=0,sumx2=0;
	double a,b;
	cout<<"Please enter n"<<endl;
	cin>>n;
	for (int i = 1; i<=n;i++)
	{
		cout<<"Enter x"<<i<<" and y"<<i<<endl;
		cin>>x[i]>>y[i];
		cout <<endl;
	}
	for (int c= 1; c<=n; c++)
	{
		
		sum1 = sum1 + x[c]*y[c];
		
		sumx = sumx + x[c];
	
		sumy = sumy +y[c];
		
		sumx2 = sumx2 + pow(x[c],2);
		
	}
	
	
		b = (sum1-((sumx*sumy)/n))/((sumx2 - pow(sumx,2))/n);
		
		a =(sumy- (b*sumx))/n;

	
	if (b<0)
	{
		cout<<"the equation of the line is "<<"y = "<< a<<"x"<< b;
	}
	else
	{
		cout <<"the equation of the line is "<<"y ="<<a<<"x"<<b;
	}
	
	/* Not completely right*/
}
