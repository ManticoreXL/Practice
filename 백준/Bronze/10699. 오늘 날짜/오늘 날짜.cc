#define _CRT_SECURE_NO_WARNINGS
#include<iostream>
#include<cstdio>
#include<ctime>
using namespace std;

int main(void)
{
	time_t timer;
	struct tm* t;
	timer = time(NULL);
	t = localtime(&timer);
	
	int year = 1900 + t->tm_year;
	int month = 1 + t->tm_mon;
	int day = t->tm_mday;

	cout << year << "-";

	if (month < 10)
		cout << "0" << month;
	else
		cout << month;

	cout << "-";

	if (day < 10)
		cout << "0" << day;
	else
		cout << day;

	return 0;
}