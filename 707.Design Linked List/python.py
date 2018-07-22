class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        curr = self.head
        for i in range(index):
            if curr == None:    return -1
            curr = curr.next
        return curr.val if curr!= None else -1

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: void
        """
        newHead = Node(val)
        newHead.next = self.head
        self.head = newHead
        
    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: void
        """
        newTail = Node(val)
        curr = self.head
        if curr == None:
            self.head = newTail
            return
        while curr.next != None:    curr = curr.next
        curr.next = newTail

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: void
        """
        if index == 0:
            self.addAtHead(val)
            return
        curr = self.head
        for i in range(index-1):
            if curr == None:    return
            curr = curr.next
        if curr == None:    return
        newNode = Node(val)
        newNode.next = curr.next
        curr.next = newNode

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index == 0:
            if self.head == None:
                return
            else:
                self.head = self.head.next
        curr = self.head
        for i in range(index-1):
            if curr == None:    return
            curr = curr.next
        if curr != None and curr.next != None:
            curr.next = curr.next.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)