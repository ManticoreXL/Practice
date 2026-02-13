#include <iostream>
#include <cmath>
using namespace std;

int dp[41];

void fibo(int n)
{   
    if (n == 0)
        cout << 1 << " " << 0 << endl;
    else if (n == 1)
        cout << 0 << " " << 1 << endl;
    else
        cout << dp[n - 1] << " " << dp[n] << endl;
}

int main(void)
{
    // base case
    dp[0] = 0;
    dp[1] = 1;
    dp[2] = 1;

    // initialize dp table
    for (int i = 2; i < 41; i++)
        dp[i] = dp[i - 1] + dp[i - 2];

    // test case
    int c;
    cin >> c;

    for (int i = 0; i < c; i++)
    {
        int n;
        cin >> n;
        fibo(n);
    }

    return 0;
}