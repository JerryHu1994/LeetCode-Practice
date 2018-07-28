class Solution:
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        counts = [0, 0, 0]
        for i in bills:
            if i == 5:
                counts[0] += 1
            elif i == 10:
                if counts[0] == 0:
                    return False
                else:
                    counts[0] -= 1
                counts[1] += 1
            else:
                if counts[1] > 0:
                    counts[1] -= 1
                    if counts[0] > 0:
                        counts[0] -= 1
                    else:
                        return False
                else:
                    if counts[0] > 2:
                        counts[0] -= 3
                    else:
                        return False
                counts[2] += 1
        return True