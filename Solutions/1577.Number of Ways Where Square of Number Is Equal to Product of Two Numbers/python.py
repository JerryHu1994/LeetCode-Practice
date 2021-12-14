class Solution:
    def numTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        nums1_keys = counter1.keys()
        nums2_keys = counter2.keys()
        ans = 0
        for k1 in nums1_keys:
            for k2 in nums1_keys:
                sqrt_num = int(math.sqrt(k1*k2))
                if sqrt_num*sqrt_num != k1*k2:  continue
                if sqrt_num in counter2:
                    if k1 != k2:
                        ans += counter1[k1]*counter1[k2]*counter2[sqrt_num]
                    else:
                        ans += counter1[k1]*(counter1[k1]-1)*counter2[sqrt_num]
        for k1 in nums2_keys:
            for k2 in nums2_keys:
                sqrt_num = int(math.sqrt(k1*k2))
                if sqrt_num*sqrt_num != k1*k2:  continue
                if sqrt_num in counter1:
                    if k1 != k2:
                        ans += counter2[k1]*counter2[k2]*counter1[sqrt_num]
                    else:
                        ans += counter2[k1]*(counter2[k1]-1)*counter1[sqrt_num]
        return int(ans/2)