#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

// a가 b보다 긴지 확인
bool lencmp(string a, string b)
{
	if (a.length() == b.length())
	{
		return a < b;
	}
	else
		return a.length() < b.length();
}

string list[20000];

int main(void)
{
	int n;
	cin >> n;

	// 문자열 입력 받기
	for (int i = 0; i < n; i++)
	{
		cin >> list[i];
	}

	sort(list, list + n, lencmp);

	// 정렬된 순서로 문자열 출력하기
	for (int i = 0; i < n; i++)
	{
		if (list[i] == list[i - 1])
			continue;
		cout << list[i] << endl;
	}

	return 0;
}