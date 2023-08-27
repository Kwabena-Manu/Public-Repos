#include <iostream>
using namespace std;
int main()
{
	int num,size=1;
	for (int i = 1; i<=100; i++)
	{	
	
		for (int b = 1; b<=10000; b = b*10)
		{
			if (i/b != 0)
			{
				size *=10;
			}
		}
		int reverse =0;
		for (int a =10;a<=10000; a=a*10)
		{
		
			if (i/a != 0)
			{
				num = i%a;
				reverse = reverse + num*a;
			}
			
		
		}
		
		cout<<"The reverse of "<<i<<" = "<<reverse<<endl;
	}
}
