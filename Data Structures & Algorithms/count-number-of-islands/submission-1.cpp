class Solution {
public:
    array<array<int, 2>, 4> dirs{{{0, 1}, {1, 0}, {0, -1}, {-1, 0}}};
    int dfs(int i, int j, vector<vector<bool>>& visited, const vector<vector<char>>& grid) {
        if (i < 0 || i == grid.size() || j < 0 || j == grid[0].size()) return 0;
        if (visited[i][j] || grid[i][j] == '0') return 0;
        visited[i][j] = true;
        for (const auto[di, dj] : dirs) {
            dfs(i + di, j + dj, visited, grid);
        }
        return 1;
    }
    int numIslands(vector<vector<char>>& grid) {
        vector<vector<bool>> visited(grid.size(), vector<bool>(grid[0].size(), false));
        auto islands{0};
        for (auto i{0}; i < grid.size(); ++i) {
            for (auto j{0}; j < grid[0].size(); ++j) {
                islands += dfs(i, j, visited, grid);
            }
        }
        return islands;
    }
};
