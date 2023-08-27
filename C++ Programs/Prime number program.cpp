#include <iostream>
using namespace std;
int main()
{
	cout << " this is all going down to a first class plan"<<endl;
	int n,t = 0,i;
	cout << "Please enter n"<<endl;
	cin >>n;
	
	if (n <= 0 || n == 1)
	{
		cout << "This is not close to becoming a prime number so suck it"<<endl;
	}
	else 
	{
	
		for (i = 2; i <= (n/2);i ++)
		{
			if (n % i == 0)
			{
				t = 1;
				break;
			}
	
		}
		if (t == 0)
		{
			cout << n << " is a prime number. ";
		}
		else
		{
			cout<< n <<" isn't a prime number.";
		}
	}
	
}
