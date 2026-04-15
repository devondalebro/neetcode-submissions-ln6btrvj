class Solution {
public:
    int findMin(vector<int> &nums) {
        auto l{0};
        auto r{static_cast<int>(nums.size()) - 1};
        while (l < r) {
            auto m{l + (r - l) / 2};
            if (nums[l] < nums[m] && nums[m] < nums[r]) {
                // whole thing must be sorted
                return nums[l];
            } else if (l == m) {
                return min(nums[l], nums[r]);
            } else if (nums[l] < nums[m]) {
                l = m + 1;
            } else {
                r = m;
            }
        }
        return nums[r];
    }
};
