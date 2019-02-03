class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        ind = bisect.bisect_left(arr, x)
        if ind == len(arr):
            left, right = ind-2, ind-1
        else:
            left, right = ind-1, ind
        small, large = [], []
        count = 0
        while left >=0 and right < len(arr) and count != k:
            if abs(arr[left]-x) <= abs(arr[right]-x):
                small.append(arr[left])
                left -= 1
            else:
                large.append(arr[right])
                right += 1
            count += 1
        for i in range(k-count):
            if left >=0 :
                small.append(arr[left])
                left -= 1
            if right < len(arr):
                large.append(arr[right])
                right += 1
        return small[::-1]+large