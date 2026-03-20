#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main(void)
{
	int n;
	cin >> n;
	
	vector<int> rope(n, 0);

	for (int i = 0; i < n; i++)
		cin >> rope[i];

	sort(rope.rbegin(), rope.rend());

	int curr = 0;

	for (int i = 0; i < n; i++)
	{
		int weight = rope[i] * (i + 1);

		if (weight > curr)
			curr = weight;
	}

	cout << curr << endl;

	return 0;
}