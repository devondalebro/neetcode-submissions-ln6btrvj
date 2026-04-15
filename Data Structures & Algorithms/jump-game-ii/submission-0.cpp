class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> dp(nums.size(), -1);
        dp[0] = 0;
        for (auto i{0}; i < nums.size(); ++i) {
            if (dp[i] == -1) continue; 
            for (auto j{1}; j <= nums[i] && i + j < nums.size(); ++j) {
                if (dp[i + j] == -1) {
                    dp[i + j] = dp[i] + 1;
                } else {
                    dp[i + j] = min(dp[i + j], dp[i] + 1);
                }
            }
        }
        return dp[nums.size() - 1];
    }
};
