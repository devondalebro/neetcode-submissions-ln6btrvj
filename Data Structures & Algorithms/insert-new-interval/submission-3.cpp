class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals, vector<int>& newInterval) {
        vector<vector<int>> ret{};
        const int start{newInterval[0]}, end{newInterval[1]};
        bool checkBack{false};
        if (!intervals.size()) {
            intervals.push_back(newInterval);
            return intervals;
        }
        vector<int> prev{0, 0};

        bool newAdded {false};
        for (auto i{0}; i < intervals.size(); ++i) {
            if (newAdded) {
                ret.push_back(intervals[i]);
                continue;
            }
            const auto& curr {intervals[i]};
            if (curr[1] < start) {
                ret.push_back(curr);
                continue;
            } else if (curr[0] > end) {
                ret.push_back(newInterval);
                ret.push_back(curr);
            } else if (start < curr[0]) {
                if (end < curr[1]) {
                    ret.push_back({start, curr[1]});
                } else {
                    int temp = i;
                    while (temp < intervals.size()) {
                        if (end < intervals[temp][0]) {
                            ret.push_back(newInterval);
                            i = temp;
                            break;
                        } else if (end < intervals[temp][1]) {
                            ret.push_back({start, intervals[temp][1]});
                            i = temp;
                            break;
                        } else if (end >= intervals[temp][1] && temp == intervals.size() - 1) {
                            ret.push_back({start, end});
                            i = temp;
                        }
                        temp++;
                    }
                }
            } else if (start >= curr[0]) {
                if (end <= curr[1]) { 
                    ret.push_back({curr[0], curr[1]});
                } else {
                    int temp = i;
                    while (temp < intervals.size()) {
                        if (end < intervals[temp][0]) {
                            ret.push_back({curr[0], end});
                            break;
                        } else if (end <= intervals[temp][1]) {
                            ret.push_back({curr[0], intervals[temp][1]});
                            i = temp;
                            break;
                        } else if (end > intervals[temp][1] && temp == intervals.size() - 1) {
                            ret.push_back({curr[0], end});
                        }
                        i = temp;
                        temp++;
                    }
                }
            }
            newAdded = true;
        }
        if (!newAdded) {
            ret.push_back(newInterval);
        }
        return ret;
    }
};
