class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        vector<vector<int>> ret{};
        auto i{0};
        std::sort(intervals.begin(), intervals.end(), [](const auto& i1, const auto& i2) {
            return i1[0] < i2[0];
        });
        ret.push_back(intervals[0]);
        for (auto i{1}; i < intervals.size(); ++i) {
            if (intervals[i][0] <= ret.back()[1]) {
                ret.back()[1] = std::max(ret.back()[1], intervals[i][1]);
            } else {
                ret.push_back(intervals[i]);
            }
        }
        return ret;
    }
};
