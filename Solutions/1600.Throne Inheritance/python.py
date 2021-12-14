class ThroneInheritance:

    def __init__(self, kingName: str):
        self.throne_map = defaultdict(list)
        self.king = kingName
        self.dead_people = set()

    def birth(self, parentName: str, childName: str) -> None:
        self.throne_map[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead_people.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = []
        stack = [self.king]
        def dfs(node):
            if node not in self.dead_people:
                res.append(node)
            for nextnode in self.throne_map[node]:
                dfs(nextnode)
        dfs(self.king)
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()