class Solution {
public:
    std::vector<int> minInterval(std::vector<std::vector<int>>& intervals, std::vector<int>& queries) {
        std::vector<std::pair<int, int>> qSorted{};
        for (auto i{0}; i < queries.size(); ++i) {
            qSorted.push_back({i, queries[i]});
        }
        std::sort(qSorted.begin(), qSorted.end(), [](const auto& q1, const auto& q2) {
            return q1.second < q2.second;
        });

        std::sort(intervals.begin(), intervals.end(), [](const auto& i1, const auto& i2) {
            return i1[0] < i2[0];
        });

        auto cmp = [](const auto& i1, const auto &i2) {
            if (i1[1] - i1[0] + 1 != i2[1] - i2[0] + 1) {
                return i1[1] - i1[0] + 1 > i2[1] - i2[0] + 1;
            }
            return i1[1] > i2[1];
        };

        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, decltype(cmp)> pq(cmp);
        auto i{0}; 
        for (const auto &q : qSorted) {
            while (i < intervals.size() && intervals[i][0] <= q.second) {
                pq.push(intervals[i]);
                ++i;
            }
            while (pq.size() && pq.top()[1] < q.second) {
                pq.pop();
            }
            if (!pq.size()) {
                queries[q.first] = -1;
            } else {
                queries[q.first] = pq.top()[1] - pq.top()[0] + 1; 
            }
        }
        return queries;
    }
};

