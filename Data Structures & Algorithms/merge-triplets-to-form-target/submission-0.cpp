class Solution {
public:
    bool mergeTriplets(vector<vector<int>>& triplets, vector<int>& target) {
        vector<int> og{0, 0, 0};
        auto temp{0};
        for (const auto& t : triplets) {
            auto valid{true};
            for (auto i{0}; i < 3; ++i) {
                if (t[i] > target[i]) {
                    valid = false;
                    break;
                }
            }
            if (valid) {
                for (auto i{0}; i < 3; ++i) {
                    og[i] = std::max(og[i], t[i]);
                }
            }
            temp++;
        }
        for (auto i{0}; i < 3; ++i) {
            if (og[i] != target[i]) {
                return false;
            }
        }
        return true;
    }
};
