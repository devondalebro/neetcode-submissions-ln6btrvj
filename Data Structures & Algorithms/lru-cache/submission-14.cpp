class LRUCache {
    struct KeyVal {
        int key;
        int val;
    };
    unordered_map<int, list<KeyVal>::iterator> keyToValIts_{};
    list<KeyVal> valsList_{};
    int cap_{};
public:
    LRUCache(int capacity) : cap_(capacity) {}
    
    int get(int key) {
        auto valIt{keyToValIts_.find(key)};
        if (valIt == keyToValIts_.end()) return -1;
        auto listValIt{valIt->second};
        valsList_.splice(valsList_.begin(), valsList_, listValIt);
        return listValIt->val;
    }
    
    void put(int key, int value) {
        auto valIt{keyToValIts_.find(key)};
        if (valIt == keyToValIts_.end()) {
            if (valsList_.size() == cap_) {
                // remove the key of the last val from the map
                keyToValIts_.erase(valsList_.back().key);
                auto lastValIt{prev(valsList_.end())};
                keyToValIts_[key] = lastValIt;
                valsList_.back().key = key;
                valsList_.back().val = value;
                valsList_.splice(valsList_.begin(), valsList_, lastValIt);
            } else {
                valsList_.push_front({key, value});
                keyToValIts_[key] = valsList_.begin();
            }
        } else {
            auto listValIt{valIt->second};
            listValIt->val = value;
            valsList_.splice(valsList_.begin(), valsList_, listValIt);
        }
    }
};
