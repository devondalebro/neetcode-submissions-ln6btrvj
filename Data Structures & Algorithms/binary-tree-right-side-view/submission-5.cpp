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
    void rightSide(TreeNode* root, vector<int>& ret, int lvl) {
        if (!root) return;
        if (lvl + 1 > ret.size()) ret.push_back(0);
        ret[lvl] = root->val;
        rightSide(root->left, ret, lvl + 1);
        rightSide(root->right, ret, lvl + 1);
    }
    vector<int> rightSideView(TreeNode* root) {
        vector<int> ret{};
        rightSide(root, ret, 0);
        return ret;
    }
};
