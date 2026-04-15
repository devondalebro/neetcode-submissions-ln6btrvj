class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        for (auto i{0}; i < nums.size(); ++i) {
            auto n{abs(nums[i])};
            if (nums[n - 1] < 0) return n;
            nums[n - 1] *= -1;
        }
        return 0;
    }
};
