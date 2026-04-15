class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        unordered_map<int, int> count{};
        auto ret{0};
        for (const auto &n : nums) {
            if (count[n] != 0) continue;
            auto tCount{1 + count[n - 1] + count[n + 1]};
            ret = max(ret, tCount);
            count[n - count[n - 1]] = count[n + count[n + 1]] = count [n] = tCount;
            std::cout << "for number " << n << " its " << ret << "\n";
        }
        return ret;
    }
};
