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
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // we have three cases a->c<-b, a->b, b<-a
        // anyhow its just the case that 
        if (p->val >= q->val) swap(p, q);
        if (!root) return root;
        if (root->val >= p->val && root->val <= q->val) return root;
        auto leftRet{lowestCommonAncestor(root->left, p, q)};
        if (leftRet) return leftRet;
        return lowestCommonAncestor(root->right, p, q);
    }
};
