class Solution(object): 
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(a,b):
            lista = [int(i) for i in str(a)]
            listb = [int(i) for i in str(b)]
            la, lb = len(lista), len(listb)
            l = la*lb
            for i in range(l):
                if lista[i%la] > listb[i%lb]:
                    return 1
                elif lista[i%la] < listb[i%lb]:
                    return -1
            return 0
                    
        nums = sorted(nums, cmp = compare, reverse=True)
        ret = "".join([str(i) for i in nums])
        while len(ret) >=2 and ret[0]=="0":
            ret = ret[1:]
        return ret