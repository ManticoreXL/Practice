#include<iostream>
using namespace std;

int main(void)
{
	int x = 0;
	cin >> x;

	int result = 0;

	while (x > 0)
	{
		if (x % 2 == 1)
			result++;
		x /= 2;
	}
	
	cout << result;

	return 0;
}