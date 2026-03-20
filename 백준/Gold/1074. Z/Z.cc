#include <iostream>
#include <cmath>
using namespace std;

int value = 0;

int zRecursive(int n, int r, int c)
{
    if (n == 0)
        return 0;

    return 2 * (r % 2) + (c % 2) + 4 * zRecursive(n - 1, (int)(r / 2), (int)(c / 2));
}

int main(void)
{
    int n, r, c;
    cin >> n >> r >> c;

    int size = pow(2, n);

    cout << zRecursive(n, r, c) << endl;
        
    return 0;
}