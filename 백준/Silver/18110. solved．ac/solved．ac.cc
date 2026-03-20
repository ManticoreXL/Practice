#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
using namespace std;

int main(void)
{
	int n;
	int res = 0;
	double sum = 0;

	cin >> n;

	if (n == 0)
	{
		cout << res;
		return 0;
	}

	vector<int> v(n);
	for (int i = 0; i < n; i++)
		cin >> v[i];

	sort(v.begin(), v.end());

	int trim = round(n * 0.15);

	for (int i = trim; i < n - trim; i++)
		sum += v[i];

	res = round(sum / (n - trim * 2));

	cout << res;

	return 0;
}