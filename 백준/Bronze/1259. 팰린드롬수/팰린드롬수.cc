#include<iostream>
#include<string.h>
using namespace std;

int main(void)
{
	char str[6] = "99999";
	char rstr[6] = "00000";
	while (1)
	{
		cin >> str;
		if (str[0] == '0')
		{
			exit(0);
		}
		int len = strlen(str);
		if (len == 1)
		{
			cout << "yes" << endl;
			continue;
		}
		for (int i = 0; i < len; i++)
		{
			rstr[i] = str[len - i - 1];
		}
		if (strncmp(str, rstr, len) == 0)
		{
			cout << "yes" << endl;
		}
		else if (strncmp(str, rstr, len)!=0)
		{
			cout << "no" << endl;
		}
	}

	return 0;
}