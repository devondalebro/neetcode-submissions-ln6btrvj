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
    unordered_map<int, int> inorderIdx{};
public:
    TreeNode* build(const vector<int>& preorder, int preL, int preR,
    const vector<int>& inorder, int inL, int inR) {
        if (preL == preR) return nullptr;
        auto rootVal{preorder[preL]};
        TreeNode* root{new TreeNode(rootVal)};
        auto rootValInorderIdx{inorderIdx[rootVal]};
        auto leftSubtreeSize{rootValInorderIdx - inL};
        auto rightSubtreeSize{inR - rootValInorderIdx + 1};
        root->left = build(preorder, preL + 1, preL + 1 + leftSubtreeSize, inorder, inL, rootValInorderIdx);
        root->right = build(preorder, preL + 1 + leftSubtreeSize, preR, inorder, rootValInorderIdx + 1, inR);
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (auto i{0}; i < preorder.size(); ++i) {
            inorderIdx[inorder[i]] = i;
        }
        return build(preorder, 0, preorder.size(), inorder, 0, inorder.size());
    }
};
