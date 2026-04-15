class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        auto ret{0};
        heights.push_back(0);
        stack<pair<int, int>> st{};
        for (auto i{0}; i < heights.size(); ++i) {
            auto index{i};
            while (!st.empty() && heights[i] < st.top().second) {
                ret = std::max(ret, (i - st.top().first) * st.top().second);
                index = st.top().first;
                st.pop();
            }
            st.push({index, heights[i]});
        }
        return ret;
    }
};
