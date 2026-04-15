class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> count{};
        for (const auto &n : nums) {
            count[n] += 1;
        }
        vector<vector<int>> buckets(nums.size() + 1, vector<int>{});
        for (auto &[n, c] : count) {
            buckets[c].push_back(n);
        }
        vector<int> ret{};
        ret.reserve(k);
        for (auto i{static_cast<int>(buckets.size() - 1)}; i >= 0; --i) {
            if (buckets[i].empty()) continue;
            for (const auto &n : buckets[i]) {
                ret.push_back(n);
                if (ret.size() == k) {
                    return ret;
                }
            }
        }
        return ret;
    }
};
