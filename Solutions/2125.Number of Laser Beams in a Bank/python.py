class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev_count = None
        for laser_row in bank:
            curr_count = laser_row.count('1')
            if curr_count != 0:
                if prev_count != None:
                    ans += prev_count*curr_count
                prev_count = curr_count
        return ans