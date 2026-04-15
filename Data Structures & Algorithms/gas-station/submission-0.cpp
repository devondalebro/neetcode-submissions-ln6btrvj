class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        auto gasSum{std::accumulate(gas.begin(), gas.end(), 0)};
        auto costSum{std::accumulate(cost.begin(), cost.end(), 0)};
        if (gasSum - costSum < 0) return -1;
        auto fuel{0}, start{0}, curr{0}, end{static_cast<int>(cost.size() - 1)};
        while (true) {
            if (curr == end) {
                return start;
            }
            fuel += gas[curr] - cost[curr];
            curr++;
            if (curr == cost.size()) {
                curr = 0;
            }
            if (fuel < 0) {
                start = curr;
                fuel = 0;
                end = start - 1;
                if (end < 0) end = cost.size() - 1;
            }
        }
        return -1;
    }
};
