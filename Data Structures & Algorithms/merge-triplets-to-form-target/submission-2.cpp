class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        auto valid{true};
        for (auto i{0}; i < 3; ++i) {
            if (triplets[0][i] > target[i]) {
                valid = false;
                break;
            }
        }
        if (!valid) {
            for (auto i{0}; i < 3; ++i) {
                triplets[0][i] = 0;
            }
        }
        for (auto i{1}; i < triplets.size(); ++i) {
            auto valid{true};
            for (auto j{0}; j < 3; ++j) {
                if (triplets[i][j] > target[j]) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                for (auto j{0}; j < 3; ++j) {
                    triplets[0][j] = std::max(triplets[0][j], triplets[i][j]);
                }
            }
        }
        for (auto i{0}; i < 3; ++i) {
            if (triplets[0][i] != target[i]) {
                return false;
            }
        }
        return true;
    }
};
