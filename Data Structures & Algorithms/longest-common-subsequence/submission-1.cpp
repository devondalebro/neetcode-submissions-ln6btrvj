class Solution {
public:
    int getLongest(int i1, int i2, const std::string_view t1, const std::string_view t2, vector<vector<int>> &dp) {
        if (dp[i1][i2] != -1) {
            return dp[i1][i2];
        }
        if (i1 >= t1.size() || i2 >= t2.size()) {
            std::cout << "wtf " << i1 << i2 << "\n";
            dp[i1][i2] = 0;
            return 0;
        }

        if (t1[i1] == t2[i2]) {
            std::cout << "ok" << i1 << i2 << "\n";
            dp[i1][i2] = 1 + getLongest(i1 + 1, i2 + 1, t1, t2, dp);
            return dp[i1][i2];
        } else {
            dp[i1][i2] = std::max(getLongest(i1 + 1, i2, t1, t2, dp), getLongest(i1, i2 + 1, t1, t2, dp));
            return dp[i1][i2];
        }
    }

    int longestCommonSubsequence(string text1, string text2) {
        vector<vector<int>> dp(text1.size() + 1, vector<int>(text2.size() + 1, -1));
        return getLongest(0, 0, text1, text2, dp);
    }
};