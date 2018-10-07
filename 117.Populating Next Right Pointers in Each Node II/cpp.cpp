/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
class Solution {
public:
    void connect(TreeLinkNode *root) {
        if (root == NULL)   return;
        vector<TreeLinkNode*>pre;
        pre.push_back(root);
        while (!pre.empty()) {
            vector<TreeLinkNode*>next;
            for (int i=0; i<int(pre.size());i++) {
                if (pre[i]->left != NULL)   next.push_back(pre[i]->left);
                if (pre[i]->right != NULL)   next.push_back(pre[i]->right);
            }
            for (int i=0;i<int(next.size())-1;i++) {
                next[i]->next = next[i+1];
            }
            pre = next;
        }
    }
};