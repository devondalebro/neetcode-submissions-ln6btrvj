class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> ret{};
        ret.reserve(nums.size());
        auto product{1};
        auto zeros{0};
        for (const auto &n :nums) {
            if (n != 0) product *= n;
            else zeros++;
        }
        if (zeros > 1) {
            for (auto i{0}; i < nums.size(); ++i) {
                ret.push_back(0);
            }
            return ret;
        }
        for (const auto &n : nums) {
            if (n == 0) {
                ret.push_back(product);
            } else {
                if (zeros) {
                    ret.push_back(0);
                } else {
                    ret.push_back(product / n);
                }
            }
        }
        return ret;
    }
};
