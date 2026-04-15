class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        // brute force is just O(n^2)
        heights.push_back(0);
        auto ret{0};
        stack<pair<int, int>> past{};
        // index, number
        for (auto i{0}; i < heights.size(); ++i) {
            auto lastIdx{i};
            while (!past.empty() && past.top().second > heights[i]) {
                ret = max(ret, (i - past.top().first) * past.top().second);
                lastIdx = past.top().first;
                past.pop();
            }
            past.emplace(lastIdx, heights[i]);
        }
        return ret;
    }
};
