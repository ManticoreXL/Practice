#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

vector<pair<int, int>> list;

int main(void)
{
	int n;
	cin >> n;

	int x, y;

	for (int i = 0; i < n; i++)
	{
		cin >> x >> y;
		list.push_back({ x, y });
	}

	sort(list.begin(), list.end());

	for (int i = 0; i < n; i++)
	{
		cout << list[i].first << " " << list[i].second << '\n';
	}

	return 0;
}