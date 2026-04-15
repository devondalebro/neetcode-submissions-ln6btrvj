class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        std::vector<bool> dp(s.size() + 1, false);

        std::string_view sView{s};
        dp[0] = true;
        for (auto i{1}; i <= s.size(); ++i) {
            if (!dp[i - 1]) {
                continue;
            }
            for (const string_view w: wordDict) {
                if (w.size() > s.size() - i + 1) {
                    continue;
                }
                if (sView.substr(i - 1, w.size()) == w) {
                    dp[i + w.size() - 1] = true;
                }
            }
        }
        return dp[s.size()];
    }
};