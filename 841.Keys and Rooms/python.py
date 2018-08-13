class Solution(object):
    def dfs(self,i, rooms, visited):
        if visited[i]:  return
        visited[i] = True
        for j in rooms[i]:
            if not visited[j]:
                self.dfs(j, rooms, visited)
        
    
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visited = [False]*(len(rooms))
        self.dfs(0, rooms, visited)
        for i in visited:
            if not i:   return False
        return True