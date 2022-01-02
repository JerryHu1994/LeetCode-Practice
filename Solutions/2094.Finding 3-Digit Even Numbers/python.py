class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        digits = sorted(digits)
        int_set = set()
        l = len(digits)
        for first_ind in range(l):
            first = digits[first_ind]
            if first == 0:  continue
            for second_ind in range(l):
                if second_ind == first_ind: continue
                second = digits[second_ind]
                for third_ind in range(l):
                    if third_ind == first_ind or third_ind == second_ind:   continue
                    if digits[third_ind]%2 == 0:
                        third = digits[third_ind]
                        num = 100*first+10*second+third
                        int_set.add(num)
        return sorted(list(int_set))