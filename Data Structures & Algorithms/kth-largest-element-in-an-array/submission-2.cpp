class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, std::greater<int>> q{};
        for (const auto &n : nums) {
            q.push(n);
            while (q.size() > k) q.pop();
        }
        return q.top();
    }
};
