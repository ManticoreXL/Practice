#include<iostream>
#include<vector>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;

char star[3072][6144];

void printStar(int x, int y, int n)
{
	if (n == 3)
	{
		star[x][y] = '*';
		star[x + 1][y - 1] = '*';
		star[x + 2][y - 2] = '*';
		star[x + 2][y - 1] = '*';
		star[x + 2][y] = '*';
		star[x + 2][y + 1] = '*';
		star[x + 2][y + 2] = '*';
		star[x + 1][y + 1] = '*';
	}
	else
	{
		printStar(x, y, n / 2);
		printStar(x + n / 2, y - n / 2, n / 2);
		printStar(x + n / 2, y + n / 2, n / 2);
	}
}

int main(void)
{
	int a[3];

	while (true)
	{
		cin >> a[0] >> a[1] >> a[2];

		if (a[0] == 0 && a[1] == 0 && a[2] == 0)
			break;

		sort(a, a + 3);

		if (((pow(a[0], 2) + pow(a[1], 2)) == pow(a[2], 2)))
			cout << "right" << endl;
		else
			cout << "wrong" << endl;
	}

	return 0;
}