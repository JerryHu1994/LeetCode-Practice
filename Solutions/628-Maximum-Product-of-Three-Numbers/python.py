class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pos, neg = [], []
        for i in nums:
            if i > 0:
                if len(pos) < 3:
                    pos.append(i)
                elif i > pos[0]:
                    pos[0] = i
                pos.sort()
            else:
                if len(neg) < 3:
                    neg.append(i)
                elif i < neg[-1]:
                    neg[-1] = i
                neg.sort()
        if len(neg) == 3:
            if len(pos) == 0:   return neg[0]*neg[1]*neg[2]
            if len(pos) == 1:   return pos[0]*neg[0]*neg[1]
            if len(pos) == 2:   return pos[1]*neg[0]*neg[1]
            return pos[0]*pos[1]*pos[2] if pos[0]*pos[1] > neg[0]*neg[1] else neg[0]*neg[1]*pos[2]
        if len(neg) == 2:
            if len(pos) == 1:   return pos[0]*neg[0]*neg[1]
            if len(pos) == 2:   return pos[1]*neg[0]*neg[1]
            return pos[0]*pos[1]*pos[2] if pos[0]*pos[1] > neg[0]*neg[1] else neg[0]*neg[1]*pos[2]
        if len(neg) == 1:
            if len(pos) == 3:
                return pos[0]*pos[1]*pos[2]
            else:
                return neg[0]*pos[0]*pos[1]
        return pos[0]*pos[1]*pos[2]