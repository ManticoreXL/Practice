#include<iostream>
using namespace std;

int main(void)
{
	int index;
	cin >> index;

	int i = 1;
	while (index > i)
	{
		index -= i;
		i++;
	}

	if (i % 2 == 1)
		cout << i + 1 - index << "/" << index << endl;
	else
		cout << index << "/" << i + 1 - index << endl;

	return 0;
}