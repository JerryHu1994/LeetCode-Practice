/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* oddEvenList(ListNode* head) {
        if (head == NULL)
            return head;
        ListNode* evenhead = new ListNode(0);
        ListNode* oddhead = new ListNode(0);
        ListNode* even = evenhead;
        ListNode* odd = oddhead;
        ListNode* curr = head;
        int cnt = 0;
        while (curr != NULL) {
            if (cnt%2==0) {
                even->next = curr;
                even = even->next;
            }else{
                odd->next = curr;
                odd = odd->next;
            }
            cnt += 1;
            curr = curr->next;
        }
        odd->next = NULL;
        even->next = oddhead->next;
        return evenhead->next;
    }
};