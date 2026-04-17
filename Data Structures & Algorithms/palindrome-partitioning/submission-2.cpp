class Solution {
public:
    bool isPalindrome(const string& s) {
        auto l{0};
        auto r{s.size() - 1};
        while (l < r) {
            if (s[l] != s[r]) return false;
            l++;
            r--;
        }
        return true;
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
