#include <iostream>
using namespace std;
int main()
{
	double jdays = 0;
	int year[10000],month[10000],day[10000], dif;
	for (int a = 1; a<=2;a++)
	{
		cout <<"Please enter the year "<<a<<endl;
		cin>>year[a];
		cout <<"Please enter the month "<<a<<endl;
		cin>>month[a];
		cout <<"Please enter the day "<<a<<endl;
		cin>>day[a];
		
	}
	dif = year[2]-year[1];
	if (year[2]-year[1] >=2)
	{
		for (int b = year[1]+ 1; b=year[2]-1;b++ )
		{
			if (b%100== 0)
			{
				if (b%400 == 0)
				{
					jdays = jdays +366;
				}
			}
			else if (b%100 != 0)
			{
				if (b%4 == 0)
				{
					jdays = jdays +366;
				}
			}
			else
			{
				jdays = jdays + 365;
			}
		
		}
			
			for(int c = month[1]; c<=12;c++)
			{
				if (c = month[1])
				{
					if (c = 2)
					{
						if (year[1]%100 == 0)
						{
							if (year[1]% 400 == 0)
							{
								jdays = jdays + 29 - day[1];
							}
						}
						else if (year[1]%100 != 0)
						{
							if (year[1]%4 == 0)
							{
								jdays = jdays +29- day[1];
							}
						}
						else
						{
							jdays = jdays +28 - day[1];
						}
					}
					else if (c % 2 == 0)
					{
						jdays = jdays + 30-day[1];
					}
					else
					{
						jdays =jdays +31 -day[1];
					}
					
				}
			
			else if (c %2 == 0 )
			{ 
				jdays = jdays +30;
				
			}
			else 
			{
				jdays = jdays + 31;
			}
		 }
		 
		 if ( year[2]%100 == 0)
		 {
		 	if (year[2 % 400]=0)
		 	{
			 
		 
		 for (int e = 1 ; e<=month[2];e++)
		 {
		 	if (e = 2)
		 	{
			  jdays = jdays +29;
		    }
			else if (e == month[2])
		 	{
		 		jdays = jdays + day[2];
			}
			else if (e%2 == 0)
			{
				jdays = jdays + 30;
			}
			else 
			{
				jdays = jdays +31;
			}
		 }	
		 }
		 }
		 }
		 cout <<endl<<" The number of days between these two days are "<<jdays;
}
		
	
	
