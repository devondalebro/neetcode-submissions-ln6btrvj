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
    int numGood{0};
public:
    void doGood(TreeNode *root, int max) {
        if (!root) return;
        if (root->val >= max) numGood++;
        max = std::max(max, root->val);
        doGood(root->left, max);
        doGood(root->right, max);
    }
    int goodNodes(TreeNode* root) {
        doGood(root, -1000);
        return numGood;
    }
};
