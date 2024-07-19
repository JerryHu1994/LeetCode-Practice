class Solution:
    def smallestNumber(self, pattern: str) -> str:
        nums = [1,2,3,4,5,6,7,8,9]
        def backtrack(currans, visited):
            if len(currans) == len(pattern)+1:
                self.ans = min(self.ans, currans)
                return
            iteratelist = []
            if pattern[len(currans)-1] == "I":
                iteratelist = [i for i in range(int(currans[-1]), len(nums))]
            else:
                iteratelist = [i for i in range(0, int(currans[-1])-1)]
            for i in iteratelist:
                if nums[i] not in visited:
                    visited.add(nums[i])
                    backtrack(currans+str(nums[i]), visited)
                    visited.remove(nums[i])
        self.ans = "9"*(len(pattern)+1)
        for n in nums:
            backtrack(str(n), set([n]))
        return self.ans
    