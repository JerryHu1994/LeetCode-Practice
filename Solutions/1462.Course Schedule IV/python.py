class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        ans = []
        pre_map = defaultdict(list)
        for from_course, to_course in prerequisites:
            pre_map[from_course].append(to_course)
        @lru_cache
        def bfs(startidx, endidx):
            queue = [startidx]
            visited = set([startidx])
            while len(queue):
                curr_idx = queue.pop(0)
                for nextidx in pre_map[curr_idx]:
                    if nextidx == endidx:   return True
                    if nextidx not in visited:
                        queue.append(nextidx)
                        visited.add(nextidx)
            return False
        for from_course, to_course in queries:
            ans.append(bfs(from_course, to_course))
        return ans