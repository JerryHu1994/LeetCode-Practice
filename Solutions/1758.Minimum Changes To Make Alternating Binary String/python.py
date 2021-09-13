class Solution:
    def minOperations(self, s: str) -> int:
        first_one, first_zero = 0, 0 #1010, 0101
        for ind, val in enumerate(s):
            if ind%2 == 0:
                if val == '1':
                    first_zero += 1
                else:
                    first_one += 1
            else:
                if val == '1':
                    first_one += 1
                else:
                    first_zero += 1
                
        return min(first_one, first_zero)