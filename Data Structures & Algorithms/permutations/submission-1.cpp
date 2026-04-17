class Solution {
public:

    void permute(int n, vector<int>& curr, unordered_set<int>& used, const vector<int>& nums) {
        curr.push_back(n);
        used.insert(n);
        if (curr.size() == nums.size()) {
            permutes.push_back(curr);
        } else {
            for (const auto &n : nums) {
                if (used.contains(n)) continue;
                permute(n, curr, used, nums);
            }
        }
        used.erase(n);
        curr.pop_back();
    }
    vector<vector<int>> permutes{};
    vector<vector<int>> permute(vector<int>& nums) {
        vector<int> curr{};
        unordered_set<int> used{};
        for (const auto &n : nums) {
            permute(n, curr, used, nums);
        }
        return permutes;
    }
};
