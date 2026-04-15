class Solution {
public:
    int networkDelayTime(vector<vector<int>>& times, int n, int k) {
        vector<int> dist(n + 1, INT_MAX);
        unordered_map<int, vector<pair<int, int>>> edge{};
        for (const auto &t : times) {
            edge[t[0]].push_back({t[1], t[2]});
        }
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> minHeap{};
        dist[k] = 0;
        minHeap.push({0, k});
        while (!minHeap.empty()) {
            auto curr{minHeap.top()};
            minHeap.pop();
            for (const auto &dest : edge[curr.second]) {
                if (curr.first + dest.second < dist[dest.first]) {
                    dist[dest.first] = curr.first + dest.second;
                    minHeap.push({dist[dest.first], dest.first});
                }
            }
        }
        auto ret{0};
        for (auto i{1}; i <= n; ++i) {
            if (dist[i] == INT_MAX) return -1;
            ret = max(ret, dist[i]);
        }
        return ret;
    }
};
