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
    bool isCousins(TreeNode* root, int x, int y) {
        if (root == NULL)   return false;
        queue <TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            queue <TreeNode*> nextq;
            set <int> s;
            unordered_map <int, int> parents;
            while (!q.empty()) {
                TreeNode* curr = q.front();
                q.pop();
                if (curr->left != NULL) {
                    s.insert(curr->left->val);
                    parents[curr->left->val] = curr->val;
                    nextq.push(curr->left);
                }
                if (curr->right != NULL) {
                    s.insert(curr->right->val);
                    parents[curr->right->val] = curr->val;
                    nextq.push(curr->right);
                }
            }
            if (s.find(x) != s.end() && s.find(y) != s.end() && parents[x] != parents[y]) {
                return true;
            } else if (s.find(x) != s.end() || s.find(y) != s.end()) {
                return false;
            }
            q = nextq;
        }
        return false;
    }
};