class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        diff = [gas[i] - cost[i]    for i in range(len(gas))]
        for i in range(len(diff)):
            currsum = 0
            count = 0
            for j in diff[i:] + diff[:i]:
                currsum += j
                if currsum < 0:
                    break
                count += 1
            if count == len(diff):  return i
        return -1
            