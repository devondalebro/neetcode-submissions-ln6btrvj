class Solution {
public:
    int robAux(int houses, int start, vector<vector<int>>& dp, vector<int>& nums) {
        if (houses == 0) {
            dp[houses][start] = 0;
        } else if (dp[houses][start] >= 0) {
            return dp[houses][start];
        } else if (houses == 1) {
            dp[houses][start] = nums[houses - 1 + start];
        } else {
            dp[houses][start] = max(robAux(houses - 1, start, dp, nums), robAux(houses - 2, start, dp, nums) + nums[houses - 1 + start]);
        }
        return dp[houses][start];
    }
    int rob(vector<int>& nums) {
        int houses = nums.size();
        vector<vector<int>> dp(nums.size() + 1, vector<int>(2, -1));
        if (houses == 1) {
            return nums[0];
        }
        return max(robAux(houses - 1, 0, dp, nums), robAux(houses - 1, 1, dp, nums));
    }
};
