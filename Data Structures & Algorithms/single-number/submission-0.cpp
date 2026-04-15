class Solution {
public:
    int singleNumber(vector<int>& nums) {
       auto num{nums[0]};
        for (auto i{1}; i < nums.size(); ++i) {
            num ^= nums[i];
        }
        return num;
    }
};
