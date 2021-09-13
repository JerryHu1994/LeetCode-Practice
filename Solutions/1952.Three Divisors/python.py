class Solution:
    def isPrime(self, n:int) -> bool:
        for i in range(2, int(n/2)):
            if n%i == 0:    return False
        return True
    
    def isThree(self, n: int) -> bool:
        if n == 1:  return False
        return int(int(math.sqrt(n)) ** 2) == n and self.isPrime(int(math.sqrt(n)))