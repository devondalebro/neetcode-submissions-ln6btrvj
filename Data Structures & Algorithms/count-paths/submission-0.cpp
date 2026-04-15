class Solution {
public:
    int uniquePaths(int m, int n) {
        std::vector<std::vector<int>> ways(m, std::vector<int>(n, 0));
        for (auto i{0}; i < m; ++i) ways[i][0] = 1;
        for (auto i{0}; i < n; ++i) ways[0][i] = 1;
        for (auto i{1}; i < m; ++i) {
            for (auto j{1}; j < n; ++j) {
                ways[i][j] = ways[i][j - 1] + ways[i - 1][j];
            }
        }
        return ways[m - 1][n - 1];
    }
};
