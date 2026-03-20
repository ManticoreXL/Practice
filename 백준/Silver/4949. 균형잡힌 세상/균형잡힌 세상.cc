#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<stack>
using namespace std;

int main(void)
{
	while(true)
	{
		string input;

		getline(cin, input);

		if (input[0] == '.')
		{
			break;
		}

		stack<char> stk;

		for (int i = 0; i < input.length(); i++)
		{
			if (input[i] == '(' || input[i] == '[')
				stk.push(input[i]);
			else if (input[i] == ')')
			{
				if (stk.empty() || stk.top() == '[')
				{
					cout << "no" << endl;
					break;
				}
				stk.pop();
			}
			else if (input[i] == ']')
			{
				if (stk.empty() || stk.top() == '(')
				{
					cout << "no" << endl;
					break;
				}
				stk.pop();
			}
			else if (input[i] == '.')
			{
				if (stk.empty())
				{
					cout << "yes" << endl;
				}
				else
					cout << "no" << endl;
			}
		}
	}

	return 0;
}