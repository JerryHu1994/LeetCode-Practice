class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        ind = 0
        original = len(arr)
        while ind < len(arr):
            if arr[ind] == 0:
                arr.insert(ind+1, 0)
                ind = ind+2
            else:
                ind += 1
        while len(arr) > original:
            arr.pop()