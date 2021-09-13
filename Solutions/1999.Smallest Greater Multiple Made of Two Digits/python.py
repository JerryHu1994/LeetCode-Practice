class Solution:
    def findInteger(self, k: int, digit1: int, digit2: int) -> int:
        upbound = 1 << 31
        for i in range(1, 11):
            # use product to generate possible numbers. 
            for seq in product([min(digit1,digit2), max(digit1,digit2)], repeat = i):
                num = 0
                for n in seq:
                    num = num * 10
                    num += n
                    if num > k and num % k == 0 and num < upbound: return num
        return -1