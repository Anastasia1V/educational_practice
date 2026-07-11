#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

using ll = long long;

int main() {
    ll n;
    cin >> n;
    vector<vector<ll>> c(n, vector<ll>(n));
    for (ll i = 0; i < n; ++i) {
        for (ll j = 0; j < n; ++j) {
            cin >> c[i][j];
        }
    }
    ll max_mask = 1 << n;
    vector<vector<ll>> dp(max_mask, vector<ll>(n, 0));
    for (ll i = 0; i < n; ++i) {
        dp[1 << i][i] = 1;
    }
    for (ll mask = 1; mask < max_mask; ++mask) {
        for (ll i = 0; i < n; ++i) {
            if (dp[mask][i] == 0) {
                continue;
            }
            for (ll j = 0; j < n; ++j) {
                if (((1 << j) & mask) != 0) {
                    continue;
                }
                if (c[i][j] == 0) {
                    continue;
                }
                dp[mask | (1 << j)][j] += dp[mask][i];
            }
        }
    }
    ll ans = 0;
    for (ll i = 0; i < n; ++i) {
        ans += dp[max_mask - 1][i];
    }
    cout << ans << "\n";
    return 0;
}
