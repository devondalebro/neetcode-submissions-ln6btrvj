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
    int maxSum{INT_MIN};
    int maxPath(TreeNode* root) {
        if (!root) return 0;
        auto ret{root->val};
        auto leftMax{maxPath(root->left)};
        auto rightMax{maxPath(root->right)};
        if (leftMax > 0 || rightMax > 0) {
            if (leftMax > rightMax) {
                ret += leftMax;
            } else {
                ret += rightMax;
            }
        }
        maxSum = max(maxSum, ret);
        maxSum = max(maxSum, root->val + leftMax + rightMax);
        cout << root->val << " " << maxSum << "\n";
        return ret;
    }
    int maxPathSum(TreeNode* root) {
        maxPath(root);
        return maxSum;
    }
};
