#include<iostream>
using namespace std;

int main(void)
{
	int test;
	cin >> test;

	for (int i = 0; i < test; i++)
	{
		int result = 1;
		int n = 0;
		int m = 0;

		cin >> n >> m;

		int r = 1;
		for (int j = m; j > m-n; j--)
		{
			result = result * j;
			result = result / r;
			r++;
		}

		cout << result << endl;
	}

	return 0;
}