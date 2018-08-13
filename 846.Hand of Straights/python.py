class Solution(object):
    def isNStraightHand(self, hand, W):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand)%W != 0:
            return False
        dic = collections.defaultdict(int)
        for i in hand:
            dic[i] += 1
        ite = len(hand)/W
        for i in range(ite):
            mini = sorted(dic.keys())[0]
            curr = mini
            for i in range(W):
                if dic[curr] > 0:
                    dic[curr] -= 1
                else:
                    return False
                if dic[curr] == 0:  del dic[curr]
                curr += 1
        return True