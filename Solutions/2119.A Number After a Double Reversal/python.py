class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        return num == 0 or str(num)[-1] != "0"