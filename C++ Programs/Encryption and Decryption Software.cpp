#include <iostream>
#include <string>
#include <cctype>
using namespace std;
void encrypt();
void decrypt();

int main()
{
	int choice;
	
	do
	{
		cout<<"\n\nEnter 1 to encrypt and 2 to decrypt!!!"<<"\n\n\nEnter choice: ";
		cin>>choice;
		
	}while(choice < 1 || choice  >2);
	
	
	
	if (choice ==1)
	{
		cout<<"\n\n---------------Encryption Beginning----------------------\n\n";
		encrypt();
	}
	else
	{
		cout<<"\n\n---------------Decryption Beginning----------------------\n\n";
		decrypt();
	}
	
	
}

void encrypt()
{
	int shifts;
	string word;
	char check;
	string  newword ="";
	
	cout<<"Enter the word / sentence to be encrypted: ";
	cin.get();
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

void decrypt()
{
	int shifts;
	string encryptedWord;
	char check;
	string  originalWord ="";
	
	cout<<"Enter the word / sentence to be decrypted: ";
	cin.get();
	getline (cin, encryptedWord);
	
	cout<<endl<<endl<<"Enter the number of shifts: ";
	cin>>shifts;
	
	
	
	
	for (int i =0;i<encryptedWord.length();i++) // word.length() outputs the number of characters in the word/senetence
	{
		check = encryptedWord[i]; // the ith character in the word/sentence is placed in check
		int tmp;
		tmp = int (check); // the ASCII number of the character in check is placed in tmp. This is also an explicit type casting.
		
		tmp = tmp + shifts; // the ASCII number is decreased by the number of shifts specified
		check = char(tmp); //explicit type casting / explicit type conversion. The resulting ASCII number in tmp is converted to char and placed backk in check
		originalWord +=check; // newword and the character in check  and the string in newword are concatenated
		
	}
	
	
	cout<<endl<<"Encrypted word/ sentence: "<<encryptedWord<<endl; //outputs the word /sentence entered
	cout<<endl<<"Original word/ new sentence: "<<originalWord<<endl; // outputs the new encrypted word/sentence
}
