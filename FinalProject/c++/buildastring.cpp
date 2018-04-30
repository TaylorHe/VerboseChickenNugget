#include <iostream>
#include <vector>
#include <algorithm>
#include <tuple>
#include <iostream>
#define repeat(i,n) for (int i = 0; (i) < (n); ++(i))
using namespace std;
pair<vector<int>,vector<int> > suffix_array_and_rank(string const & s) { // O(nloglogn)
    int n = s.length();
    vector<int> sa(n+1);
    vector<int> rank(n+1);
    repeat (i,n+1) {
        sa[i] = i;
        rank[i] = i < n ? s[i] : -1;
    }
    for (int k = 1; k <= n; k *= 2) {
        auto compare = [&](int i, int j) {
            int ri = i + k <= n ? rank[i + k] : -1;
            int rj = j + k <= n ? rank[j + k] : -1;
            return make_pair(rank[i], ri) < make_pair(rank[j], rj);
        };
        sort(sa.begin(), sa.end(), compare);
        vector<int> dp(n+1);
        dp[sa[0]] = 0;
        repeat (i,n) dp[sa[i+1]] = dp[sa[i]] + compare(sa[i], sa[i+1]);
        rank = dp;
    }
    return { sa, rank };
}
 
int longest_prefix_length(string const & t, vector<int> const & sa, vector<int> const & rank, int offset) {
    int ans = 0;
    for (int i = rank[offset]; i >= 1; -- i) {
        if (t[sa[i]] != t[offset]) break; // means l is 0
        if (sa[i] <= offset) continue;
        // cout << "t: " << t << endl;
        // cout << "sa[i]: " << sa[i] << endl;
        // cout << "t + sa[i]: " << *(t.begin() + sa[i]) << endl;
        // cout << "t+offset: " << *(t.begin() + offset);
        int l = mismatch(t.begin() + sa[i], t.end(), t.begin() + offset).second - t.begin() - offset;
        cout << "mismatch.second is: " << l << endl;
        //l = l - (t.begin() + offset);
        
        cout << "t.second - (t+offset):"<< l << endl;
        if (l <= ans) break;
        ans = max(ans, min(sa[i] - offset, l));
    }
    for (int i = rank[offset]; i < sa.size(); ++ i) {
        if (t[sa[i]] != t[offset]) break; // means l is 0
        if (sa[i] <= offset) continue;
        int l = mismatch(t.begin() + sa[i], t.end(), t.begin() + offset).second - (t.begin() + offset);
        if (l <= ans) break;
        ans = max(ans, min(sa[i] - offset, l));
    }
    return ans;
}
void solve() {
    int n, a, b; string s; cin >> n >> a >> b >> s;
    string t(s.rbegin(), s.rend());
    vector<int> sa, rank; tie(sa, rank) = suffix_array_and_rank(t);
    vector<int> dp(n+1); // monotonic
    repeat (i,n) {
        dp[i+1] = dp[i] + a;
        int l = longest_prefix_length(t, sa, rank, n-i-1);
        if (l) repeat (j,l) dp[i+1] = min(dp[i+1], dp[i-j] + b);
    }
    cout << dp[n] << endl;
}
int main() {
    int t; cin >> t;
    repeat (i,t) solve();
    return 0;
}