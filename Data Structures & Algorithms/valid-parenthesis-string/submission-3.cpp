class Solution {
public:
    bool checkValidString(string s) {
        std::stack<int> ast{};
        std::stack<int> paren{};
        for (auto i{0}; i < s.size(); ++i) {
            if (s[i] == '*') {
                ast.push(i);
            } else if (s[i] == '(') {
                paren.push(i);
            } else {
                if (paren.size() != 0) {
                    paren.pop();
                } else {
                    if (ast.size() == 0) {
                        return false;
                    } else {
                        ast.pop();
                    }
                }
            }
        }
        while (paren.size() > 0) {
            if (ast.size() == 0) {
                return false;
            } else if (paren.top() > ast.top()) {
                return false;
            } else {
                paren.pop();
                ast.pop();
            }
        }
        return true;
    }
};
