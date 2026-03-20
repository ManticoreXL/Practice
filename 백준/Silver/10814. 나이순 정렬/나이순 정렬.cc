#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

bool paircmp(pair<int, string> a, pair<int, string> b)
{
	// 나이가 같은 경우 정렬 X
	// 다른 경우 나이순 정렬
	if (a.first == b.first)
		return false;
	else
		return a.first < b.first;
}

vector<pair<int, string>> list;

int main(void)
{
	int n;
	cin >> n;
	
	for (int i = 0; i < n; i++)
	{
		int age;
		string name;
		cin >> age >> name;

		list.push_back(make_pair(age, name));
	}

	stable_sort(list.begin(), list.end(), paircmp);

	for (int i = 0; i < n; i++)
	{
		cout << list[i].first << " " << list[i].second << "\n";
	}
}