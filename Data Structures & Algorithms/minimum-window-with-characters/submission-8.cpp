class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> count{};
        for (const auto &c : t) {
            count[c]++;
        }
        auto l{0};
        auto r{-1};
        auto remain{t.size()};
        auto minLen{INT_MAX};
        auto retL{-1};
        auto retR{-1};
        while (r < int(s.size())) {
            if (remain == 0) {
                if (r - l + 1 < minLen) {
                    minLen = r - l + 1;
                    retL = l;
                    retR = r;
                }
                auto c{s[l]};
                if (count.find(c) != count.end()) {
                    count[c]++;
                    if (count[c] > 0) {
                        remain++;
                    }
                }
                l++;
            } else {
                // or its invalid
                r++;
                auto c{s[r]};
                if (count.find(c) != count.end()) {
                    count[c]--;
                    if (count[c] >= 0) {
                        remain--;
                    }
                }
            }
        }
        if (retL != -1) {
            return s.substr(retL, minLen);
        } else {
            return "";
        }
    }
};
