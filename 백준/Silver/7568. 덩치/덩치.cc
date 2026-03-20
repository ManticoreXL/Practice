#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
using namespace std;

pair<int, int> list[50];

int main(void)
{
	int n;
	cin >> n;

	for (int i = 0; i < n; i++)
	{
		cin >> list[i].first >> list[i].second;
	}

	int rank = 1;

	for (int i = 0; i < n; i++)
	{
		for (int j = 0; j < n; j++)
		{
			if (list[i].first < list[j].first && list[i].second < list[j].second)
			{
				rank++;
			}
		}
		cout << rank << " ";
		rank = 1;
	}

	return 0;
}