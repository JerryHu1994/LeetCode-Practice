class Solution:
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        balances = collections.defaultdict(int)
        for fro, to, amount in transactions:
            balances[fro] += amount
            balances[to] -= amount
        # save all non-zero balances
        b = [v for v in balances.values() if v != 0]
        cnt = len(b)
        # find the minimal groups of balances adds up to zero
        def helper(bal, target, pre, start):
            if target == 0: return pre
            n = len(bal)
            if start == n:    return None
            ans = None
            for i in range(start, n):
                ret = helper(bal, target+bal[i], pre+[i], i+1)
                if ret != None:
                    if ans == None or len(ret) < len(ans): ans = ret
            return ans
        while len(b) > 0:
            remove = helper(b, b[0], [0], 1)
            remove = set(remove)
            b = [val for ind, val in enumerate(b) if ind not in remove]
            cnt -= 1
        return cnt