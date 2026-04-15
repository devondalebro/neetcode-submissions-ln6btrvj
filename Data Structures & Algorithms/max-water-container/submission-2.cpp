class Solution {
public:
    int maxArea(vector<int>& heights) {
        auto lo{0};
        auto hi{static_cast<int>(heights.size() - 1)};
        auto ret{0};
        while (lo < hi) {
            ret = max(ret, min(heights[lo], heights[hi]) * (hi - lo));
            if (heights[lo] < heights[hi]) {
                lo++;
            } else {
                hi--;
            }
        }
        return ret;
    }
};
