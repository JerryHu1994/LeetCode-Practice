class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
        self.freq = 1
    
class dQueue(object):
    def __init__(self):
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.size = 0
        self.head.next, self.tail.prev = self.tail, self.head
            
    def removeNode(self, node):
        prevnode, nextnode = node.prev, node.next
        prevnode.next, nextnode.prev = nextnode, prevnode
        self.size -= 1
        
    def appendNode(self, newNode):
        lastnode = self.tail.prev
        lastnode.next, newNode.prev, newNode.next, self.tail.prev = newNode, lastnode, self.tail, newNode
        self.size += 1
        
class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.dic = {}
        self.freqMap = collections.defaultdict(dQueue)
        self.cap = capacity
        self.minfreq = 0
        self.totalsize = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.cap <= 0:   return -1
        if key not in self.dic: return -1
        currnode = self.dic[key]
        currfreq = currnode.freq
        currdlist = self.freqMap[currfreq]
        # remove the key from current frequency
        currdlist.removeNode(currnode)
        currnode.freq += 1
        # add the key to next frequency level
        self.freqMap[currnode.freq].appendNode(currnode)
        # increment minfreq if current list is empty
        if self.freqMap[self.minfreq].size == 0:    self.minfreq += 1
        return currnode.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.cap <= 0:   return
        if key in self.dic:
            # keep the key in the same level, update the value
            currnode = self.dic[key]
            currnode.val = value
            # increase its frequency
            currfreq = self.freqMap[currnode.freq]
            currfreq.removeNode(currnode)
            currnode.freq += 1
            self.freqMap[currnode.freq].appendNode(currnode)
            if self.freqMap[self.minfreq].size == 0:    self.minfreq += 1
            return
        elif self.totalsize == self.cap:
            # throw away the head key in the minfreq
            minlist = self.freqMap[self.minfreq]
            k = minlist.head.next.key
            minlist.removeNode(minlist.head.next)
            del self.dic[k]
        else:
            self.totalsize += 1
        # create a new key, append to freq 1, reset the minfreq
        newNode = Node(key, value)
        self.freqMap[1].appendNode(newNode)
        self.dic[key] = newNode
        self.minfreq = 1
        
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)