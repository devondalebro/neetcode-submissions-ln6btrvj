class Solution {
public:
    int sol(int i, vector<int>& prices) {
        if (i >= prices.size() - 1) {
            return 0;
        }

        auto ret{0};
        for (auto j{i}; j < prices.size() - 1; ++j) {
            auto max{0};
            for (auto k{j}; k < prices.size(); ++k) {
                if (prices[k] <= prices[j]) {
                    continue;
                }
                max = std::max(max, prices[k] - prices[j] + sol(k + 2, prices));
            }
            ret = std::max(ret, max);
        }
        return ret;
    }
    int maxProfit(vector<int>& prices) {
        return sol(0, prices);
    }
};
