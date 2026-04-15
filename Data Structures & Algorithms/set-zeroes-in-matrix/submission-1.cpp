class Solution {
public:
    void setZ(int i, int j, vector<vector<int>>& matrix) {
        for (auto t{0}; t < matrix.size(); ++t) {
            matrix[t][i] = 0;
        }
        for (auto t{0}; t < matrix[0].size(); ++t) {
            matrix[j][t] = 0;
        }
    }
    void setZeroes(vector<vector<int>>& matrix) {
        set<vector<int>> zeros{};
        for (auto j{0}; j < matrix.size(); ++j) {
            for (auto i{0}; i < matrix[0].size(); ++i) {
                if (matrix[j][i] == 0) {
                    zeros.insert({i, j});
                }
            }
        }
        for (const auto &z: zeros) {
            auto i{z[0]};
            auto j{z[1]};
            setZ(i, j, matrix);
        }
    }
};
