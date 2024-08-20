/*
FDS Assignment-10

Que. Implement C++ program for expression conversion as infix to postfix and its evaluation using stack based on given conditions:
1. Operands and operator, both must be single character.
2. Input Postfix expression must be in a desired format.
Only '+','-','*'and'/' operators are expected.
*/

#include<iostream>
#include<math.h>
using namespace std;

class stack
{
	private:
		float *stk;
		int top,N;
	public:
		stack(int);
		int stackempty();
		void push(char);
		char pop();
		char peek();
};

stack::stack(int k)
{
    top=-1;
    N=k;
    stk=new float [N];
}

int stack::stackempty()
{
    return top==-1?1:0;
}

void stack::push(char op)
{
    stk[++top]=op;
}

char stack::pop()
{
    return stk[top--];
}
char stack::peek()
{
    return stk[top];   
}

int getprio(char op)
{
    if((op=='+')||(op=='-'))
        return 1;
    else if((op=='*')||(op=='/'))
        return 2;
    else if(op=='^')
        return 3;
    else if((op=='$')||(op=='(')||(op==')'))
        return 0;
}


void infix_to_postfix(char *iexp,char *pexp,stack s)
{
    int i,j;
    char ch;
    i=j=0;
    s.push('$');
    
    while((iexp[i])!='\0')
    {
        ch=iexp[i];
        if((ch>='A')&&(ch<='Z'))
            pexp[j++]=ch;
        else if(ch=='(')
            s.push(ch);
        else if(ch==')')
        {	ch=s.pop();
                while(ch!='(')
                {
                    pexp[j++]=ch;
                    ch=s.pop();      
                }
        }
        else if(getprio(ch)>getprio(s.peek()))
            s.push(ch);
        else
        {
            while(getprio(ch)<=getprio(s.peek()))
                pexp[j++]=s.pop();
            s.push(ch);
        }
        i++;   
    }
    ch=s.pop();
    while(ch!='$')
    {
        pexp[j++]=ch;
        ch=s.pop();   
    }
    //pexp[i]='\0';
}
		
int main()
{
	char iexp[80],pexp[80];
	stack s(10);
	cout<<"\nEnter Infix Expression: ";
	cin>>iexp;
	infix_to_postfix(iexp,pexp,s);
	cout<<"\nPostfix Expression is: "<<pexp;
}


/*
Output

Enter Infix Expression: A*B+C

Postfix Expression is: AB*C+



Enter Infix Expression: A^B*C-C+D/A/(E+F)

Postfix Expression is: AB^C*C-DA/EF+/+

*/

