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
    bool doValid(TreeNode* root, int min, int max) {
        if (!root) return true;
        if (root->val <= min || root->val >= max) return false;
        return doValid(root->left, min, root->val) && doValid(root->right, root->val, max);
    }
    bool isValidBST(TreeNode* root) {
        return doValid(root, -1001, 1001);
    }
};
