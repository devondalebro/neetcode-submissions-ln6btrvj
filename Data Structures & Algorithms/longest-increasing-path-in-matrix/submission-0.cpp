class Solution {
public:
    int dfs(int i, int j, int prev, vector<vector<int>>& matrix, vector<vector<int>>& dp) {
        if (i < 0 || i == matrix[0].size()) {
            return 0;
        } 
        if (j < 0 ||j == matrix.size()) {
            return 0;
        }
        if (matrix[j][i] <= prev) {
            return 0;
        }
        if (dp[j][i] != -1) {
            return dp[j][i];
        }
        vector<pair<int, int>> dir{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
        for (const auto &d : dir) {
            dp[j][i] = std::max(dp[j][i], 1 + dfs(i + d.first, j + d.second, matrix[j][i], matrix, dp));
        }
        return dp[j][i];
    }

    int longestIncreasingPath(vector<vector<int>>& matrix) {
        vector<vector<int>> dp(matrix.size(), vector<int>(matrix[0].size(), -1));
        auto ret{1};
        for (auto j{0}; j < matrix.size(); ++j) {
            for (auto i{0}; i < matrix[0].size(); ++i) {
                ret = std::max(ret, dfs(i, j, -1, matrix, dp));
            }
        }
        return ret;
    }
};
