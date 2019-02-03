class Node(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.next = None

class MyHashMap(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.li = [None]*100

    def put(self, key, value):
        """
        value will always be non-negative.
        :type key: int
        :type value: int
        :rtype: void
        """
        hashcode = key%100
        bucket = self.li[hashcode]
        if bucket == None:
            self.li[hashcode] = Node(key, value)
        else:
            curr = bucket
            if curr.key == key:
                curr.val = value
                return
            while curr.next != None:
                curr = curr.next
                if curr.key == key:
                    curr.val = value
                    return
            curr.next = Node(key, value)

    def get(self, key):
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        :type key: int
        :rtype: int
        """
        hashcode = key%100
        bucket = self.li[hashcode]
        if bucket == None:
            return -1
        else:
            curr = bucket
            while curr != None:
                if curr.key == key: return curr.val
                curr = curr.next
        return -1

    def remove(self, key):
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        :type key: int
        :rtype: void
        """
        hashcode = key%100
        bucket = self.li[hashcode]
        if bucket != None:
            curr = bucket
            if curr.key == key:
                self.li[hashcode] = curr.next
                return
            while curr.next != None:
                if curr.next.key == key:
                    curr.next = curr.next.next
                    return
                curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)