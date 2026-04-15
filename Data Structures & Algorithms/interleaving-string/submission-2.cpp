class Solution {
public:
    bool sol(int strNum, vector<int>index, vector<string>& strs, int i, string target, vector<vector<vector<int>>>& dp) {
        auto currI{index[strNum]};
        int &slot{dp[index[0]][index[1]][strNum]};
        if (slot != -1) {
            return slot;
        } if (currI == strs[strNum].size()) {
            if (i != target.size()) {
                return (slot = 0);
            } else {
                return (slot = 1);
            }
        } else if (strs[strNum][currI] != target[i]) {
            return (slot = 0);
        }
        index[strNum]++;
        return (slot = (sol(!strNum, index, strs, i + 1, target, dp) || sol(strNum, index, strs, i + 1, target, dp)));
    }

    bool isInterleave(string s1, string s2, string s3) {
        if (s1.size() + s2.size() != s3.size()) {
            return false;
        }
        vector<vector<vector<int>>> dp(s1.size() + 1, vector<vector<int>>(s2.size() + 1, vector<int>(2, -1)));
        vector<int> index{0, 0};
        vector<string> strs{s1, s2};
        return sol(0, index, strs, 0, s3, dp) || sol(1, index, strs, 0, s3, dp);
    }
};
