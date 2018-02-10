class Node:
    def __init__(self, key, val):
        self.k = key
        self.v = val
        self.next = None
        self.pre = None
    

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = dict()
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.cap = capacity
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.dic:
            node = self.dic[key]
            value = node.v
            #remove from DLlist
            self.removeNode(node)
            #add to tail of DLlist
            self.appendNode(node)
            return value
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.dic:
            #already in, remove node, append to tail
            node = self.dic[key]
            node.v = value
            self.removeNode(node)
            self.appendNode(node)
            return
        if len(self.dic) >= self.cap:
            #if the cache is full, remove from the head
            toRemove = self.head.next
            self.removeNode(toRemove)
            del self.dic[toRemove.k]
        #create a new node, insert to dict, append
        newnode = Node(key, value)
        self.dic[key] = newnode
        self.appendNode(newnode)
        
    def removeNode(self, n):
        prenode = n.pre
        nextnode = n.next
        prenode.next = nextnode
        nextnode.pre = prenode
        
    def appendNode(self, n):
        prenode = self.tail.pre
        prenode.next = n
        n.pre = prenode
        n.next = self.tail
        self.tail.pre = n
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)