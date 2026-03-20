#include <iostream>
#include <cmath>
#include <limits>
#include <algorithm>
using namespace std;

string wb[8] = {
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
};
string bw[8] = {
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
};

string board[50];

int wb_count(int x, int y)
{
    int count = 0;
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            if (board[x + i][y + j] != wb[i][j])
                count++;

    return count;
}

int bw_count(int x, int y)
{
    int count = 0;
    for (int i = 0; i < 8; i++)
        for (int j = 0; j < 8; j++)
            if (board[x + i][y + j] != bw[i][j])
                count++;

    return count;
}

int main(void)
{
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++)
        cin >> board[i];

    int min_val = 50000;

    for (int i = 0; i + 8 <= n; i++)
    {
        for (int j = 0; j + 8 <= m; j++)
        {
            int temp = min(wb_count(i, j), bw_count(i, j));
            if (temp < min_val)
                min_val = temp;
        }
    }

    cout << min_val << endl;
    
    return 0;
}