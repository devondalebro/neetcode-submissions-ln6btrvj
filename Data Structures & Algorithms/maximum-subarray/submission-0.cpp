class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        auto maxSum{INT_MIN};
        auto currSum{0};
        for (const auto &n : nums) {
            currSum = max(n, currSum + n);
            maxSum = max(maxSum, currSum);
        }
        return maxSum;
    }
};
