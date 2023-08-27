#include <iostream>
#include <string>
#include <cctype>
using namespace std;
int main()
{
	int shifts;
	string word;
	char check;
	string  newword;
	
	cout<<"Enter the word / sentence to be encrypted: ";
	getline (cin, word);
	
	cout<<endl<<endl<<"Enter the number of shifts: ";
	cin>>shifts;
	
	
	
	
	for (int i =0;i<word.length();i++) // word.length() outputs the number of characters in the word/senetence
	{
		check = word[i]; // the ith character in the word/sentence is placed in check
		int tmp;
		tmp = int (check); // the ASCII number of the character in check is placed in tmp. This is also an explicit type casting.
		
		tmp = tmp - shifts; // the ASCII number is decreased by the number of shifts specified
		check = char(tmp); //explicit type casting / explicit type conversion. The resulting ASCII number in tmp is converted to char and placed backk in check
		newword +=check; // newword and the character in check  and the string in newword are concatenated
		
	}
	
	cout<<endl<<"word/ sentence: "<<word<<endl; //outputs the word /sentence entered
	cout<<endl<<"New word/ new sentence: "<<newword<<endl; // outputs the new encrypted word/sentence
	
	
	
}
