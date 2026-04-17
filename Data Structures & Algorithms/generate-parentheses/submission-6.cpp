class Solution {
public:
    vector<string> ret{};
    void generate(bool add, int x, string& curr, int n) {
        if (curr.size() == n * 2) {
            ret.push_back(curr);
            return;
        }
        if (add) {
            curr += "(";
        } else {
            curr += ")";
        }
        if (x == n || 2 * n - curr.size() == x) {
            generate(false, x - 1, curr, n);
        } else if (x == 0) {
            generate(true, x + 1, curr, n);
        } else {
            generate(true, x + 1, curr, n);
            generate(false, x - 1, curr, n);
        }
        curr.pop_back();
    }
    vector<string> generateParenthesis(int n) {
        string curr{};
        generate(true, 1, curr, n);
        return ret;
    }
};
