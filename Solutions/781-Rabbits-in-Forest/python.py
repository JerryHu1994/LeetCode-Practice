class Solution(object):
    def numRabbits(self, answers):
        """
        :type answers: List[int]
        :rtype: int
        """
        cnt = collections.Counter(answers)
        ret = 0
        for k, v in cnt.items():
            num = math.ceil(float(v)/(k+1))
            ret += int(num)*(k+1)
        return ret