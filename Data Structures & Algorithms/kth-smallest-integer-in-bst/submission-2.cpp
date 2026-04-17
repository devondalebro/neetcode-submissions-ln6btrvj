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
    int kth{0};
public:
    int traverse(TreeNode* root, int k) {
        if (!root) return -1;
        auto ret{traverse(root->left, k)};
        if (ret != -1) return ret;
        kth++;
        if (kth == k) return root->val;
        return traverse(root->right, k);
    }
    int kthSmallest(TreeNode* root, int k) {
        return traverse(root, k);
    }
};
