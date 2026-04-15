class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        std::bitset<10000> bits{};
        for (const auto &n : nums) {
            if (bits[n - 1]) return n;
            else bits[n - 1] = 1;
        }
        return 0;
    }
};
