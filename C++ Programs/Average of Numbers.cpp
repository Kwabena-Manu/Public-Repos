#include <iostream>
using namespace std;
int main()
{
	double sum_of_numbers,num,x = 0;
	double average;
	cout<<"Enter number: ";
	cin>> num;
	
	while (x <= num)
	{
		sum_of_numbers = sum_of_numbers + x;
		x++;
	}
	
	average = sum_of_numbers / num;
	
	cout<<"The average = "<<average<<endl;
	
	
	
	
	
}
