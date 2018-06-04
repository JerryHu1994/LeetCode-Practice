class Solution(object):
    
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        arr = [0]*len(s)
        if len(s)==0:   return 0
        if int(s[0])==0:    return 0
        arr[0] = 1 
        if len(s) == 1: return arr[0]
        arr[1] = 0
        if int(s[1])!=0:    arr[1]+=1
        if int(s[0]) == 1 or (int(s[0]) == 2 and int(s[1]) <= 6):
            arr[1] += 1 
        if len(s) == 2: return arr[1]
        for i in range(2, len(s)):
            curr = arr[i-1] if (int(s[i])!=0) else 0
            if int(s[i-1]) == 1 or (int(s[i-1])==2 and int(s[i])<=6):
                curr += arr[i-2]
            arr[i] = curr
        return arr[-1]
        