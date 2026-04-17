/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */

class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> ret{};
        queue<pair<TreeNode*, int>> next{};
        if (root) next.push({root, 0});
        while (!next.empty()) {
            const auto top{next.front()};
            next.pop();
            if (top.second + 1 > ret.size()) ret.push_back({});
            ret[top.second].push_back(top.first->val);
            if (top.first->left) next.push({top.first->left, top.second + 1});
            if (top.first->right) next.push({top.first->right, top.second + 1});
        }
        return ret;
    }
};
