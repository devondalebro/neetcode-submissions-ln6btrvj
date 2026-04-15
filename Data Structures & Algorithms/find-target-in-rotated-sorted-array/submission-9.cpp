class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto l{0};
        auto r{static_cast<int>(nums.size()) - 1};
        while (l <= r) {
            auto m{l + (r - l) / 2};
            if (nums[m] == target) {
                return m;
            }else if (nums[l] <= nums[m]) {
                if (target >= nums[l] && target < nums[m]) {
                    r = m - 1;
                } else {
                    l = m + 1;
                }
            } else {
                if (target > nums[m] && target <= nums[r]) {
                    l = m + 1;
                } else {
                    r = m - 1;
                }
            }
        }
        return -1;
    }
};
