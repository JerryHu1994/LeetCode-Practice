# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_ptr = head
        curr_count = 1
        while curr_ptr != None:
            curr_list = []
            temp_count = 0
            temp_ptr = curr_ptr
            for i in range(curr_count):
                if temp_ptr == None:
                    break
                curr_list.append(temp_ptr.val)
                temp_ptr = temp_ptr.next
                temp_count += 1
            curr_list = curr_list[::-1]
            if temp_count % 2 == 0:
                for i in range(curr_count):
                    if curr_ptr == None:
                        break
                    curr_ptr.val = curr_list[i]
                    curr_ptr = curr_ptr.next
            else:
                curr_ptr = temp_ptr
            curr_count += 1
        return head