class Solution {
public:
    vector<vector<string>> doPartition(int start, const string& s, const vector<vector<bool>>& isPalinMap) {
        if (start == s.size()) return {{}};
        auto end{start};
        vector<vector<string>> ret{};
        while (end < s.size()) {
            if (isPalinMap[start][end]) {
                for (auto &comb : doPartition(end + 1, s, isPalinMap)) {
                    comb.insert(comb.begin(), s.substr(start, end - start + 1));
                    ret.push_back(comb);
                }
            }
            end++;
        }
        return ret;
    }

    vector<vector<string>> partition(string s) {
        vector<vector<bool>> isPalinMap(s.size(), vector<bool>(s.size(), false));
        for (auto i{0}; i < s.size(); ++i) {
            auto l{i}, r{i};
            auto isPalin{true};
            while (l >= 0 && r < s.size() && isPalin) {
                isPalinMap[l][r] = isPalin = s[l] == s[r];
                l--;
                r++;
            }
            l = i;
            r = i + 1;
            isPalin = true;
            while (l >= 0 && r < s.size() && isPalin) {
                isPalinMap[l][r] = isPalin = s[l] == s[r];
                l--;
                r++;
            }
        }
        return doPartition(0, s, isPalinMap);
    }
};
