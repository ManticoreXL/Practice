#include<iostream>
using namespace std;

int main(void)
{
	bool attend[31];
	int temp = 0;

	// initialization
	for (int i = 1; i < 31; i++)
		attend[i] = false;

	// input
	for (int i = 0; i < 28; i++)
	{
		cin >> temp;
		attend[temp] = true;
	}

	// find omission number
	for (int i = 1; i < 31; i++)
	{
		if (!attend[i])
			cout << i << endl;
	}

	return 0;
}