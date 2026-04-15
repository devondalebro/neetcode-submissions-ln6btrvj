class Solution {
public:
    bool dp(int i, int sum, int target,vector<int>& nums) {
        if (sum == target) {
            return true;
        } else if (i == nums.size()) {
            return false;
        } else if (sum > target) {
            return false;
        } else {
            return dp(i + 1, sum + nums[i], target, nums) || dp(i + 1, sum, target, nums);
        }
        
    }

    bool canPartition(vector<int>& nums) {
        auto sum{std::accumulate(nums.begin(), nums.end(), 0)};
        if (sum % 2 != 0) {
            return false;
        }
        return dp(0, 0, sum / 2, nums);
    }
};
