
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        visited,ret = [0]*len(M), 0
        for i in range(len(M)):
            if visited[i]==0:#do dfs on each unvisited student
                ret+=1
                stack, visited[i] = [i], 1
                while len(stack)!=0:
                    curr = stack.pop()
                    for j in range(len(M)):
                        if M[curr][j]==1 and visited[j]==0:
                            visited[j]=1
                            stack.append(j)
        return ret