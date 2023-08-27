//Obed's Eulers formula question in c++
#include <iostream>
using namespace std;
int main()
{
	double  num,e=0,pre,fact=1;
	pre = e;
	cout<<"Please enter the number"<<endl;
	cin>> num;
	
	
	for (int a=0; a<=num; a++)
	{
		for(int i = 1; i<=a ; i++)
		{
			fact = fact * i;
		}
		if (e -pre != 0.0000001)
		{
			pre = e;
			e = e + (1/fact);
		}
		else
		{
			break;
		}
	}
	cout<<"The euler's whatever of the number is = " << e;
}
