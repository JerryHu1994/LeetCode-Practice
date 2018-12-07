class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        l = len(deck)
        if l == 0:  return []
        q = [i for i in range(l)]
        order = []
        while True:
            order.append(q.pop(0))
            if len(q) == 0: break
            q.append(q.pop(0))
        ret = [None]*l
        sort = sorted(deck)
        for ind, pos in enumerate(order):
            ret[pos] = sort[ind]
        return ret