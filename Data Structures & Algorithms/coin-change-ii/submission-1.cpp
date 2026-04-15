class Solution {
public:
    int change(int amount, vector<int>& coins) {
        if (amount == 0) return 1;
        vector<vector<int>> dp(coins.size(), vector<int>(amount + 1, 0));
        for (auto i{0}; i < coins.size(); ++i) {
            dp[i][0] = 1;
        }
        for (auto a{1}; a <= amount; ++a) {
            for (auto c{0}; c < coins.size(); ++c) {
                for (auto i{c}; i < coins.size(); ++i) {
                    if (coins[c] == a) {
                        dp[c][a] = 1;
                    } else if (a - coins[c] >= 0) {
                        // need to count up all the amounts of a - the current coin
                        dp[c][a] += dp[i][a - coins[c]];
                    }
                }
            }
        }
        auto ret{0}; 
        for (auto i{0}; i < coins.size(); ++i) {
            ret += dp[i][amount];
        }
        return ret;
    }
};
