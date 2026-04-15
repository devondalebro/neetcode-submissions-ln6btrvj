class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        for (auto i{0}; i < matrix.size() / 2; ++i) {
            for (auto j{i}; j < matrix.size() - i - 1; ++j) {
                vector<vector<int>> cells{
                    {i, j}, 
                    {matrix.size() - j - 1, i}, 
                    {matrix.size() - i - 1, matrix.size() - j - 1},
                    {j, matrix.size() - i - 1}
                };
                for (auto i{1}; i <= 3; ++i) {
                    swap(matrix[cells[0][0]][cells[0][1]], matrix[cells[1][0]][cells[1][1]]);
                    swap(matrix[cells[0][0]][cells[0][1]], matrix[cells[2][0]][cells[2][1]]);
                    swap(matrix[cells[0][0]][cells[0][1]], matrix[cells[3][0]][cells[3][1]]);
                }
            }
        }
    }
};
