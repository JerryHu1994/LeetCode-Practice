class Solution:
    def nonSpecialCount(self, l: int, r: int) -> int:
        lower = int(sqrt(l))
        upper = int(sqrt(r))
        def isPrime(num):
            if num == 1:
                return False
            if num == 2:
                return True
            for i in range(2, int(sqrt(num))+2):
                if num % i == 0:
                    return False
            return True
        s = set()
        cnt = 0
        for num in range(lower, upper+1):
            if num**2 >= l and num**2 <= r:
                if isPrime(num):
                    cnt += 1
        return r-l+1-cnt