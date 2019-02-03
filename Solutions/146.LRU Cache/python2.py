class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.dic = {}
        self.cap = capacity
        self.size = 0
        self.head.next, self.tail.prev = self.tail, self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dic: return -1
        ret = self.dic[key].val
        self.removeNode(key)
        self.appendNode(key, ret)
        return ret

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # check if the cache is full or key in cache
        if key in self.dic:
            self.removeNode(key)
        elif self.size == self.cap:
            # remove the first node
            self.removeNode(self.head.next.key)
        else:
            self.size += 1
        # append new node in the end
        self.appendNode(key, value)
            
    def removeNode(self, key):
        node = self.dic[key]
        prevnode, nextnode = node.prev, node.next
        prevnode.next, nextnode.prev = nextnode, prevnode
        del self.dic[key]
        
    def appendNode(self, key, val):
        newNode = Node(key, val)
        self.dic[key] = newNode
        lastnode = self.tail.prev
        lastnode.next, newNode.prev, newNode.next, self.tail.prev = newNode, lastnode, self.tail, newNode
    
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)