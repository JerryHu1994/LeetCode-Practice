class Solution:
    def checkZeroOnes(self, s: str) -> bool:
        longest_zero, longest_one = 0, 1
        curr_ind, curr_cnt = '1', 0
        for i in s:
            if i == '1':
                if curr_ind == '1':
                    curr_cnt += 1
                else:
                    curr_ind, curr_cnt = '1', 1
                longest_one = max(longest_one, curr_cnt)
            else:
                if curr_ind == '0':
                    curr_cnt += 1
                else:
                    curr_ind, curr_cnt = '0', 1
                longest_zero = max(longest_zero, curr_cnt)
        return longest_one > longest_zero
        