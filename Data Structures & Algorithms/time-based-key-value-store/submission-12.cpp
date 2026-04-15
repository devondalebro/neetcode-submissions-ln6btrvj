class TimeMap {
    struct Pair {
        string val;
        int time;
    };

    unordered_map<string, vector<Pair>> vals_{};
public:
    TimeMap() {}
    
    void set(string key, string value, int timestamp) {
        vals_[key].emplace_back(value, timestamp);
    }
    
    string get(string key, int timestamp) {
        auto valsVecIt{vals_.find(key)};
        if (valsVecIt == vals_.end()) {
            return "";
        } 
        const auto& vals{valsVecIt->second};
        if (vals[0].time > timestamp) return "";
        auto l{0}; 
        auto r{static_cast<int>(valsVecIt->second.size()) - 1};
        while (l < r) {
            auto m{l + (r - l + 1) / 2};
            if (vals[m].time == timestamp) {
                return vals[m].val;
            } else if (timestamp < vals[m].time) {
                r = m - 1;
            } else {
                l = m;
            }
        }
        return vals[l].val;
    }
};
