class Solution {
    unordered_map<string, bool> palinMap;
public:
    bool isPalindrome(const string& s) {
        auto palinMapIt{palinMap.find(s)};
        if (palinMapIt != palinMap.end()) return palinMapIt->second;
        auto l{0};
        auto r{s.size() - 1};
        auto ret{true};
        while (l < r) {
            if (s[l] != s[r]) {
                ret = false;
                break;
            }
            l++;
            r--;
        }
        palinMap[s] = ret;
        return ret;
    }
    vector<vector<string>> doPartition(const string& s, int i) {
        if (i == s.size()) return {{}};
        vector<vector<string>> ret{};
        string curr{};
        for (auto j{i}; j < s.size(); ++j) {
            curr += s[j];
            if (isPalindrome(curr)) {
                for (const auto split : doPartition(s, j + 1)) {
                    vector<string> currSplit{curr};
                    for (const auto p : split) {
                        currSplit.push_back(move(p));
                    }
                    ret.push_back(move(currSplit));
                }
            }
        }
        return ret;
    }
    vector<vector<string>> partition(string s) {
        return doPartition(s, 0);
    }
};
