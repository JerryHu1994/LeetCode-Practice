/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    pair<int, int> helper(TreeNode *node, int & ans) {
        pair<int, int> ret;
        if (node != NULL) {
            pair<int, int> leftpair = helper(node->left, ans);
            pair<int, int> rightpair = helper(node->right, ans);
            ans = max(ans, max(node->val - min(leftpair.first, rightpair.first), max(leftpair.second, rightpair.second) - node->val));
            ret.first = min(node->val, min(leftpair.first, rightpair.first));
            ret.second = max(node->val, max(leftpair.second, rightpair.second));
        } else {
            ret.first = 1000001;
            ret.second = -1;
        }
        return ret;
    }
    int maxAncestorDiff(TreeNode* root) {
        int ans = 0;
        helper(root, ans);
        return ans;
    }
    
};