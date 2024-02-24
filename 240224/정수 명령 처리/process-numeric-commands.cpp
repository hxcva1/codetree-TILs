#include <bits/stdc++.h>
using namespace std;
int main() {
    // 여기에 코드를 작성해주세요.
    stack<int> s;
    int n;
    cin >> n;
    string com;
    int num;
    for (int i = 0; i < n; i++){
        cin >> com;
        if (com == "push"){
            cin >> num;
            s.push(num);
        }
        if (com == "size"){
            cout << s.size() << '\n';
        }
        if (com == "empty"){
            cout << s.empty() << '\n';
        }
        if (com == "pop"){
            cout << s.top() << '\n';
            s.pop();
        }
        if (com == "top"){
            cout << s.top() << "\n";
        }

    }
    return 0;
}