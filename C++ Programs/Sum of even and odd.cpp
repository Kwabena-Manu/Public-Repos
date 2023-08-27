#include <iostream>
using namespace std;
int main()
{
	int num,even_sum =0,odd_sum=0;
	cout<<"Enter the number: ";
	cin>> num;
	
	for (int i=0; i<=num; i++)
	{
		if (i%2 ==0)
		{
			even_sum = even_sum + i;
		}
		else
		{
			odd_sum = odd_sum + i;
			
			
		}
	}
	
	cout<<"Odd sum = "<<odd_sum <<endl<<"Even_sum = "<< even_sum<<endl<<endl;
}
