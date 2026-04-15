class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        set<vector<int>> uniq{};
        sort(nums.begin(), nums.end());
        for (auto i{0}; i < nums.size() - 2; ++i) {
            auto lo{i + 1};
            auto hi{static_cast<int>(nums.size() - 1)};
            while (lo < hi) {
                auto sum{nums[lo] + nums[hi]};
                if (sum + nums[i] == 0) {
                    uniq.insert({nums[lo], nums[i], nums[hi]});
                    lo++;
                } else if (sum + nums[i] < 0) {
                    lo++;
                } else {
                    hi--;
                }
            }
        }
        vector<vector<int>> ret{};
        for (const auto &a : uniq) {
            ret.push_back(a);
        }
        return ret;
    }
};
