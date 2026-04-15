class Solution {
public:
    int findMin(vector<int> &nums) {
        auto l{0};
        auto r{static_cast<int>(nums.size() - 1)};
        while (l < r) {
            auto m{l + (r - l) / 2};
            if (nums[l] < nums[r]) {
                return nums[l];
            }
            if (nums[l] < nums[m]) {
                l = m + 1;
            } else if (nums[m] < nums[r]) {
                r = m;
            } else {
                return std::min(nums[l], nums[r]);
            }
        }
        return nums[l];
    }
};
