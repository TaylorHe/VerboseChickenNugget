//#include <bits/stdc++.h>
#include <string>
#include <iostream>
#include <vector>
#include <math.h>
using namespace std;

vector<string> split_string(string);
typedef long long ll;

ll rd = 5294212309;
ll rq = 9743212277;
ll d = 2820254141;
ll q = 3518047817;

ll rabin_hash(string s) {
    // unsigned int l = s.length();
    ll p = 0;
    for (char c : s) {
        p = (rd * p + int(c)) % rq;
    }
    return p;
}

vector<int> rabin_karp_search(string pattern, string s) {
    ll h = 1;
    int m = pattern.length();
    int n = s.length();
    for (int i = 0; i < m-1; ++i) {
        h = (d * h) % q;
    }
    vector<int> result;
    ll p = 0;
    ll t = 0;
    for (int i = 0; i < m; ++i) {
        p = (d*p + int(pattern[i])) % q;
        t = (d*t + int(s[i])) % q;
    }
    for (ll k = 0; k <= n-m; ++k) {
        if (p == t) {
            bool match = true;
            for (ll i = 0; i < m; ++i) {
                if (pattern[i] != s[k+i]) {
                    match = false;
                    break;
                }
            }
            if (match) {
                result.push_back(k);
            }
        }
        if (k < n-m) {
            t = (t-h*int(s[k]))%q;
            t = (t*d+int(s[k+m]))%q; 
            t = (t+q)%q;
        }
    }
    // for (int i = 0; i < result.size(); i++) {
    //     cout << result[i];
    // }
    // cout << " END" << endl;
    // cout << result[0];
    return result;
}

/*
 * Complete the buildString function below.
 */
int buildString(int a, int b, string s) {
    /*
     * Write your code here.
     */
    int l = s.length();
    int *cost = new int[l+1];

    int copy_length = min(1, int(floor(float(b)/a)));
    int MAX_INT = 2147483647; 
    
    fill_n(cost, l+1, MAX_INT);
    cost[0] = 0;

    for (int i = 1; i < s.length()+1; ++i) {
        cost[i] = min(cost[i], cost[i-1] + a);
        int j = copy_length;
        // Something is wrong here
        while (j <= i && i < l - j && 
            s.substr(0, i).find(s.substr(i,j)) != string::npos
            // rabin_karp_search(s.substr(i, j), s.substr(i)).size() != 0
            ) {
            cost[i+j] = min(cost[i+j], cost[i] + b);
            ++j;
        }
    }
    // int ret = cost[l];
    for(int i = 0; i < l+1; i++) {
        cout << cost[i] << " ";
    }
    cout << endl;
    //delete[] cost;
    return cost[l-1];
}

int main() {
    // ofstream fout(getenv("OUTPUT_PATH"));

    int t;
    cin >> t;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    for (int t_itr = 0; t_itr < t; t_itr++) {
        string nab_temp;
        getline(cin, nab_temp);

        vector<string> nab = split_string(nab_temp);

        // int n = stoi(nab[0]);

        int a = stoi(nab[1]);

        int b = stoi(nab[2]);

        string s;
        getline(cin, s);

        int result = buildString(a, b, s);
        cout << result << endl;
    }

    // fout.close();

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
