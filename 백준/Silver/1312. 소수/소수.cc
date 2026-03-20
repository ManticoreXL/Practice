#include<iostream>
using namespace std;

int main(void)
{
	int a, b, n;

	cin >> a >> b >> n;

	int result = 0;

	for (int i = 0; i < n; i++)
	{
		if (a < b)
		{
			result = (a * 10) / b;
			a = (a * 10) % b;
		}
		else if (a > b)
		{
			result = a / b;
			a = a % b;
			i--;
		}
		else if (a == 0)
		{
			result = 0;
		}
	}

	cout << result << endl;

	return 0;
}