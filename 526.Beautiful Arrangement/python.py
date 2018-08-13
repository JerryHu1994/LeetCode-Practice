class Solution(object):
    def helper(self, start, N, visited):
        if start > N:
            self.count += 1
            return
        for i in range(1, N+1):
            if not visited[i-1] and (start%i==0 or i%start==0):
                visited[i-1] = True
                self.helper(start+1, N, visited)
                visited[i-1] = False
    
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        visited = [False]*N
        self.count = 0
        self.helper(1, N, visited)
        return self.count