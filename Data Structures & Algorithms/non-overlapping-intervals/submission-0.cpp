class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const auto& i1, const auto& i2) {
            return i1[1] < i2[1];
        });
        int ret{0};
        for (auto i{0}; i < intervals.size(); ++i) {
            if (i != 0 && intervals[i][0] < intervals[i - 1][1]) {
                //re move this
                ++ret;
                intervals[i][1] = intervals[i - 1][1];
            }
        }
        return ret;
    }
};
