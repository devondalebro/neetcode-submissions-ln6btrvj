/**
 * Definition of Interval:
 * class Interval {
 * public:
 *     int start, end;
 *     Interval(int start, int end) {
 *         this->start = start;
 *         this->end = end;
 *     }
 * }
 */

class Solution {
public:
    void merge(vector<Interval>& intervals, int& days) {
        vector<Interval> ret{};
        for (auto i{0}; i < intervals.size(); ++i) {
            if (i != 0 && intervals[i].start < intervals[i - 1].end) {
                //re move this
                ret.push_back(intervals[i]);
                intervals[i].end = intervals[i - 1].end;
            }
        }
        if (ret.size()) {
            ++days;
            merge(ret, days);
        }
    }

    int minMeetingRooms(vector<Interval>& intervals) {
        if (!intervals.size()) {
            return 0;
        }

        std::sort(intervals.begin(), intervals.end(), [](const auto& i1, const auto &i2) {
            return i1.start < i2.start;
        });

        auto days{1};
        merge(intervals, days);
        return days;
    }
};
