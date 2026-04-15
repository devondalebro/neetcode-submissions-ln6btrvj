class Solution {
public:
    bool traverse(int i, int j, vector<vector<bool>> &visited, int max, const vector<vector<int>>& grid) {
        if (j < 0 || j == grid.size()) {
            return false;
        } else if (i < 0 || i == grid[0].size()) {
            return false;
        } else if (grid[j][i] > max) {
            return false;
        } else if (visited[j][i]) {
            return false;
        } else if (i == grid[0].size() - 1 && j == grid.size() - 1) return true;
        visited[j][i] = true;
        return traverse(i + 1, j, visited, max, grid) || traverse(i, j + 1, visited, max, grid) || traverse(i - 1, j, visited, max, grid) || traverse(i, j - 1, visited, max, grid);
    }
    int swimInWater(vector<vector<int>>& grid) {
        auto max{0};
        auto min{INT_MAX};
        for (const auto &g : grid) {
            for (const auto &c : g) {
                max = std::max(max, c);
                min = std::min(min, c);
            }
        }
        auto low{min};
        auto high{max};
        int mid{};
        auto ret{0};
        vector<vector<bool>> visited(grid.size(), vector<bool>(grid[0].size(), 0));
        while (low < high) {
            mid = (low + high) / 2;
            auto temp{visited};
            if (traverse(0, 0, temp, mid, grid)) {
                high = mid;
            } else { 
                low = mid + 1;
            }
        }
        return high;
    }
};
