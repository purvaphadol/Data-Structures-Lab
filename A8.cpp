/*
FDS Assignment-8

Que. Write C++ program for storing binary number using doubly linked lists. Write functions-
a) To compute 1‘s and 2‘s complement
b) Add two binary numbers
*/

#include<iostream>
using namespace std;
class node
{
	public:
		node *prev, *next;
		int bit;
};
class doubly
{
	public:
	int length;
	node *create();
	node *head, *tail;
	doubly()
	{
		head=tail=NULL;
		length++;
	}
	void appendlast();
	void display();
	void onescomplement();
	void twoscomplement();
};

node *doubly::create()
{
	int value;
	node *temp;
	temp=new node;
	if(temp==NULL)
	{
		cout<<"\nMemory full\n";
	}
	else
	{
L:		cout<<"\nEnter the binary bit:\n";
		cin>>value;
		if(value!=1 && value!=0 && value!=-1)
		{
			cout<<"\nPlease enter a valid bit.\n";
			goto L;
		}
		temp -> prev=NULL;
		temp -> bit=value;
		temp -> next=NULL;
	}
	return temp;
}
void doubly::appendlast()
{
	node *temp;
	cout<<"\nEnter the binary number(Enter -1 to stop)\n";
	while(1)
	{
		temp=create();
		if(temp -> bit==-1)
		{
			break;
		}
		if (head==NULL)
		{
			head=temp; 
			tail=temp;
		}
		else
		{
			tail -> next=temp;
			temp -> prev=tail;
			tail=temp;
		}
		length++;
	}
}
void doubly::display()
{
	node *current;
	current=head;
	while(current!=NULL)
	{
		cout<<current->bit;
		current=current->next;
	}
}
void doubly::onescomplement()
{
	node *current;
	current=head;
	while(current!=NULL)
	{
		if(current ->bit==0)
		{
			current -> bit=1;
		}
		else
		{
			current -> bit=0;
		}
		current=current ->next;
	}
}
void doubly::twoscomplement()
{
	int flag=0;
	node*current;
	current=tail;
	while(current!=NULL)
	{
		if(flag==0)
		{
			if(current -> bit==1)
			{
				flag=1;
			}
		}
		else
		{
			if(current ->bit==0)
			{	
				current ->bit=0;
			}
		}
		current=current->prev;
	}
}

int main()
{
	doubly dl;
	cout<< "\nAppend last.\n";
	dl.appendlast();
	cout<<"\nOnes complement:\n";
	dl.onescomplement();
	dl.display();
	cout<<"\nTwos complement:\n";
	dl.twoscomplement();
	dl.display();
	return 0;
}

/*
Output

Append last.

Enter the binary number(Enter -1 to stop)

Enter the binary bit:
1

Enter the binary bit:
0

Enter the binary bit:
1

Enter the binary bit:
-1

Ones complement:
010
Twos complement:
010

*/

