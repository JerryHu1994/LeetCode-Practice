class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        arr1_set = set()
        for array in arr1:
            arrstr = str(array)
            for i in range(1,len(arrstr)+1):
                arr1_set.add(arrstr[0:i])
        ans = 0 
        for array in arr2:
            arrstr = str(array)
            for i in range(len(arrstr)+1, 0, -1):
                if arrstr[0:i] in arr1_set:
                    ans = max(ans, len(arrstr[0:i]))
                    break
        return ans