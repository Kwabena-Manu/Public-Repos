#include <iostream>
using namespace std;
int main()
{
	int numoflines,stars,spaces;
	cout<<"Enter the number of lines: ";
	cin>> numoflines;
	
	spaces = numoflines -1; //number of spaces before the first star in the first line 
	
	for (int i =1; i<=numoflines; i++)
	{
		
		for (int a =1 ; a <= spaces; a++)
		{
			cout<<" ";
		}
		stars = i *2 -1; //how many stars to print on each line of the first half of the diamond
		
		for (int a =1 ;a <=stars;a++)
		{
			cout<<"*";
		}
		cout<<endl; 
		spaces -=1;
		
		
		
		
	}
		for (int d = 1; d<= numoflines-1; d++)
		{
			cout<<" ";
		}
		cout<<"*"<<endl;
}
