from functools import lru_cache
class Solution:
    @lru_cache(None)
    def divisorGame(self, N: int) -> bool:
        if N == 0 or N == 1:  return False
        if N == 2:  return True
        if all(self.divisorGame(N-f)  for f in range(1, int(math.sqrt(N))+1) if N%f == 0):
            return False
        return True