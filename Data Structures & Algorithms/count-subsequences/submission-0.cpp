class Solution {
public:
    int sol(int i, int j, const string &s, const string &t, vector<vector<int>> &dp) {
        if (j == t.size()) return 1;
        if (i == s.size()) return 0;
        if (dp[i][j] != -1) return dp[i][j];
        if (s[i] == t[j]) {
            return dp[i][j] = sol(i + 1, j + 1, s, t, dp) + sol(i + 1, j, s, t, dp);
        } else {
            return dp[i][j] = sol(i + 1, j, s, t, dp);
        }
    }
    int numDistinct(string s, string t) {
        vector<vector<int>> dp(s.size(), vector<int>(t.size(), -1));
        auto ret{sol(0, 0, s, t, dp)};
        for (auto i{0}; i < s.size(); ++i) {
            for (auto j{0}; j < t.size(); ++j) {
                std::cout << i << " " << j << " " << dp[i][j] << '\n';
            }
        }
        return ret;
    }
};
