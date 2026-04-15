class Solution {
public:
    vector<int> partitionLabels(string s) {
        vector<int> ret{};
        unordered_map<char, std::pair<int, int>> bounds{};
        for (auto i{0}; i < s.size(); ++i) {
            auto c{s[i]};
            if (bounds.contains(c)) {
                bounds[c].second = i;
            } else {
                bounds[c].first = bounds[c].second = i;
            }
        }
        auto currEnd{-1};
        auto currSize{0};
        for (auto i{0}; i < s.size(); ++i) {
            currEnd = std::max(currEnd, bounds[s[i]].second);
            currSize++;
            if (i == currEnd) {
                ret.push_back(currSize);
                currSize = 0;
            }
        }
        return ret;
    }
};
