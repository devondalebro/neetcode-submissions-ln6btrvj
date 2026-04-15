class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> pres(nums.size());
        vector<int> post(nums.size());
        auto curr{1};
        for (auto i{0}; i < nums.size(); ++i) {
            curr *= nums[i];
            pres[i] = curr;
        }
        curr = 1;
        for (auto i{static_cast<int>(nums.size() - 1)}; i >= 0; --i) {
            curr *= nums[i];
            post[i] = curr;
        }
        vector<int> ret{};
        ret.reserve(nums.size());
        for (auto i{0}; i < nums.size(); ++i) {
            if (i == 0) {
                ret.push_back(post[1]);
            } else if (i == nums.size() - 1) {
                ret.push_back(pres[i - 1] * 1);
            } else {
                ret.push_back(pres[i - 1] * post[i + 1]);
            }
        }
        return ret;
    }
};
