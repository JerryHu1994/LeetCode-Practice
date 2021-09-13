class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.parent = None
        self.children = []

class LockingTree:

    def __init__(self, parent: List[int]):
        self.nodelist = []
        self.lockdic = {}
        for i in range(len(parent)):
            self.nodelist.append(TreeNode(i))
        self.nodelist[0].parent = TreeNode(-1)
        for ind in range(1, len(parent)):
            self.nodelist[ind].parent = self.nodelist[parent[ind]]
            self.nodelist[parent[ind]].children.append(self.nodelist[ind])

    def lock(self, num: int, user: int) -> bool:
        if num not in self.lockdic:
            self.lockdic[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.lockdic and self.lockdic[num] == user:
            del self.lockdic[num]
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        cond1 = num not in self.lockdic
        cond2 = self.no_lock_ancestor(self.nodelist[num])
        cond3 = self.one_locked_descendant(self.nodelist[num])
        if cond1 and cond2 and cond3:
            self.unlock_all_descendants(self.nodelist[num])
            self.lock(num, user)
            return True
        else:
            return False
    
    def unlock_all_descendants(self, node) -> bool:
        queue = []
        queue += node.children
        while len(queue) > 0:
            curr = queue.pop()
            if curr.val in self.lockdic:
                del self.lockdic[curr.val]
            queue += curr.children
    
    def one_locked_descendant(self, node) -> bool:
        queue = []
        queue += node.children
        while len(queue) > 0:
            curr = queue.pop()
            if curr.val in self.lockdic:   return True
            queue += curr.children
        return False
    
    def no_lock_ancestor(self, node) -> bool:
        if node.val == -1:  return True
        if node.val in self.lockdic:   return False
        return self.no_lock_ancestor(node.parent)


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)