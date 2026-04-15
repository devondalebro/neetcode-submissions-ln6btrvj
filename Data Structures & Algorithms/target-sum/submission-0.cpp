class Solution {
public:
    int ret{0};
    void sol(int curr, int index, vector<int>& nums, int target) {
        if (index == nums.size()) {
            if (curr == target) ret++;
            return;
        }
        sol(curr + nums[index], index + 1, nums, target);
        sol(curr - nums[index], index + 1, nums, target);
    }
    int findTargetSumWays(vector<int>& nums, int target) {
        sol(0, 0, nums, target);
        return ret;
    }
};
