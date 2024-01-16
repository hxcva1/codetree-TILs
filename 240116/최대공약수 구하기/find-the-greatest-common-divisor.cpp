#include <iostream>

using namespace std;

void maxDiv(int n, int m)
{
    int max = -1;
    int small;
    if (n > m)
        small = m;
    else
        small = n;
    for(int i = 1; i <= small; i++) {
        if (n % i == 0 && m % i == 0) {
            max = i;
        }
    }
    cout << max;
}
int main() {
    // 여기에 코드를 작성해주세요.
    int n, m;
    cin >> n >> m;
    maxDiv(n , m);
    return 0;
}