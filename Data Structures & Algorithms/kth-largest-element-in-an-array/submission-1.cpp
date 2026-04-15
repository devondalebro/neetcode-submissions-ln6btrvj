class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int> q{};
        for (const auto &n : nums) {
            q.push(n);
        }
        auto n{0};
        for (auto i{0}; i < k; ++i) {
            n = q.top();
            q.pop();
        }
        return n;
    }
};
