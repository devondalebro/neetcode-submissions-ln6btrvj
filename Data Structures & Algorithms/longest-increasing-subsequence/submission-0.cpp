class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        std::vector<int> dp(nums.size(), 1);
        auto ret{1};
        for (auto i{static_cast<int>(nums.size()) - 2}; i >= 0; i--) {
            auto val{1};
            for (auto j{i + 1}; j < nums.size(); ++j) {
                if (nums[j] <= nums[i]) {
                    continue;
                }
                val = std::max(val, dp[j] + 1);
            }
            dp[i] = val;
            ret = std::max(ret, val);
        }
        return ret;
    }
};
