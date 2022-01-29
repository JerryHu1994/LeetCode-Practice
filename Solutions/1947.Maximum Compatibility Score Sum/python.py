class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        l, s = len(students), len(students[0])
        self.ans = 0
        def dfs(ind, visited, score):
            if ind == l:
                self.ans = max(self.ans, score)
                return
            for mentor_idx in range(l):
                if mentor_idx not in visited:
                    visited.add(mentor_idx)
                    currscore = sum(a==b for a, b in zip(students[ind], mentors[mentor_idx]))
                    dfs(ind+1, visited, currscore+score)
                    visited.remove(mentor_idx)
        dfs(0, set(), 0)
        return self.ans